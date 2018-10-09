"""
Main wrapper of NPL Data Subsetting packages
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
__created__ = "21/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Subset(AbstractProcessor):
    """
    Subset class operates on instances of eopy.dataIO.Product in-memory data products, returning a subset of the
    product, e.g. regions of interest.
    
    :Variables:
        .. py:attribute:: processor_directory

        *str*

        Directory of processor implementation

    :Attributes:

        :inherited from *eopy.dataIO.AbstractProcessor.AbstractProcessor*:

            .. py:attribute:: processingTool

            *cls*

            Object for processing a specific instance of *eopy.dataIO.Product.Product* in-memory data products

    :Methods:

        :inherited from *eopy.dataIO.AbstractProcessor.AbstractProcessor*:

            .. py:method:: run(...):

                Returns processed instance of *eopy.dataIO.Product.Product*. Uses functionality from Processing Tool
    """

    processor_directory = dirname(__file__)


if __name__ == "__main__":
    pass
 

