"""
Main wrapper of NPL data processor packages
"""

'''___Built-In Modules___'''
from os.path import dirname
import sys

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from ProductProcessingTool import ProductProcessingTool

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class AbstractProcessor:
    """
    AbstractProcessor is an inheritable class of which specific processor implementations for *eopy.dataProcessing*
    processor packages should be a sub-class of

    :Variables:
        .. py:attribute:: processor_directory

        *str*

        Directory of processor implementation.

    :Attributes:
        .. py:attribute:: processingTool:

        *eopy.dataProcessing.AbstractProcessingTool*

        Object for processing a specific instance of *eopy.dataIO.Product.Product* in-memory data products.
    
    :Methods:
        .. py:method:: run(...):

            Returns processed instance of *eopy.dataIO.Product.Product*

            Uses functionality from Processing Tool
    """

    processor_directory = None

    def __init__(self):
        """
        Initialises the class
        """

        # Initialise attributes
        self.processingTool = None

    def run(self, product, **kwargs):
        """
        Returns processed instance of *eopy.dataIO.Product.Product*

        Uses functionality from Processing Tool

        :type product: eopy.dataIO.Product.Product
        :param product: Data product

        :return:
            :product_processed: *eopy.dataIO.Product.Product*

            Data product after processing
        """

        productProcessingTool = ProductProcessingTool()
        processingTool = productProcessingTool.setProcessingTool(self.processor_directory, product.attributes['product_string'])

        # Processed product
        self.processingTool = processingTool(product.attributes['product_string'])
        product_processed = self.processingTool.processProduct(product, **kwargs)

        return product_processed


if __name__ == "__main__":
    pass
 

