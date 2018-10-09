"""
Parsing factory for radcalnet products with a given path
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename, splitext
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


class RadCalNetParsingFactory(AbstractParsingFactory):
    """
    RadCalnetParsingFactory is a sub-class of *AbstractParsingFactory* for parsing metadata for radcalnet products, from
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

        path = basename(product_path)

        # > product attributes
        # -- product type string
        ext = splitext(path)[1][1:]
        if ext == "output":
            attributes["product_string"] = path[:4]
        elif ext == "input":
            attributes["product_string"] = path[:4] + "_IN"

        # > date
        attributes["date"] = dt(int(path[7:11]), 1, 1) + timedelta(int(path[12:15]) - 1)

        # > mission attributes
        #  -- mission
        attributes["mission"] = "radcalnet"
        # -- mission type
        attributes["mission_type"] = "ground"
        # -- site
        attributes["site"] = path[:4]
        # -- site_config
        attributes["site_config"] = path[4:6]

        return attributes


if __name__ == "__main__":
    pass
 

