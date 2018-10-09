"""
Main wrapper of NPL Radiance2Reflectance unit conversion processor package, sub-class of Abstract Processor
"""

'''___Built-In Modules___'''
from os.path import dirname
import sys

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(dirname(__file__)))
sys.path.append(dataProcessing_directory)
from AbstractProcessor import AbstractProcessor


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Radiance2Reflectance(AbstractProcessor):
    """
    Radiance2Reflectance class operates on instances of *eopy.dataIO.Product.Product* in-memory data products which have
    units of radiance and converts them to reflectance
    
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
 

