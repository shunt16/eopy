"""
Parsing factory for Sentinel-3 OLCI L1 products with a given path
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename
from os.path import join as pjoin
from copy import deepcopy
import re
from datetime import datetime as dt
from datetime import timedelta

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataParsing_directory = dirname(dirname(dirname(__file__)))
sys.path.append(dataParsing_directory)
from AbstractParsingFactory import AbstractParsingFactory


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class OLCIL1ParsingFactory(AbstractParsingFactory):
    """
    OLCIL1ParsingFactory is a sub-class of *AbstractParsingFactory* for parsing metadata for OLCI L1 products, from
    their product path

    :Methods:

        .. py:method:: parseProduct(...):

            Returns dictionary of parsed product metadata for OLCI L1 products.

            :inherited from eopy.dataProcessing.AbstractProcessingFactory.AbstractProcessingFactory:

                .. py:method:: __init__():

                    Initialises the class
    """

    def parseProduct(self, product_path, detail="min", **kwargs):
        """
        Returns dictionary of parsed product metadata.

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

        attributes = {}

        path = basename(dirname(product_path))

        # > product attributes
        # -- product type string
        attributes["product_string"] = path[4:12]
        # -- acquisition data
        time_fmt = "%Y%m%d"
        attributes["date"] = dt.strptime(path[16:24], time_fmt)
        # -- acquisition time
        time_fmt = "%Y%m%dT%H%M%S"
        attributes["start_time"] = dt.strptime(path[16:31], time_fmt)
        attributes["end_time"] = dt.strptime(path[32:47], time_fmt)
        # -- creation time
        attributes["creation_time"] = dt.strptime(path[48:63], time_fmt)

        # > mission attributes
        #  -- mission
        attributes["mission"] = "Sentinel-3"+path[2]
        # -- mission type
        attributes["mission_type"] = "satellite"
        # -- instrument
        attributes["instrument"] = "OLCI"

        return attributes


if __name__ == "__main__":
    pass
 

