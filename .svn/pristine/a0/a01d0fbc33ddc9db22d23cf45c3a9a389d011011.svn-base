"""
Contains class to be parent of implementations of parsing factory classes
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
from copy import deepcopy
from datetime import datetime as dt
from datetime import timedelta

'''___Third-Party Modules___'''

'''___NPL Modules___'''


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class AbstractParsingFactory:
    """
    AbstractParsingFactory is an inheritable class of which parsing factory implementations should be a sub-class of

    :Methods:
        .. py:method:: parseProduct(...):

            Returns dictionary of parsed product metadata.
    """

    def __init__(self):
        """
        Initialises the class
        """

        pass

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

        attributes = None

        return attributes


if __name__ == "__main__":
    pass
 

