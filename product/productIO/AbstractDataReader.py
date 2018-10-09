"""
Contains class to be used as parent class for data reader implementations
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class AbstractDataReader:
    """
    AbstractDataReader is an inheritable class of which specific data readers implementations should be a sub-class of

    :Attributes:
        .. py:attribute:: dataFactory

        *eopy.dataIO.AbstractDataFactory.AbstractDataFactory*

        Instance of sub-class of product factory for reading product data

    :Methods:
        .. py:method:: setDataFactory(...):

            Return product factory suitable for data product at product_path

            *If no suitable factory in reader implementation available returns None*

        .. py:method:: openProduct(...):

            Opens an in-memory representation of data product specified by product_path.

            Inherits this functionality from *self.dataFactory*.

        .. py:method:: getData(...):

            Returns variable[s] of in-memory product as an xarray data structure.

            Inherits this functionality from *self.dataFactory*.
    """

    def __init__(self, product_path=None):
        """
        Initialise DataReader object

        :type product_path: str
        :param product_path: The data product file path
        """

        # Initialise attributes
        self.dataFactory = None   # Data Factory for input data path

        if product_path is not None:
            # See if dataFactory available in reader implementation suitable data product at specified product_path
            dataFactory = self.setDataFactory(product_path)

            # If dataFactory found create a dataFactory object
            if dataFactory is not None:
                self.dataFactory = dataFactory()

    def setDataFactory(self, product_path=None):
        """
        Return product factory suitable for data product at product_path

        *If no suitable factory available returns None*

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :DataFactory: *eopy.dataIO.AbstractDataFactory.AbstractDataFactory*

            Product Data Factory
        """
        return None

    def openProduct(self, product_path):
        """
        Opens an in-memory represenation of data product at specified path

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :product: *-*

            In memory representation of data product

            :variables: *dict*

            Dictionary of variables for which data can be returned by self.getData(variable) method.

            :attributes: *dict*

            Dictionary of product metadata
        """

        # Use dataFactory method openProduct() to initialise in-memory representation of data product
        product, variables, attributes = self.dataFactory.openProduct(product_path)

        return product, variables, attributes

    def getData(self, product, variables, attributes, variable, *args):
        """
        Returns variable[s] of in-memory product as an xarray data structure.

        :type product: -
        :param product: In memory representation of data product

        :type variables: dict
        :param variables: Dictionary of variables for which data can be returned by self.getData(variable) method.

        :type attributes: dict
        :param attributes: Dictionary of product metadata (contents described more fully in class doc string)

        :type varaible: str
        :param variable: Name of variable to return data for

        :type args: str
        :param args: Name of additional variables to to return data for

        :return:
            :data: *xarray.DataArray [xarray.Dataset]*

            Specified variable[s] in memory in xarray data structure
        """

        # Use dataFactory method getData() to get variable as an xarray
        data = self.dataFactory.getData(product, variables, attributes, variable, *args)

        return data


if __name__ == "__main__":
    pass
