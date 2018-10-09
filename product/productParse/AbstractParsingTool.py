"""
Contains class to be used as a parent class for data parsing tool implementations
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class AbstractParsingTool:
    """
    AbstractParsingTool is an inheritable class of which specific parsing tool implementations should be a sub-class of

    :Attributes:
        .. py:attribute:: processingFactory

        *obj*

        Contains functionality to process *eopy.dataIO.Product.Product* objects as required.

    :Methods:
        .. py:method:: setParsingFactory(...):

            Returns parsingFactory for data product with given ``product_path``.

            *If no suitable factory in parsing tool implementation available returns None*

        .. py:method:: parseProduct(...):

            Returns dictionary of parsed product metadata.
    """

    def __init__(self, product_path=None):
        """
        Initialise ParsingTool object

        :type product_path: str
        :param product_path: Data product path
        """

        # Initialise attributes
        self.parsingFactory = None   # Parsing Factory for input data path

        if product_path is not None:
            # See if parsingFactory available for product with a specified product_path
            parsingFactory = self.setParsingFactory(product_path)

            # If parsingFactory found create a parsingFactory object
            if parsingFactory is not None:
                self.parsingFactory = parsingFactory()

    def setParsingFactory(self, product_path=None):
        """
        Returns parsingFactory for data product with given ``product_path``.

        *If no suitable factory in parsing tool implementation available returns None*

        :type product_path: str
        :param product_path: Data product path

        :return:
            :ParsingFactory: *eopy.dataParse.AbstractParsingFactory.AbstractParsingFactory*

            Parsing factory suitable for input ``product_path``

            *If no suitable parsing factory implementations available returns None*
        """

        return None

    def parseProduct(self, product_path, detail="min", **kwargs):
        """
        Returns dictionary of parsed product metadata.

        Uses functionality from *self.parsingFactory*.

        :type product_path: str
        :param product_path: Data product path

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

        # Use parsingFactory method parseProduct() to process data product
        attributes = self.parsingFactory.parseProduct(product_path, detail="min", **kwargs)

        return attributes


if __name__ == "__main__":
    pass
 

