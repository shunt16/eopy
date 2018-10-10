"""
Data factory for opening Sentinel-3/OLCI L1b data
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from datetime import datetime as dt
from datetime import timedelta
from copy import deepcopy

'''___Third-Party Modules___'''
import snappy
import xarray as xr
import jpy
from numpy import zeros, asarray, uint32, float32, full, bool_, ndarray, array
import numpy.ma as ma
from datetime import datetime
from astropy.time import Time


'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractDataFactory import AbstractDataFactory
from Variable import Variable
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2018"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

# todo - acquisition time
# todo - finalise contents of self.attributes
# todo - getData apply_mask kwarg


class SnappySharedFactory(AbstractDataFactory):
    """
    SnappySharedFactory contains common factory functionality from the snappy library

    :Methods:
        .. py:method:: openProduct(...):

           Opens an in-memory representation of data product specified by product_path.

        .. py:method:: openMultipleProducts(...):

            Opens a dictionary of in-memory representations of multiple snappy data products

        .. py:method:: createDataVariable(...):

            Returns "data" type `SpectralVariable` class objects, for given product variable

        .. py:method:: getDataVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: createMaskVariable(...):

            Returns "mask" type `Variable` class objects, for given product variable

        .. py:method:: getMaskVariableNames(...):

            Returns list of product "mask" type variable names

        .. py:method:: createMeteorologicalVariable(...):

            Returns "meteorological" type `Variable` class objects, for given product variable

        .. py:method:: getMeteorologicalVariableNames(...):

            Returns list of product "meteorological" type variable names

        .. py:method:: createSensorVariable(...):

            Returns "sensor" type `Variable` class objects, for given product variable

        .. py:method:: getSensorVariableNames(...):

            Returns list of product "sensor" type variable names

        .. py:method:: createInfoVariable(...):

            Returns "info" type `Variable` class objects, for given product variable

        .. py:method:: getInfoVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: determine_getData_product(...):

            Return `snappy.Product` object to get data from for given variables

        .. py:method:: determine_getData_mask(...):

            Return mask to apply to data when opened

        .. py:method:: getData(...):

            Returns variable[s] of in-memory product as an xarray data structure.

        .. py:method:: getPixelValues(...):

            Returns pixel values of variable of in-memory product

        :Inherited from eopy.product.productIO.AbstractDataFactory.AbstractDataFactory:
            .. py:method:: readVariables(...):

                Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

            .. py:method:: getDataVariables(...):

                Returns list of product "data" type variables as ``Variable`` or `SpectralVariable` class objects.

            .. py:method:: editDataVariable(...):

                Returns 'data' variable objects with attributes edited compared to default values obtained from product

            .. py:method:: getMaskVariables(...):

                Returns list of product "mask" type variables as ``Variable`` class objects.

            .. py:method:: editMaskVariable(...):

                Returns 'mask' variable objects with attributes edited compared to default values obtained from product

            .. py:method:: getMeteorologicalVariables(...):

                Returns list of product "meteorological" type variables as ``Variable`` class objects.

            .. py:method:: editMeteorologicalVariable(...):

                Returns 'meteorological' variable objects with attributes edited compared to default values obtained
                from product

            .. py:method:: getSensorVariables(...):

                Returns list of product "sensor" type variables as ``Variable`` class objects.

            .. py:method:: editSensorVariable(...):

                Returns 'sensor' variable objects with attributes edited compared to default values obtained from
                product

            .. py:method:: getInfoVariables(...):

                Returns list of product "info" type variables as ``Variable`` class objects.

            .. py:method:: editInfoVariable(...):

                Returns 'info' variable objects with attributes edited compared to default values obtained from product

            . py:method:: readAttributes(...):

                Returns dictionary of product attributes
    """

    def __init__(self):
        """
        Initialise class
        """

        # Mask to apply to in memory data arrays obtained in self.getData() - may be populated during subsetting
        # especially for none rectangular regions of interest

        self.data_mask = None

    def openProduct(self, product_path):
        """
        Opens an in-memory represenation of snappy data product at specified path with metadata

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :products: *list*

            List of dictionaries of in-memory representations of opened data products, entries:

            * 'product_name' - name of product
            * 'product' - snappy.Product object
            * 'variable' - variables that can be opened from product

            In this case just one element in list, though can contain multiple elements - for example, for product
            opened in each of it's different spatial resolutions (e.g. for Sentinel-2 products)

            :variables: *list*

            list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

            :attributes: *dict*

            Dictionary of product attributes.
        """

        # 1. Open product/s with snappy functionality
        product = snappy.ProductIO.readProduct(product_path)
        products = [{"product_name": product.getName(),
                     "product": product}]

        # 2. Populate variables and attributes dictionaries with product metadata
        # a. populate variables
        products, variables = self.readVariables(products)

        # b. populate attributes
        products, attributes = self.readAttributes(products)
        products, attributes = self.addAttributes(products, attributes)

        return products, variables, attributes

    def openMultipleProducts(self, product_paths):
        """
        Opens a dictionary of in-memory representations of snappy data products

        :type product_path: list
        :param product_path: List of data products to open, each element of list can define a product as:

        * String of path to open
        * Dictionary defining product, with entries:

            * 'product_name' - name of product
            * 'product_path' - path of product
            * 'product_reader' - (optional) specific snap reader to use

        :return:
            :product: *dict*

            List of dictionaries of in-memory representations of opened data products, entries:

            * 'product_name' - name of product
            * 'product' - snappy.Product object
            * 'variable' - variables that can be opened from product

            Can contain multiple elements - for example, for product opened in each of it's different spatial
            resolutions (e.g. for Sentinel-2 products)

        """

        # 1. Populate products dictionary with snappy.Product objects
        products = []

        for i, product_path in enumerate(product_paths):
            if type(product_path) == list:
                products.append({"product_name": i,
                                 "product": snappy.ProductIO.readProduct(product_path)})

            elif type(product_path) == dict:
                prod_dict = {"product_name": product_path["product_name"] if "product_name" in product_path.keys() else i}

                if "product_reader" in product_path:
                    reader = snappy.ProductIO.getProductReader(product_path["product_reader"])
                    prod_dict["product"] = reader.readProductNodes(product_path["product_path"], None)
                else:
                    prod_dict["product"] = snappy.ProductIO.readProduct(product_path["product_path"])

                products.append(prod_dict)

        return products

    def readVariables(self, products):
        """
        Returns list of multiple product variables as ``Variable`` or ``SpectralVariable`` class objects and updates
        products dictionary

        :type product: *dict*
        :param product: Dictionary of in-memory representation of `opened snappy.Product` data product

        :return:
            :products: *dict*

            Dictionary of in-memory representation of opened `snappy.Product` data product, with updated variables

            :variables: *list*

            List of products variables as ``Variable`` or ``SpectralVariable`` class objects.
        """

        variables = []
        for i in range(len(products)):
            product_obj = products[i]["product"]
            product_variables = self.getDataVariables(product_obj) + \
                                self.getMaskVariables(product_obj) + \
                                self.getMeteorologicalVariables(product_obj) + \
                                self.getSensorVariables(product_obj) + \
                                self.getInfoVariables(product_obj)
            variables += product_variables
            products[i]["variables"] = [v.name for v in product_variables]

        return products, variables

    def readAttributes(self, products):
        """
        Return dictionary of multiple products attributes

        :type product: *dict*
        :param product: Dictionary of in-memory representation of `opened snappy.Product` data product

        :return:
            :products: *dict*

            Dictionary of in-memory representation of `opened snappy.Product` data product

            :attributes: *list*

            Dictionary of multiple products attributes
        """

        attributes = {"product_name": products[0]["product"].getName(),
                      "product_string": products[0]["product"].getProductType(),
                      "product_type": "satellite",
                      "start_time": datetime.strptime(products[0]["product"].getStartTime().getElemString(),
                                                      '%d-%b-%Y %H:%M:%S.%f'),
                      "end_time": datetime.strptime(products[0]["product"].getEndTime().getElemString(),
                                                    '%d-%b-%Y %H:%M:%S.%f')}

        if len(products) > 1:
            for p in products:
                attributes["product_processing_" + p["product_name"]] = []
                attributes["product_columns_" + p["product_name"]] = p["product"].getSceneRasterWidth()
                attributes["product_rows_" + p["product_name"]] = p["product"].getSceneRasterHeight()
        else:
            attributes["product_processing"] = []
            attributes["product_columns"] = products[0]["product"].getSceneRasterWidth()
            attributes["product_rows"] = products[0]["product"].getSceneRasterHeight()

        return products, attributes

    def addAttributes(self, products, attributes):
        """
        Return updated dictionary of multiple products attributes

        :type product: dict
        :param product: Dictionary of in-memory representation of `opened snappy.Product` data product

        :type attributes: dict
        :param attributes: Dictionary of multiple products attributes

        :return:
            :products: *dict*

            Dictionary of in-memory representation of `opened snappy.Product` data product

            :attributes: *list*

            Dictionary of multiple products attributes
        """

        return products, attributes

    def createDataVariable(self, product, variable_name):
        """
        Returns "data" type `SpectralVariable` class objects, for given product variable

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :data_variable: *eopy.product.productIO.SpectralVariable.SpectraVariable*

            ``SpectralVariable`` object for given product 'data' variable
        """

        spectral_variable = False
        tiepointgrid = False

        if variable_name in list(product.getBandNames()):
            if product.getBand(variable_name).getSpectralWavelength() > 0.0:
                spectral_variable = True
        else:
            tiepointgrid = True

        if spectral_variable:
            data_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'data',
                                  'units': product.getBand(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                            int(product.getBand(variable_name).getRasterHeight())),
                                  'wavelength': product.getBand(variable_name).getSpectralWavelength(),
                                  'bandwidth': product.getBand(variable_name).getSpectralBandwidth(),
                                  'srf': None}
            data_variable = SpectralVariable(data_variable_dict)
        elif not tiepointgrid:
            data_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'data',
                                  'units': product.getBand(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                            int(product.getBand(variable_name).getRasterHeight()))}
            data_variable = Variable(data_variable_dict)
        else:
            data_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'data',
                                  'units': product.getTiePointGrid(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getSceneRasterWidth()), int(product.getSceneRasterHeight()))}
            data_variable = Variable(data_variable_dict)

        return data_variable

    def getDataVariableNames(self, product):
        """
        Returns list of product "data" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :data_variable_names: *list*

            List of product "data" type variable names
        """

        all_variables_names = list(product.getBandNames()) + list(product.getTiePointGridNames())

        # Remove info variables
        data_variable_names = [v for v in all_variables_names if v not in self.getInfoVariableNames(product)]

        return data_variable_names

    def createMaskVariable(self, product, variable_name):
        """
        Returns "mask" type `Variable` class objects, for given product variable

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :mask_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'mask' variable
        """

        mask_variable_dict = {'name': variable_name,
                              'dtype': 'float',
                              'vtype': 'mask',
                              'units': None,
                              'ndims': 2,
                              'shape': (int(product.getSceneRasterWidth()), int(product.getSceneRasterHeight()))}

        mask_variable = Variable(mask_variable_dict)

        return mask_variable

    def getMaskVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :mask_variable_names: *list*

            List of product "mask" type variable names
        """

        return list(product.getMaskGroup().getNodeNames())

    def createMeteorologicalVariable(self, product, variable_name):
        """
        Returns "meteorological" type `Variable` class objects, for given product variable

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :meteorological_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'meteorological' variable
        """

        spectral_variable = False
        tiepointgrid = False
        mask = False

        if variable_name in list(product.getBandNames()):
            if product.getBand(variable_name).getSpectralWavelength() > 0.0:
                spectral_variable = True
        elif variable_name not in list(product.getMaskGroup().getNodeNames()):
            tiepointgrid = True
        else:
            mask = True

        if spectral_variable:
            meteorological_variable_dict = {'name': variable_name,
                                            'dtype': 'float',
                                            'vtype': 'meterological',
                                            'units': product.getBand(variable_name).getUnit(),
                                            'ndims': 2,
                                            'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                                      int(product.getBand(variable_name).getRasterHeight())),
                                            'wavelength': product.getBand(variable_name).getSpectralWavelength(),
                                            'bandwidth': product.getBand(variable_name).getSpectralBandwidth(),
                                            'srf': None}
            meteorological_variable = SpectralVariable(meteorological_variable_dict)
        elif not tiepointgrid:
            meteorological_variable_dict = {'name': variable_name,
                                            'dtype': 'float',
                                            'vtype': 'meteorological',
                                            'units': product.getBand(variable_name).getUnit(),
                                            'ndims': 2,
                                            'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                                      int(product.getBand(variable_name).getRasterHeight()))}
            meteorological_variable = Variable(meteorological_variable_dict)
        else:
            meteorological_variable_dict = {'name': variable_name,
                                            'dtype': 'float',
                                            'vtype': 'meteorological',
                                            'units': product.getTiePointGrid(variable_name).getUnit(),
                                            'ndims': 2,
                                            'shape': (int(product.getSceneRasterWidth()), int(product.getSceneRasterHeight()))}
            meteorological_variable = Variable(meteorological_variable_dict)

        return meteorological_variable

    def getMeteorologicalVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :meteorological_variable_names: *list*

            List of product "mask" type variable names
        """

        return []

    def createSensorVariable(self, product, variable_name):
        """
        Returns "sensor" type `Variable` class objects, for given product variable

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :sensor_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'sensor' variable
        """

        sensor_variable_dict = {'name': variable_name,
                                'dtype': 'float',
                                'vtype': 'sensor',
                                'units': product.getBand(variable_name).getUnit(),
                                'ndims': 2,
                                'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                          int(product.getBand(variable_name).getRasterHeight()))}

        sensor_variable = Variable(sensor_variable_dict)

        return sensor_variable

    def getSensorVariableNames(self, product):
        """
        Returns list of product "sensor" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :sensor_variable_names: *list*

            List of product "sensor" type variable names
        """

        return []

    def createInfoVariable(self, product, variable_name):
        """
        Returns "info" type `Variable` class objects, for given product variable

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :info_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'info' variable
        """

        spectral_variable = False
        tiepointgrid = False
        mask = False
        time_stamp = False

        if variable_name == "time_stamp":
            time_stamp = True

        if variable_name in list(product.getBandNames()):
            if product.getBand(variable_name).getSpectralWavelength() > 0.0:
                spectral_variable = True
        elif variable_name not in list(product.getMaskGroup().getNodeNames()):
            tiepointgrid = True
        else:
            mask = True

        if time_stamp:
            info_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'info',
                                  'units': "UTC",
                                  'ndims': 1,
                                  'shape': (int(product.getSceneRasterHeight()))}
            info_variable = Variable(info_variable_dict)
        elif spectral_variable:
            info_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'info',
                                  'units': product.getBand(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                            int(product.getBand(variable_name).getRasterHeight())),
                                  'wavelength': product.getBand(variable_name).getSpectralWavelength(),
                                  'bandwidth': product.getBand(variable_name).getSpectralBandwidth(),
                                  'srf': None}
            info_variable = SpectralVariable(info_variable_dict)
        elif not tiepointgrid:
            info_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'info',
                                  'units': product.getBand(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getBand(variable_name).getRasterWidth()),
                                            int(product.getBand(variable_name).getRasterHeight()))}
            info_variable = Variable(info_variable_dict)
        else:
            info_variable_dict = {'name': variable_name,
                                  'dtype': 'float',
                                  'vtype': 'info',
                                  'units': product.getTiePointGrid(variable_name).getUnit(),
                                  'ndims': 2,
                                  'shape': (int(product.getSceneRasterWidth()),
                                            int(product.getSceneRasterHeight()))}
            info_variable = Variable(info_variable_dict)

        return info_variable

    def getInfoVariableNames(self, product):
        """
        Returns list of product "info" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :info_variable_names: *list*

            List of product "info" type variable names
        """

        all_variables_names = list(product.getBandNames()) + list(product.getTiePointGridNames())

        info_variable_names = []
        if "longitude" in all_variables_names:
            info_variable_names.append("longitude")

        elif "lon" in all_variables_names:
            info_variable_names.append("lon")

        if "latitude" in all_variables_names:
            info_variable_names.append("latitude")

        elif "lat" in all_variables_names:
            info_variable_names.append("lat")

        info_variable_names.append("time_stamp")

        return info_variable_names

    def return_available_variables(self, product, expected_variables):
        """
        Return variables available in data product from expected list

        :type product: snappy.Product
        :param product: data product

        :param expected_variables: list
        :param expected_variables: required variables expected to be contained in data product

        :return:
            :available_expected_variables: *list*

            variables from expected_variables list contained in the data product
        """

        available_variables = list(product.getBandNames()) + list(product.getTiePointGridNames()) + \
                              list(product.getMaskGroup().getNodeNames())

        return [v for v in expected_variables if v in available_variables]

    def determine_getData_product(self, products, selected_variables):
        """
        Return `snappy.Product` object to get data from for given variables

        :type products: list
        :param products: List of dictionaries of in-memory representations of opened data products

        :type selected_variables: list
        :param selected_variables: List of selected variables to open

        :return:
            :product: *snappy.Product*

            In-memory representation data product to get data from
        """

        product = None
        for i, product_dict in enumerate(products):
            product_variables = product_dict['variables']
            if all(s in product_variables for s in selected_variables):
                product = product_dict['product']

        if product is None:
            raise NameError("Cannot open combination of variables")

        return product

    def determine_getData_mask(self, products, selected_variables):
        """
        Return mask to apply to data when opened

        :type products: list
        :param products: List of dictionaries of in-memory representations of opened data products

        :type selected: list
        :param selected_variables: List of selected variables to open

        :return:
            :mask: *numpy.ndarray*

            Mask to apply to data when opened
        """

        mask = None

        if type(self.data_mask) == ndarray:
            return self.data_mask

        for i, product_dict in enumerate(products):
            product_variables = product_dict['variables']
            if all(s in product_variables for s in selected_variables):
                mask = self.data_mask[i] if self.data_mask is not None else None

        return mask

    def getData(self, products, variables, attributes, variable, *args):
        """
        Returns variable[s] of in-memory product[s] as an xarray data structure.

        :type products: dict
        :param products: Dictionary of in-memory representation of *snappy.Product* data product

        :type variables: list
        :param variables: List of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type attributes: dict
        :param attributes: Dictionary of product[s] metadata

        :type variable: str
        :param variable: Name of variable to return data for

        :type args: str
        :param args: Name of additional variables to to return data for

        :return:
            :data: *xarray.DataArray [xarray.Dataset]*

            Specified variable[s] in memory in xarray data structure
        """

        # Full list of variables to open
        selected_variables = [variable] + list(args)

        product = self.determine_getData_product(products, selected_variables)
        mask = self.determine_getData_mask(products, selected_variables)

        # Case A: Only one variable required so form an xarray.DataArray
        if len(selected_variables) == 1:

            # i. Read variable pixel values
            pixel_values = self.getPixelValues(product, variables, attributes, variable, mask=mask)

            # ii. convert variables attributes to netcdf friendly format
            variable_info = self.simplify_attr(self.getVariableInfo(variables, variable))

            # ii. Form xarray.DataArray
            data = xr.DataArray(pixel_values, name=variable, attrs=variable_info)

        # Case B: Multiple variables required so form an xarray.Dataset
        else:
            # i. Set coords
            coords, remaining_variables = self.define_coords(product, variables, attributes, selected_variables)

            # ii. Build variable data dictionary
            data_vars = {}
            for v in remaining_variables:
                data_vars[v] = (['x', 'y'], self.getPixelValues(product, variables, attributes, v, mask=mask),
                                self.simplify_attr(self.getVariableInfo(variables, v)))

            # iii. Form xarray.Dataset
            data = xr.Dataset(data_vars=data_vars, coords=coords, attrs=self.simplify_attr(attributes))

        return data

    def define_coords(self, product, variables, attributes, selected_variables):
        """
        Build `xarray.Dataset` coord dictionary from based on list of selected variables

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variables: list
        :param variables: list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type attributes: dict
        :param attributes: Dictionary of product attributes

        :type selected_variables: list
        :param selected_variables: List of requested variables

        :return:
            :coords: *dict*

            xarray.Dataset` coord dictionary

            :remaining_variables: *list*

            variables remaining from selected variables list not included in coords
        """

        coords = {}
        remaining_variables = deepcopy(selected_variables)

        # check required varis against dictionary of possible coordinate variables to see if any coords needed
        var_coords = {"lon": {"shape": ["x", "y"], "poss_names": ["longitude", "long", "lon"]},
                      "lat": {"shape": ["x", "y"], "poss_names": ["latitude", "lat"]},
                      "alt": {"shape": ["x", "y"], "poss_names": ["altitude", "alt", "elevation"]},
                      "time_stamp": {"shape": ["x"], "poss_names": ["time_stamp"]}}

        for common_name in var_coords.keys():
            for poss_name in var_coords[common_name]["poss_names"]:
                if poss_name in selected_variables:
                    coords[common_name] = (var_coords[common_name]["shape"],
                                           self.getPixelValues(product, variables, attributes, poss_name),
                                           self.simplify_attr(self.getVariableInfo(variables, poss_name)))
                    remaining_variables.remove(poss_name)

        # If no coordinate variables required set coords to None
        if coords == {}:
            return None, remaining_variables
        return coords, remaining_variables

    def getPixelValues(self, product, variables, attributes, variable, mask=None):
        """
        Returns pixel values of variable of in-memory products

        :type product: *snappy.Product*
        :param product: In memory representation of data product.

        :type variables: list
        :param variables: list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type attributes: dict
        :param attributes: Dictionary of product attributes

        :type variable: str
        :param variable: Name of variable to return data for.

        :return:
            :pixel_values: *numpy.ndarray*

            specified variable pixels values
        """

        # 1. Pre-processing

        # Check requested variable in variables dictionary
        # if variable not in [v.name for v in variables]:
        #     raise RuntimeError("%s variable not available in opened %s product" % (variable, attributes['product_string']))

        # * special case for time_stamp as values in metadata
        if variable == "time_stamp":
            return self.getTimeStampValues(product, variables, attributes, variable)

        # 2. Open data

        # a. Initialise data array
        w = product.getSceneRasterWidth()
        h = product.getSceneRasterHeight()
        pixel_values = zeros(w * h, float32)

        # b. Get data object, depending on variable type
        band_names = product.getBandNames()
        tie_point_grid_names = product.getTiePointGridNames()
        mask_names = product.getMaskGroup().getNodeNames()
        if variable in band_names:
            obj = product.getBand(variable)
            valid_mask = zeros(h * w, bool_)
            product.getBand(variable).readValidMask(0, 0, w, h, valid_mask)
            valid_mask.shape = h, w

        elif variable in tie_point_grid_names:
            obj = product.getTiePointGrid(variable)
        elif variable in mask_names:
            mask = product.getMaskGroup().get(variable)
            obj = jpy.cast(mask, snappy.Mask)
            pixel_values = zeros(w * h, uint32)

        # c. Populate pixel data array with data from data object
        obj.readPixels(0, 0, w, h, pixel_values)
        pixel_values.shape = h, w

        # d. apply valid data mask to band data
        if variable in band_names:
            if mask is not None:
                pixel_values = ma.masked_array(pixel_values, mask=mask-valid_mask)
            else:
                pixel_values = ma.masked_array(pixel_values, mask=-valid_mask)
            return pixel_values

        if mask is not None:
            pixel_values = ma.masked_array(pixel_values, mask=mask)

        return pixel_values

    def getTimeStampValues(self, product, variables, attributes, variable):
        """
        Return values for per pixel time per row

        :type product: *snappy.Product*
        :param product: In memory representation of data product.

        :type variables: list
        :param variables: list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type attributes: dict
        :param attributes: Dictionary of product attributes

        :type variable: str
        :param variable: Name of variable to return data for.

        :return:
            :time_stamp_values: *numpy.ndarray*

            time stamp per row
        """

        start_time = attributes["start_time"]
        end_time = attributes["end_time"]
        product_rows = product.getSceneRasterHeight()

        row_time = (end_time - start_time) / (product_rows-1)
        increments = range(0, product_rows) * array([row_time] * product_rows)

        return asarray(start_time + increments, dtype=datetime)

    def simplify_attr(self, attr):
        """
        Return a simplified form of input attributes dictionary suitable for netcdf file attributes

        :type attr: dict
        :param attr: attributes dictionary

        :return:
            :new_attr: *dict*

            Simplified attributes dictionary
        """

        # Start with copy of original attributes
        new_attr = deepcopy(attr)

        for attribute in new_attr.keys():

            # Change bools to "True", "False" strings
            if str(type(new_attr[attribute])) == "<type 'bool'>":
                if new_attr[attribute] == True:
                    new_attr[attribute] = "True"
                elif new_attr[attribute] == False:
                    new_attr[attribute] = "False"

            # Change datetime.datetime objects to strings
            elif str(type(new_attr[attribute])) == "<type 'datetime.datetime'>":
                new_attr[attribute] = new_attr[attribute].strftime("%Y-%m-%dT%H:%M:%S")

            # Change None type to "None" string
            elif str(type(new_attr[attribute])) == "<type 'NoneType'>":
                new_attr[attribute] = "None"

            # Remove coordinates attribute
            elif attribute == "coordinates":
                del new_attr[attribute]

        return new_attr

if __name__ == "__main__":
    pass