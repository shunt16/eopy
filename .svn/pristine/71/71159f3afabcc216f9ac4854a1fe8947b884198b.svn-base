"""
Contains class to be used as parent class for data factory implementations
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from Variable import Variable
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "08/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class AbstractDataFactory:
    """
    AbstractDataFactory is an inheritable class of which specific data factory implementations should be a sub-class of

    :Methods:
        .. py:method:: openProduct(...):

            Opens an in-memory representation of data product specified by product_path.

        .. py:method:: readVariables(...):

            Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        .. py:method:: getDataVariables(...):

            Returns list of product "data" type variables as ``Variable`` or `SpectralVariable` class objects.

        .. py:method:: createDataVariable(...):

            Returns "data" type `SpectralVariable` class objects, for given product variable

        .. py:method:: getDataVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: editDataVariable(...):

            Returns 'data' variable objects with attributes edited compared to default values obtained from product

        .. py:method:: getMaskVariables(...):

            Returns list of product "mask" type variables as ``Variable`` class objects.

        .. py:method:: createMaskVariable(...):

            Returns "mask" type `Variable` class objects, for given product variable

        .. py:method:: getMaskVariableNames(...):

            Returns list of product "mask" type variable names

        .. py:method:: editMaskVariable(...):

            Returns 'mask' variable objects with attributes edited compared to default values obtained from product

        .. py:method:: getMeteorologicalVariables(...):

            Returns list of product "meteorological" type variables as ``Variable`` class objects.

        .. py:method:: createMeteorologicalVariable(...):

            Returns "meteorological" type `Variable` class objects, for given product variable

        .. py:method:: getMeteorologicalVariableNames(...):

            Returns list of product "meteorological" type variable names

        .. py:method:: editMeteorologicalVariable(...):

            Returns 'meteorological' variable objects with attributes edited compared to default values obtained from product

        .. py:method:: getSensorVariables(...):

            Returns list of product "sensor" type variables as ``Variable`` class objects.

        .. py:method:: createSensorVariable(...):

            Returns "sensor" type `Variable` class objects, for given product variable

        .. py:method:: getSensorVariableNames(...):

            Returns list of product "sensor" type variable names

        .. py:method:: editSensorVariable(...):

            Returns 'sensor' variable objects with attributes edited compared to default values obtained from product

        .. py:method:: getInfoVariables(...):

            Returns list of product "info" type variables as ``Variable`` class objects.

        .. py:method:: createInforVariable(...):

            Returns "info" type `Variable` class objects, for given product variable

        .. py:method:: getInfoVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: editInfoVariable(...):

            Returns 'info' variable objects with attributes edited compared to default values obtained from product

        . py:method:: readAttributes(...):

            Returns dictionary of product attributes

        .. py:method:: getData(...):

            Returns variable[s] of in-memory product as an xarray data structure.
    """

    def __init__(self):
        """
        Initialise class
        """

        pass

    def openProduct(self, product_path):
        """
        Opens an in-memory representation of data product at specified product_path

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :product: *-*

            In memory representation of data product

            :variables: *dict*

            List of product variables as ``Variable`` or ``SpectralVariable`` class objects.

            :attributes: *dict*

            Dictionary of product metadata
        """

        product = None
        variables = self.readVariables(product)
        attributes = self.readAttributes(product)
        return product, variables, attributes

    def readVariables(self, product):
        """
        Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :variables: *list*

            List with elements ``Variable`` objects per variable for which data can be returned by
            *self.getData(variable)* method.
        """
        data_variables = self.getDataVariables(product)
        mask_variables = self.getMaskVariables(product)
        meteorological_variables = self.getMeteorologicalVariables(product)
        sensor_variables = self.getSensorVariables(product)
        info_variables = self.getInfoVariables(product)

        return data_variables + mask_variables + meteorological_variables + sensor_variables + info_variables

    def getVariableNames(self, product):
        """
        Returns list of all product variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :variable_names: *list*

            List of all product variable names
        """

        variable_names = self.getDataVariableNames(product) + \
                         self.getMaskVariableNames(product) + \
                         self.getMeteorologicalVariableNames(product) + \
                         self.getSensorVariableNames(product) + \
                         self.getInfoVariableNames(product)

        return variable_names

    def getVariableInfo(self, variables, name):
        """
        Returns variable information dictionary for specified variable

        :type variables: list
        :param variables: list of variable objects

        :type name: str
        :param name: variable name to return information for

        :return:
            :variable_dict: *dict*

            Dictionary of variable metadata
        """

        return [var.return_variable_dict() for var in variables if var.name == name][0]

    def getDataVariables(self, product):
        """
        Returns list of product "data" type variables as ``Variable`` or `SpectralVariable` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :data_variables: *list*

            List with elements ``Variable`` objects per "data" type variable for which data can be returned by
            *self.getData(variable)* method.
        """

        data_variable_names = self.getDataVariableNames(product)
        data_variables = [self.createDataVariable(product, n) for n in data_variable_names]
        data_variables = [self.editDataVariable(product, v) for v in data_variables]

        return data_variables

    def createDataVariable(self, product, variable_name):
        """
        Returns "data" type `SpectralVariable` class objects, for given product variable

        :type product: *-*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :data_variable: *eopy.product.productIO.SpectralVariable.SpectraVariable*

            ``SpectralVariable`` object for given product 'data' variable
        """

        data_variable_dict = {'name': variable_name,
                              'dtype': None,
                              'vtype': 'data',
                              'units': None,
                              'ndims': None,
                              'shape': None,
                              'wavelength': None,
                              'bandwidth': None,
                              'srf': None}

        data_variable = SpectralVariable(data_variable_dict)

        return data_variable

    def getDataVariableNames(self, product):
        """
        Returns list of product "data" type variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :data_variable_names: *list*

            List of product "data" type variable names
        """
        return []

    def editDataVariable(self, product, data_variable):
        """
        Returns 'data' variable objects with attributes edited compared to default values obtained from product

        :type product: *-*
        :param product: In memory representation of data product

        :type data_variable: *eopy.product.productIO.SpectralVariable.SpectraVariable*
        :type data_variable: product variable object of "data" type

        :return:
            :data_variable_edited: *list*

            product 'data' variable object with attributes edited compared to default values obtained from product
        """
        return data_variable

    def getMaskVariables(self, product):
        """
        Returns list of product "mask" type variables as ``Variable`` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :mask_variables: *list*

            List with elements ``Variable`` objects per "mask" type variable for which data can be returned by
            *self.getData(variable)* method.
        """
        mask_variable_names = self.getMaskVariableNames(product)
        mask_variables = [self.createMaskVariable(product, n) for n in mask_variable_names]
        mask_variables = [self.editMaskVariable(product, v) for v in mask_variables]

        return mask_variables

    def createMaskVariable(self, product, variable_name):
        """
        Returns "mask" type `Variable` class objects, for given product variable

        :type product: *-*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :mask_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'mask' variable
        """

        mask_variable_dict = {'name': variable_name,
                              'dtype': None,
                              'vtype': 'mask',
                              'units': None,
                              'ndims': None,
                              'shape': None}

        mask_variable = Variable(mask_variable_dict)

        return mask_variable

    def getMaskVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :mask_variable_names: *list*

            List of product "mask" type variable names
        """
        return []

    def editMaskVariable(self, product, mask_variable):
        """
        Returns 'mask' variable objects with attributes edited compared to default values obtained from product

        :type product: *-*
        :param product: In memory representation of data product

        :type mask_variable: *eopy.product.productIO.Variable.Variable*
        :type mask_variable: product variable object of "mask" type

        :return:
            :mask_variable_edited: *list*

            product 'mask' variable object with attributes edited compared to default values obtained from product
        """
        return mask_variable

    def getMeteorologicalVariables(self, product):
        """
        Returns list of product "meteorological" type variables as ``Variable`` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :meteorological_variables: *list*

            List with elements ``Variable`` objects per "meteorological" type variable for which data can be returned by
            *self.getData(variable)* method.
        """
        meteorological_variable_names = self.getMeteorologicalVariableNames(product)
        meteorological_variables = [self.createMeteorologicalVariable(product, n) for n in meteorological_variable_names]
        meteorological_variables = [self.editMeteorologicalVariable(product, v) for v in meteorological_variables]

        return meteorological_variables

    def createMeteorologicalVariable(self, product, variable_name):
        """
        Returns "meteorological" type `Variable` class objects, for given product variable

        :type product: *-*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :meteorological_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'meteorological' variable
        """

        meteorological_variable_dict = {'name': variable_name,
                                        'dtype': None,
                                        'vtype': 'meteorological',
                                        'units': None,
                                        'ndims': None,
                                        'shape': None}

        meteorological_variable = Variable(meteorological_variable_dict)

        return meteorological_variable

    def getMeteorologicalVariableNames(self, product):
        """
        Returns list of product "meteorological" type variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :meteorological_variable_names: *list*

            List of product "mask" type variable names
        """
        return []

    def editMeteorologicalVariable(self, product, meteorological_variable):
        """
        Returns 'meteorological' variable objects with attributes edited compared to default values obtained from
        product

        :type product: *-*
        :param product: In memory representation of data product

        :type meteorological_variable: *eopy.product.productIO.Variable.Variable*
        :type meteorological_variable: product variable object of "meteorological" type

        :return:
            :meteorological_variable_edited: *list*

            product 'meteorological' variable object with attributes edited compared to default values obtained from
            product
        """
        return meteorological_variable

    def getSensorVariables(self, product):
        """
        Returns list of product "sensor" type variables as ``Variable`` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :sensor_variables: *list*

            List with elements ``Variable`` objects per "sensor" type variable for which data can be returned by
            *self.getData(variable)* method.
        """
        sensor_variable_names = self.getSensorVariableNames(product)
        sensor_variables = [self.createSensorVariable(product, n) for n in sensor_variable_names]
        sensor_variables = [self.editSensorVariable(product, v) for v in sensor_variables]

        return sensor_variables

    def createSensorVariable(self, product, variable_name):
        """
        Returns "sensor" type `Variable` class objects, for given product variable

        :type product: *-*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :sensor_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'sensor' variable
        """

        sensor_variable_dict = {'name': variable_name,
                                'dtype': None,
                                'vtype': 'sensor',
                                'units': None,
                                'ndims': None,
                                'shape': None}

        sensor_variable = Variable(sensor_variable_dict)

        return sensor_variable

    def getSensorVariableNames(self, product):
        """
        Returns list of product "sensor" type variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :sensor_variable_names: *list*

            List of product "sensor" type variable names
        """
        return []

    def editSensorVariable(self, product, sensor_variable):
        """
        Returns 'sensor' variable objects with attributes edited compared to default values obtained from product

        :type product: *-*
        :param product: In memory representation of data product

        :type sensor_variable: *eopy.product.productIO.Variable.Variable*
        :type sensor_variable: product variable object of "sensor" type

        :return:
            :sensor_variable_edited: *list*

            product 'sensor' variable object with attributes edited compared to default values obtained from product
        """

        return sensor_variable

    def getInfoVariables(self, product):
        """
        Returns list of product "info" type variables as ``Variable`` class objects.

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :info_variables: *list*

            List with elements ``Variable`` objects per "info" type variable for which data can be returned by
            *self.getData(variable)* method.
        """
        info_variable_names = self.getInfoVariableNames(product)
        info_variables = [self.createInfoVariable(product, n) for n in info_variable_names]
        info_variables = [self.editInfoVariable(product, v) for v in info_variables]

        return info_variables

    def createInfoVariable(self, product, variable_name):
        """
        Returns "info" type `Variable` class objects, for given product variable

        :type product: *-*
        :param product: In memory representation of data product

        :type variable_name: str
        :param product: Specified product variable name

        :return:
            :info_variable: *eopy.product.productIO.Variable.Variable*

            ``Variable`` object for given product 'info' variable
        """

        info_variable_dict = {'name': variable_name,
                              'dtype': None,
                              'vtype': 'info',
                              'units': None,
                              'ndims': None,
                              'shape': None}

        info_variable = Variable(info_variable_dict)

        return info_variable

    def getInfoVariableNames(self, product):
        """
        Returns list of product "info" type variable names

        :type product: *-*
        :param product: In memory representation of data product


        :return:
            :info_variable_names: *list*

            List of product "info" type variable names
        """
        return []

    def editInfoVariable(self, product, info_variable):
        """
        Returns 'info' variable objects with attributes edited compared to default values obtained from product

        :type product: *-*
        :param product: In memory representation of data product

        :type info_variable: *eopy.product.productIO.SpectralVariable.SpectraVariable*
        :type info_variable: product variable object of "info" type

        :return:
            :info_variable_edited: *list*

            product 'data' variable object with attributes edited compared to default values obtained from product
        """

        return info_variable

    def readAttributes(self, product):
        """
        Return dictionary of product attributes

        :type product: *-*
        :param product: In memory representation of data product

        :return:
            :attributes: *dict*

            dictionary of product attributes
        """
        return {"product_string": None}

    def getData(self, product, variables, attributes, variable, *args):
        """
        Returns variable[s] of in-memory product as an xarray data structure.

        :type product: -
        :param product: In memory representation of data product

        :type variables: dict
        :param variables: Dictionary with entry per variable for which data can be returned by self.getData(variable)
                          method.

        :type attributes: dict
        :param attributes: Dictionary of product metadata

        :type variable: str
        :param variable: Name of variable to return data for

        :param args: str
        :param args: Name of additional variables to return data for

        :return:
            :data: *xarray.DataArray [xarray.Dataset]*
            Specified variable[s] in memory in xarray data structure
        """

        data = None
        return data


if __name__ == "__main__":
    pass
 

