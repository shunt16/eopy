"""
Main wrapper of NPL Data Reading and Writer packages
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from ProductDataReader import ProductDataReader

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Product:
    """
    Product instances are an in-memory representation of a data product.

    Sample Code:

    .. code-block:: python

        # Initialise and read data

        dataProd = Product('path/to/data.file')

        # Call data values

        values = dataProd.getData('some_attribute')

    :Attributes:
        .. py:attribute:: product

            *-*

            In-memory representation of data product

        .. py:attribute:: variables:

            *list*

            List with elements ``Variable`` objects per variable for which data can be returned by
            *self.getData(variable)* method.

        .. py:attribute:: attributes:

            *dict*

            Dictionary of product attributes

        .. py:attribute:: dataReader

            *eopy.dataIO.AbstractDataReader.AbstractDataReader*

            Data reader for data specified by product_path, instantiated in *self.readProduct*

    :Methods:
        .. py:method:: openProduct(...):

            Reads the data product specified by the given file path.

            Functionality from *self.dataReader*

        .. py:method:: getData(...):

            Returns variable[s] of in-memory product as an xarray data structure.

            Functionality from *self.dataReader*

        .. py:method:: getVariableNames(...):

            Returns all variable names

        .. py:method:: getDataVariableNames(...):

            Returns variable names for data variables

        .. py:method:: getMaskVariableNames(...):

            Returns variable names for mask variables

        .. py:method:: getMeteorologicalVariableNames(...):

            Returns variable names for meteorological variables

        .. py:method:: getSensorVariableNames(...):

            Returns variable names for sensor variables

        .. py:method:: getInfoVariableNames(...):

            Returns variable names for info variables

        .. py:method:: getVariableInfo(...):

            Returns variable information dictionary for specified variable

        .. py:method:: save_to_netcdf(...):

            Writes entire data product to netcdf file at specified path
    """

    def __init__(self, product_path=None):
        """
        Initialise data Product object

        :type product_path: str
        :param product_path: The data product file path
        """

        # Initialise class attributes
        self.dataReader = None     # Data reader for data specified by product_path, instantiated in self.readProduct
        self.product = None        # In memory product instantiation
        self.attributes = None     # Product attributes dictionary
        self.variables = None      # Product variables dictionary

        # If path to product provided try to open data
        if product_path is not None:
            self.product, self.variables, self.attributes = self.openProduct(product_path)
            # try:
            #     self.product, self.variables, self.attributes = self.openProduct(product_path)
            # except:
            #     raise RuntimeError("Product Error: Unable to read data product")

    def openProduct(self, product_path):
        """
        Reads the data product specified by the given file path.

        Functionality from *self.dataReader*

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :product: *-*

            In-memory representation of a data product (type product dependant)

            :variables: *list*

            Dictionary with entry per variable for which data can be returned by *self.getData(variable)* method.

            :attributes: *dict*

            Dictionary of product metadata
        """

        # Get appropriate the data reader for  the data product at specified file path
        productDataReader = ProductDataReader()
        dataReader = productDataReader.setDataReader(product_path)

        # Read data
        self.dataReader = dataReader(product_path)
        product, variables, attributes = self.dataReader.openProduct(product_path)

        return product, variables, attributes

    def getData(self, variable, *args):
        """
        Returns variable[s] of in-memory product as an xarray data structure.

        Functionality from *self.dataReader*

        :type variable: str
        :param variable: Name of product variable to get data for

        :param args: Name of additional product variables to get data for

        :return:
            :data: *xarray.DataArray [xarray.Dataset]*

            Specified variable[s] in memory in xarray data structure
        """

        return self.dataReader.getData(self.product, self.variables, self.attributes, variable, *args)

    def _check_variables_compatible(self, variables):
        """
        Check if variables are compatible to be return on the same grid

        :type variables: list
        :param variables: list of variable names

        :return:
            :compatible: *bool*

            True if variables compatible to be return on same grid
        """

        variable_x_shapes = [self.getVariableInfo(v)["shape"][0] for v in variables]
        variable_y_shapes = [self.getVariableInfo(v)["shape"][0] for v in variables]

        if (variable_x_shapes.count(variable_x_shapes[0]) == len(variable_x_shapes)) and \
                (variable_y_shapes.count(variable_y_shapes[0]) == len(variable_y_shapes)):
            return True
        return False

    def getVariableNames(self):
        """
        Returns all variable names

        :return:
            :variable_names: *lst*

            List of all variable names
        """

        return [var.name for var in self.variables]

    def getDataVariableNames(self):
        """
        Returns variable names for data variables

        :return:
            :data_variable_names: *lst*

            List of all data variable names
        """

        return [var.name for var in self.variables if var.vtype == "data"]

    def getMaskVariableNames(self):
        """
        Returns variable names for mask variables

        :return:
            :mask_variable_names: *lst*

            List of all mask variable names
        """

        return [var.name for var in self.variables if var.vtype == "mask"]

    def getMeteorologicalVariableNames(self):
        """
        Returns variable names for meteorological variables

        :return:
            :meteorological_variable_names: *lst*

            List of all meteorological variable names
        """

        return [var.name for var in self.variables if var.vtype == "meteorological"]

    def getSensorVariableNames(self):
        """
        Returns variable names for sensor variables

        :return:
            :sensor_variable_names: *lst*

            List of all sensor variable names
        """

        return [var.name for var in self.variables if var.vtype == "sensor"]

    def getInfoVariableNames(self):
        """
        Returns variable names for info variables

        :return:
            :info_variable_names: *lst*

            List of all info variable names
        """

        return [var.name for var in self.variables if var.vtype == "info"]

    def getVariableInfo(self, name):
        """
        Returns variable information dictionary for specified variable

        :type name: str
        :param name: variable name to return information for

        :return:
            :variable_dict: *dict*

            Dictionary of variable metadata
        """

        return [var.return_variable_dict() for var in self.variables if var.name == name][0]

    def save_to_netcdf(self, path):
        """
        Writes entire data product to netcdf file at specified path

        :type path: str
        :param path: file path of output
        """

        data = self.getData(*self.getVariableNames())
        data.to_netcdf(path)

        return 0


if __name__ == "__main__":
    import os
    cwd = os.getcwd()
    slstr_prod = Product(r"D:\Sentinel-3\SLSTR\S3A_SL_1_RBT____20180614T192802_20180614T193102_20180614T215609_0180_032_199_0900_SVL_O_NR_003.SEN3\xfdumanifest.xml")
    slstr_prod.getData("S4_radiance_cn")
    pass