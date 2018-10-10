"""
Main wrapper of NPL Data Collocation packages
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(__file__))
sys.path.append(dataProcessing_directory)
from AbstractProcessor import AbstractProcessor

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "1/10/2018"
__credits__ = []
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Collocate(AbstractProcessor):
    """
    Collocate class operates on pairs of eopy.product.productIO.Product in-memory data products, collocating the slave
    product onto the master product grid
    
    :Variables:
        .. py:attribute:: processor_directory

        *str*

        Directory of processor implementation

    :Attributes:

        :inherited from *eopy.dataIO.AbstractProcessor.AbstractProcessor*:

            .. py:attribute:: processingTool

            *cls*

            Object for processing a specific instance of *eopy.product.productIO.Product.Product* in-memory data
            products

    :Methods:

        :inherited from *eopy.product.productProcessing.AbstractProcessor.AbstractProcessor*:

            .. py:method:: run(...):

                Returns processed instance of *eopy.product.productIO.Product.Product*.
                Uses functionality from Processing Tool
    """

    processor_directory = dirname(__file__)


if __name__ == "__main__":
    pass
 

