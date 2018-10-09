"""
Parsing tool for extracting information from a given Sentinel-3 product_path
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename
import re

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataParsing_directory = dirname(dirname(dirname(__file__)))
sys.path.append(dataParsing_directory)
from AbstractParsingTool import AbstractParsingTool

sys.path.append(dirname(__file__))
from OLCIL1ParsingFactory import OLCIL1ParsingFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel3ParsingTool(AbstractParsingTool):
    """
    Sentinel3ParsingTool is a sub-class of AbstractParsingTool for extracting information from a given Sentinel-3
    product path
    
    :Attributes:

        .. py:attribute:: parsingFactory

            *obj*

            Instance of sub-class of *eopy.dataParse.AbstractParsingFactory.AbstractParsingFactory* for
            extracting information from a given Sentinel-3 of a particular type

    :Methods:
        .. py:method:: setParsingFactory(...):

            Returns parsingFactory for data product with given ``product_path``.

            *If no suitable factory in parsing tool implementation available returns None*

        :Inherited from eopy.dataProcessing.AbstractProcessingTool.AbstractProcessingTool:

            .. py:method:: __init__(...):

                Initialises parsing tool

            .. py:method:: parseProduct(...):

                Returns dictionary of parsed product metadata.
    """

    def setParsingFactory(self, product_path):
        """
        Returns parsingFactory for data product with given ``product_path``.

        *If no suitable factory in parsing tool implementation available returns None*

        :type product_path: str
        :param product_path: Data product path

        :return:
            :ParsingFactory: *eopy.dataParse.AbstractParsingFactory.AbstractParsingFactory*

            Parsing factory suitable for Sentinel-3 input ``product_path``

            *If no suitable parsing factory implementations available returns None*
        """

        # Test if directory name matches any sentinel-3 parsing factory inputs

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
        #   return parsingFactory as appropriate
        if OLCIL1_pattern.match(product_directory):
            return OLCIL1ParsingFactory
        elif OLCIL2L_pattern.match(product_directory):
            # TODO - Write OLCI L1b parsing factory
            return None
        elif OLCIL2W_pattern.match(product_directory):
            # TODO - Write OLCI L2 L parsing factory
            return None
        elif SLSTRL1_pattern.match(product_directory):
            # TODO - Write OLCI L2 W parsing factory
            return None
        elif SLSTRL2LST_pattern.match(product_directory):
            # TODO - Write SLSTR L1 parsing factory
            return None
        elif SLSTRL2WST_pattern.match(product_directory):
            # TODO - Write SLSTR L2 LST parsing factory
            return None
        elif SLSTRL2WCT_pattern.match(product_directory):
            # TODO - Write SLSTR L2 WCT parsing factory
            return None
        elif SYNL1_pattern.match(product_directory):
            # TODO - Write SYN L1 parsing factory
            return None
        elif SYNL2_pattern.match(product_directory):
            # TODO - Write SYN L2 parsing factory
            return None
        elif SYNVGT_pattern.match(product_directory):
            # TODO - Write SYN VGT parsing factory
            return None
        else:
            return None

        return None


if __name__ == "__main__":
    pass
 

