"""
Processing tool for converting given Sentinel-3 eopy.dataIO.Product.Product instances in units of radiance to
reflectance
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(dirname(dirname(dirname(__file__)))))
sys.path.append(dataProcessing_directory)
from AbstractProcessingTool import AbstractProcessingTool

sys.path.append(dirname(__file__))
from OLCIL1Radiance2ReflectanceFactory import OLCIL1Radiance2ReflectanceFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel3Radiance2ReflectanceTool(AbstractProcessingTool):
    """
    Sentinel3Radiance2ReflectanceTool is a sub-class of AbstractProcessingTool for converting given Sentinel-3 data
    products with units of radiance to reflectance
    
    :Attributes:

        .. py:attribute:: processingFactory

            *obj*

            Instance of sub-class of *eopy.dataProcessing.AbstractProcessingTool.AbstractProcessingTool* for
            processing for converting given Sentinel-3 data with units of radiance to reflectance

    :Methods:
        .. py:method:: setProcessingFactory(...):

            Return the appropriate processing factory for a Sentinel-3 *eopy.dataIO.Product.Product* object.

            *If no suitable factory in processor implementation available returns None*

        :Inherited from eopy.dataProcessing.AbstractProcessingTool.AbstractProcessingTool:

            .. py:method:: __init__(...):

                Finds suitable processing factory for ``product_string`` if possible

            .. py:method:: processProduct(...):

                Returns processed version of input *eopy.dataIO.Product.Product* object, using functionality from
                processing factory
    """

    def setProcessingFactory(self, product_string):
        """
        Return the appropriate processing factory for a Sentinel-3 *eopy.dataIO.Product.Product* object.

        :type product_string: str
        :param product_string: *eopy.dataIO.Product.Product* object "product_string" entry of its attributes dictionary

        :return:
            :ProcessingFactory: *cls*

            Processing Factory suitable for Sentinel-3 *eopy.dataIO.Product.Product* object with units of radiance.

            *If no suitable processing factory in processor implementation available returns None*
        """

        # Return suitable Sentinel-3 Reflectance2RadianceFactory depending on product_string

        # OLCI L1 Radiance - Full Resolution / OLCI L1 Radiance - Reduced Resolution
        if (product_string == "OL_1_EFR") or (product_string == "OL_1_ERR"):
            return OLCIL1Radiance2ReflectanceFactory
        # SLSTR L1 Radiance & Brightness Temperatures
        if product_string == "SL_1_RBT":
            # todo - write subset factory for SL_1_RBT type products
            return None
        # Synergy - SLSTR and OLCI L1b ungridded bands
        if product_string == "SY_1_SYN":
            # todo - write subset factory for SY_1_SYN type products
            return None

        return None


if __name__ == "__main__":
    pass
 

