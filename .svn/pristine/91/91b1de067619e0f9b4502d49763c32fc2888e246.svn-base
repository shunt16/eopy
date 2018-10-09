"""
Data reader for Sentinel-3 data products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename
from os.path import join as pjoin
import re

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractDataReader import AbstractDataReader

sys.path.append(dirname(__file__))
from OLCIL1Factory import OLCIL1Factory
from OLCIL2LFactory import OLCIL2LFactory
from OLCIL2WFactory import OLCIL2WFactory
from SLSTRL1Factory import SLSTRL1Factory

sys.path.append(pjoin(dirname(dirname(__file__)), "snappy_shared"))
from SnappySharedFactory import SnappySharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel3DataReader(AbstractDataReader):
    """
    Sentinel3DataReader is a sub-class of AbstractDataReader for reading Sentinel-3 data products

    :Attributes:
        .. py:attribute:: dataFactory

            *eopy.dataIO.AbstractDataFactory.AbstractDataFactory*

            Instance of sub-class of product factory for reading Sentinel-3 product data

    :Methods:
        .. py:method:: setDataFactory(...):

            Return Sentinel-3 product factory suitable for data product at product_path

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
        Return Sentinel-3 product factory suitable for data product at product_path

        *If no suitable factory available returns None*

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :DataFactory: *eopy.dataIO.AbstractDataFactory.AbstractDataFactory*

            Sentinel-3 Product Data Factory
        """

        # Test if directory name matches any sentinel-3 product factory inputs

        # > Get directory of product
        product_directory = basename(dirname(product_path))

        # > Possible regular expression for Sentinel-3 products
        OLCIL1_pattern = re.compile(r"S3.?_OL_1_E[RF]R_.*.SEN3")     # OLCI L1b
        OLCIL2L_pattern = re.compile(r"S3.?_OL_2_(L[FR]R)_.*.SEN3")  # OLCI L2 L
        OLCIL2W_pattern = re.compile(r"S3.?_OL_2_(W[FR]R)_.*.SEN3")  # OLCI L2 W
        SLSTRL1_pattern = re.compile(r"S3.?_SL_1_RBT.*")             # SLSTR L1
        SLSTRL2LST_pattern = re.compile(r"S3.?_SL_2_LST_.*.SEN3")    # SLSTR L2 LST
        SLSTRL2WST_pattern = re.compile(r"S3.?_SL_2_WST_.*.SEN3")    # SLSTR L2 WST
        SLSTRL2WCT_pattern = re.compile(r"S3.?_SL_2_WCT_.*.SEN3")    # SLSTR L2 WCT
        SYNL1_pattern = re.compile(r"S3.?_SY_1_SYN_.*")              # SYN L1
        SYNL2_pattern = re.compile(r"S3.?_SY_2_SYN_.*.SEN3")         # SYN L2
        SYNVGT_pattern = re.compile(r"S3.?_SY_2_SYN_.*.SEN3")        # SYN VGT

        # > Check if input product_path matches any Sentinel-3 product regular expressions
        #   return dataFactory as appropriate
        if OLCIL1_pattern.match(product_directory):
            return OLCIL1Factory
        elif OLCIL2L_pattern.match(product_directory):
            return OLCIL2LFactory
        elif OLCIL2W_pattern.match(product_directory):
            return OLCIL2WFactory
        elif SLSTRL1_pattern.match(product_directory):
            return SLSTRL1Factory
        elif SLSTRL2LST_pattern.match(product_directory):
            # TODO - Write specific SLSTR L2 LST factory?
            return SnappySharedFactory
        elif SLSTRL2WST_pattern.match(product_directory):
            # TODO - Write specific SLSTR L2 WST factory?
            return SnappySharedFactory
        elif SLSTRL2WCT_pattern.match(product_directory):
            # TODO - Write specific SLSTR L2 WCT factory?
            return SnappySharedFactory
        elif SYNL1_pattern.match(product_directory):
            # TODO - Write specific SYN L1 factory?
            return SnappySharedFactory
        elif SYNL2_pattern.match(product_directory):
            # TODO - Write specific SYN L2 factory?
            return SnappySharedFactory
        elif SYNVGT_pattern.match(product_directory):
            # TODO - Write specific SYN VGT factory?
            return SnappySharedFactory
        else:
            return None

if __name__ == "__main__":
    pass
