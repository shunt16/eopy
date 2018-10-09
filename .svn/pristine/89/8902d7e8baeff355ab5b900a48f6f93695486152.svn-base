"""
Subset Tool eopy.dataIO.Product.Product for Sentinel-3 data, subclass of AbstractProcessingTool
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

sys.path.append(dirname(__file__))
from OLCIL1SubsetFactory import OLCIL1SubsetFactory

sys.path.append(pjoin(dirname(dirname(dirname(__file__))), "snappy_shared"))
from SnappySubsetFactory import SnappySubsetFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "21/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel3SubsetTool(AbstractProcessingTool):
    """
    Sentinel3SubsetTool is a sub-class of AbstractProcessingTool for returning a subset of a Sentinel-3 data product,
    e.g. a region of interest

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

            Processing Factory suitable for Sentinel-3 *eopy.dataIO.Product.Product* object.

            *If no suitable processing factory in processor implementation available returns None*
        """

        # Return suitable Sentinel-3 SubsetFactory depending on product_string

        # OLCI L1 Radiance - Full Resolution / OLCI L1 Radiance - Reduced Resolution
        if (product_string == "OL_1_EFR") or (product_string == "OL_1_ERR"):
            return OLCIL1SubsetFactory
        # OLCI L2 Water & Atmos Parameters - Full Resolution
        if product_string == "OL_2_WFR":
            # todo - Write specific subset factory for OL_2_WFR type products?
            return SnappySubsetFactory
        # OLCI L2 Land & Atmos Parameters - Full Resolution
        if product_string == "OL_2_LFR":
            # todo - Write specific subset factory for OL_2_LFR type products?
            return SnappySubsetFactory
        # OLCI L2 Water & Atmos Parameters - Reduced Resolution
        if product_string == "OL_2_WRR":
            # todo - Write specific subset factory for OL_2_WRR type products?
            return SnappySubsetFactory
        # OLCI L2 Land & Atmos Parameters - Reduced Resolution
        if product_string == "OL_2_LRR":
            # todo - Write specific subset factory for OL_2_LRR type products?
            return SnappySubsetFactory
        # SLSTR L1 Radiance & Brightness Temperatures
        if product_string == "SL_1_RBT":
            # todo - Write specific subset factory for SL_1_RBT type products?
            return SnappySubsetFactory
        # SLSTR L2 Sea Surface Temperature
        if product_string == "SL_2_WCT":
            # todo - Write specific subset factory for SL_2_WCT type products?
            return SnappySubsetFactory
        # SLSTR L2 Sea Surface Temperature - GHRSTT like
        if product_string == "SL_2_WST":
            # todo - Write specific subset factory for SL_2_WST type products?
            return SnappySubsetFactory
        # SLSTR L2 Land Surface Temperature
        if product_string == "SL_2_LST":
            # todo - Write specific subset factory for SL_2_LST type products?
            return SnappySubsetFactory
        # Synergy - SLSTR and OLCI L1b ungridded bands
        if product_string == "SY_1_SYN":
            # todo - Write specific subset factory for SY_1_SYN type products?
            return SnappySubsetFactory
        # Synergy - Surface reflectances and aerosol parameters over land
        if product_string == "SY_2_SYN":
            # todo - Write specific subset factory for SY_2_SYN type product?
            return SnappySubsetFactory
        # Synergy - 1 km vegetation like product
        if product_string == "SY_2_VEG":
            # todo - Write specific subset factory for SY_2_VEG type products?
            return SnappySubsetFactory

        return None


if __name__ == "__main__":
    pass
 

