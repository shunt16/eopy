"""
Data reader for Sentinel-2 data products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename
from os.path import join as pjoin
import re

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from MSIL1Factory import MSIL1Factory
from MSIL2Factory import MSIL2Factory

sys.path.append(dirname(dirname(__file__)))
from AbstractDataReader import AbstractDataReader


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/09/2018"
__credits__ = ["Javier Gorrono", "Niall Origo"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel2DataReader(AbstractDataReader):
    """
    Sentinel2DataReader is a sub-class of AbstractDataReader for reading Sentinel-2 data products

    :Attributes:
        .. py:attribute:: dataFactory

            *eopy.dataIO.AbstractDataFactory.AbstractDataFactory*

            Instance of sub-class of product factory for reading Sentinel-2 product data

    :Methods:
        .. py:method:: setDataFactory(...):

            Return Sentinel-2 product factory suitable for data product at product_path

            *If no suitable factory available returns None*

        :Inherited from *eopy.dataIO.AbstractDataReader.AbstractDataReader*:

            .. py:method:: __init__(...):

                Initialises attributes and finds suitable product factory for product_path if provided and possible.

            .. py:method:: openProduct(...):

                Opens an in-memory representation of data product specified by product_path. Inherits this functionality
                from *self.dataFactory*.

            .. py:method:: getData(...):

                Returns variable[s] of in-memory product as an xarray data structure. Inherits this functionality from
                *self.dataFactory*.
    """

    def setDataFactory(self, product_path):
        """
        Return Sentinel-2 product factory suitable for data product at product_path

        *If no suitable factory available returns None*

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :DataFactory: *cls*

            Sentinel-2 Product Data Factory
        """

        # Test if directory name matches any sentinel-2 product factory inputs

        # > Get directory of product
        product_directory = basename(dirname(product_path))

        # > Possible regular expression for Sentinel-2 products
        MSIL1_pattern = re.compile(r"S2.*._MSIL1C_.*.SAFE")     # MSI L1c
        MSIL2_pattern = re.compile(r"S2.*._MSIL2A_.*.SAFE")  # MSI L1c

        # > Check if input product_path matches any Sentinel-2 product regular expressions
        #   return dataFactory as appropriate
        if MSIL1_pattern.match(product_directory):
            return MSIL1Factory
        elif MSIL2_pattern.match(product_directory):
            return MSIL2Factory
        else:
            return None

if __name__ == "__main__":
    pass
