"""
Main wrapper of NPL data parsing packages
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from ProductParsingTool import ProductParsingTool

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Parse:
    """
    Parse class provides functionality for parsing information about a data product without opening it from, for
    example, the product filename.

    Sample Code:

    .. code-block:: python

        # Initialise and parse data

        dataParse = Parse("path/to/data.file')

        # Get data from attributes dictionary attribute of Parse object

        my_attribute = dataParse.attributes('my_attribute')

    :Attributes:

        .. py:attribute:: attributes:

            *dict*

            Dictionary of product attributes

        .. py:attribute:: parsingTool

            *eopy.dataParse.AbstractParsingTool.AbstractParsingTool*

            Data reader for data specified by product_path, instantiated in *self.readProduct*

    :Methods:
        .. py:method:: parseProduct(...):

            Parses metadata from the data product specified by the given file path.

    """

    def __init__(self, product_path=None, detail="min", **kwargs):
        """
        Initialise data Parse object

        :type product_path: str
        :param product_path: The data product file path.

        :type detail: str
        :param detail: Can take values:

        * "min" (default) - only information available with filename parsed.
        * "max" - information available in metadata files also parsed, but with opening the product.

        :type kwargs: -
        :param kwargs: Parsing parameters
        """

        # Initialise class attributes
        self.parsingTool = None  # Data reader for data specified by product_path, instantiated in self.parseProduct
        self.attributes = None  # Parse attributes dictionary

        # If path to product provided try to open data
        if product_path is not None:
            # try:
            self.attributes = self.parseProduct(product_path, detail=detail, **kwargs)
            # except:
            #    raise RuntimeError("Product Error: Unable to parse information from data product")

    def parseProduct(self, product_path, detail="min", **kwargs):
        """
        Parses metadata from the data product specified by the given file path.

        Functionality from *self.parsingTool*

        :type product_path: str
        :param product_path: The data product file path.

        :type detail: str
        :param detail: Can take values:

        * "min" (default) - only information available with filename parsed.
        * "max" - information available in metadata files also parsed, but with opening the product.

        :type kwargs: -
        :param kwargs: Parsing parameters

        :return:
            :attributes: *dict*

            Dictionary of parsed product metadata.
        """

        # Get appropriate the data parsing tool for  the data product at specified file path
        productParsingTool = ProductParsingTool()
        parsingTool = productParsingTool.setParsingTool(product_path)

        # Read data
        attributes = None
        if parsingTool is not None:
            self.parsingTool = parsingTool(product_path)
            attributes = self.parsingTool.parseProduct(product_path, detail=detail, **kwargs)

        return attributes


if __name__ == "__main__":
    pass
