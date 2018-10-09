"""
Contains class to be parent of implementations of processing factory classes
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


class AbstractProcessingFactory:
    """
    AbstractProcessingFactory is an inheritable class of which specific processing factory implementations for
    *eopy.dataProcessing* processor packages should be a sub-class of

    :Methods:
        .. py:method:: processProduct(...):

            Returns processed version of input *eopy.dataIO.Product.Product* object
    """

    def __init__(self):
        """
        Initialises the class
        """

        pass

    def processProduct(self, product, **kwargs):
        """
        Returns processed version of input *eopy.dataIO.Product.Product* object

        :type product: eopy.dataIO.Product.Product
        :param product: Data product to process

        :return:
            :product_processed: *eopy.dataIO.Product.Product*

            Processed data product
        """

        product_processed = product

        return product_processed



if __name__ == "__main__":
    pass
 

