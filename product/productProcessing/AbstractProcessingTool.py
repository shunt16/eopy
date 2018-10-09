"""
Contains class to be used as a parent class for data processing tool implementations
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


class AbstractProcessingTool:
    """
    AbstractProcessingTool is an inheritable class of which specific processing tool implementations for
    *eopy.dataProcessing* processor packages should be a sub-class of

    :Attributes:

        .. py:attribute:: processingFactory

        *obj*

        Contains functionality to process *eopy.dataIO.Product.Product* objects as required.

    :Methods:
        .. py:method:: setProcessingFactory(...):

            Returns processingFactory from given processor package suitable for *eopy.dataIO.Product.Product* object
            with a specified product_string entry in it's attributes dictionary.

            *If no suitable factory in processing tool implementation available returns None*

        .. py:method:: processProduct(...):

            Returns processed version of input *eopy.dataIO.Product.Product* object, using functionality from
            processingFactory
    """

    def __init__(self, product_string=None):
        """
        Initialise ProcessingTool object

        :type product_string: str
        :param product_string: *eopy.dataIO.Product.Product* object "product_string" entry of its attributes dictionary
        """

        # Initialise attributes
        self.processingFactory = None   # Subset Factory for input data path

        if product_string is not None:
            # See if processingFactory available in eopy.dataProcessing.* processor package suitable for
            # eopy.dataIO.Product.Product object with a specified product_string entry in it's attributes dictionary
            # attribute
            processingFactory = self.setProcessingFactory(product_string)

            # If processingFactory found create a processingFactory object
            if processingFactory is not None:
                self.processingFactory = processingFactory()

    def setProcessingFactory(self, product_string=None):
        """
        Returns processingFactory in *eopy.dataProcessing* processor package suitable for *eopy.dataIO.Product.Product*
        object with a specified product_string entry in it's attributes dictionary attribute.

        *If no suitable factory in processing tool implementation available returns None*

        :type product_string: str
        :param product_string: *eopy.dataIO.Product.Product* object "product_string" entry of its attributes dictionary

        :return:
            :ProcessingFactory: *eopy.dataProcessing.AbstractProcessingTool*

            Factory suitable for input *eopy.dataIO.Product.Product* object

            *If no suitable Factory implementations available returns None*
        """
        return None

    def processProduct(self, product, **kwargs):
        """
        Returns processed version of input *eopy.dataIO.Product.Product* object.

        Uses functionality from *self.processingFactory*.

        :type product: eopy.dataIO.Product.Product
        :param product: Data product to product

        :type kwargs: -
        :param kwargs: Processing parameters

        :return:
            :product_processed: *eopy.dataIO.Product.Product*

            Processed data product
        """

        # Use processingFactory method processProduct() to process data product
        product_processed = self.processingFactory.processProduct(product, **kwargs)

        return product_processed


if __name__ == "__main__":
    pass
 

