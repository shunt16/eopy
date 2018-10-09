"""
Data factory for opening Sentinel-3/OLCI L1b data
"""

# todo - distribute variable names in self.getXVariableNames()

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
from datetime import datetime as dt
from datetime import timedelta
from copy import deepcopy

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from OLCISharedFactory import OLCISharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class OLCIL1Factory(OLCISharedFactory):
    """
    OLCIL1Factory is a sub-class of AbstractDataFactory for opening OLCI L1 products

    :Methods:
        :openProduct(product_path):
            Opens an in-memory representation of data product specified by product_path.

        :getData(product, variables, attributes, variable, [variable2, variable3, ...]):
            Returns variable[s] of in-memory product as an xarray data structure.

        :readVariables(product):
            Return dictionary with entry per variable for which data can be returned by getData(variable) method.
            Entry has variable name as key and dictionary of variables attributes as value. Used to assign variables
            attribute.

        :readAttributes(product):
            Return dictionary with product attributes. Used to assign attributes attribute.

        :getPixelValues(product, variables, attributes, variable):
            Returns pixel values of variable of in-memory product as a numpy.ndarray

        :simplify_attrs(...):
            Return a simplified form of input attributes dictionary suitable for netcdf file attributes

        :inherited from eopy.dataIO.AbstractDataFactory:
            :__init__():
                Initialises attributes
    """

    # Constants
    FACTORY_STRING = "OLCIL1Factory"
    TYPE_STRING = "OL_1_EFR"


if __name__ == "__main__":
    pass
