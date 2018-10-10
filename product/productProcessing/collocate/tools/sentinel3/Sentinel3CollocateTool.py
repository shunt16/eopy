"""
Collocate Tool eopy.product.productIO.Product.Product for Sentinel-3 data, subclass of AbstractProcessingTool
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname, basename
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(dataProcessing_directory)
from AbstractProcessingTool import AbstractProcessingTool

sys.path.append(pjoin(dirname(dirname(dirname(__file__))), "snappy_shared"))
from SnappyCollocateFactory import SnappyCollocateFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "01/10/2018"
__credits__ = []
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel3CollocateTool(AbstractProcessingTool):
    """
    Sentinel3CollocateTool is a sub-class of AbstractProcessingTool for collocating pairs of Sentinel-3 data products

    :Attributes:

        .. py:attribute:: processingFactory

            *obj*

            Instance of sub-class of *eopy.product.productProcessing.AbstractProcessingTool.AbstractProcessingTool* for
            processing for collocating pairs of Sentinel-3 products

    :Methods:
        .. py:method:: setProcessingFactory(...):

            Return the appropriate processing factory for a Sentinel-3 *eopy.product.productIO.Product.Product* object.

            *If no suitable factory in processor implementation available returns None*

        :Inherited from eopy.product.productProcessing.AbstractProcessingTool.AbstractProcessingTool:

            .. py:method:: __init__(...):

                Finds suitable processing factory for ``product_string`` if possible

            .. py:method:: processProduct(...):

                Returns processed version of input *eopy.product.productIO.Product.Product* object, using functionality 
                from processing factory
    """

    def setProcessingFactory(self, product_string):
        """
        Return the appropriate processing factory for a Sentinel-3 *eopy.product.productIO.Product.Product* object.

        :type product_string: str
        :param product_string: *eopy.product.productIO.Product.Product* object "product_string" entry of its attributes 
        dictionary

        :return:
            :ProcessingFactory: *cls*

            Processing Factory suitable for Sentinel-3 *eopy.product.productIO.Product.Product* object.

            *If no suitable processing factory in processor implementation available returns None*
        """

        # Return suitable Sentinel-3 Factory depending on product_string

        # OLCI L1 Radiance - Full Resolution / OLCI L1 Radiance - Reduced Resolution
        if (product_string == "OL_1_EFR") or (product_string == "OL_1_ERR"):
            return SnappyCollocateFactory
        # OLCI L2 Water & Atmos Parameters - Full Resolution
        if product_string == "OL_2_WFR":
            # todo - Write specific collocate factory for OL_2_WFR type products?
            return SnappyCollocateFactory
        # OLCI L2 Land & Atmos Parameters - Full Resolution
        if product_string == "OL_2_LFR":
            # todo - Write specific collocate factory for OL_2_LFR type products?
            return SnappyCollocateFactory
        # OLCI L2 Water & Atmos Parameters - Reduced Resolution
        if product_string == "OL_2_WRR":
            # todo - Write specific collocate factory for OL_2_WRR type products?
            return SnappyCollocateFactory
        # OLCI L2 Land & Atmos Parameters - Reduced Resolution
        if product_string == "OL_2_LRR":
            # todo - Write specific collocate factory for OL_2_LRR type products?
            return SnappyCollocateFactory
        # SLSTR L1 Radiance & Brightness Temperatures
        if product_string == "SL_1_RBT":
            # todo - Write specific collocate factory for SL_1_RBT type products?
            return SnappyCollocateFactory
        # SLSTR L2 Sea Surface Temperature
        if product_string == "SL_2_WCT":
            # todo - Write specific collocate factory for SL_2_WCT type products?
            return SnappyCollocateFactory
        # SLSTR L2 Sea Surface Temperature - GHRSTT like
        if product_string == "SL_2_WST":
            # todo - Write specific collocate factory for SL_2_WST type products?
            return SnappyCollocateFactory
        # SLSTR L2 Land Surface Temperature
        if product_string == "SL_2_LST":
            # todo - Write specific collocate factory for SL_2_LST type products?
            return SnappyCollocateFactory
        # Synergy - SLSTR and OLCI L1b ungridded bands
        if product_string == "SY_1_SYN":
            # todo - Write specific collocate factory for SY_1_SYN type products?
            return SnappyCollocateFactory
        # Synergy - Surface reflectances and aerosol parameters over land
        if product_string == "SY_2_SYN":
            # todo - Write specific collocate factory for SY_2_SYN type product?
            return SnappyCollocateFactory
        # Synergy - 1 km vegetation like product
        if product_string == "SY_2_VEG":
            # todo - Write specific collocate factory for SY_2_VEG type products?
            return SnappyCollocateFactory

        return None


if __name__ == "__main__":
    pass
 

