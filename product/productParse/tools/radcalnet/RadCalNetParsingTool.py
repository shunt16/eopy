"""
Parsing tool for extracting information from a given radcalnet product_path
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
from RadCalNetParsingFactory import RadCalNetParsingFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class RadCalNetParsingTool(AbstractParsingTool):
    """
    RadCalNetParsingTool is a sub-class of AbstractParsingTool for extracting information from a given radcalnet
    product path
    
    :Attributes:

        .. py:attribute:: parsingFactory

            *obj*

            Instance of sub-class of *eopy.dataParse.AbstractParsingFactory.AbstractParsingFactory* for
            extracting information from a given radcalnet product

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

            Parsing factory suitable for radcalnet input ``product_path``

            *If no suitable parsing factory implementations available returns None*
        """

        # Test if directory name matches any sentinel-3 parsing factory inputs

        # > Get directory of product
        product_directory = basename(product_path)

        # > Possible regular expression for radcalnet products
        BTCN_pattern = re.compile(r"BTCN.*")    # Baotou
        RVUS_pattern = re.compile(r"RVUS.*")    # Railroad Valley
        LCFR_pattern = re.compile(r"LCFR.*")    # La Crau
        GONA_pattern = re.compile(r"GONA.*")    # Gobabeb

        # > Check if input product_path matches any radcalnet product regular expressions
        #   return parsingFactory as appropriate
        if BTCN_pattern.match(product_directory) or RVUS_pattern.match(product_directory) or \
                LCFR_pattern.match(product_directory) or GONA_pattern.match(product_directory):
            return RadCalNetParsingFactory

        return None


if __name__ == "__main__":
    pass
