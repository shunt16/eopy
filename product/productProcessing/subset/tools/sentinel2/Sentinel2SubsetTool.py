"""
Subset Tool eopy.product.productIO.Product.Product for Sentinel-2 data, subclass of AbstractProcessingTool
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
from SnappySubsetFactory import SnappySubsetFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "21/06/2017"
__credits__ = ["Javier Gorrono", "Niall Origo"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Sentinel2SubsetTool(AbstractProcessingTool):
    """
    Sentinel2SubsetTool is a sub-class of AbstractProcessingTool for returning a subset of a Sentinel-2 data product,
    e.g. a region of interest

    :Attributes:

        .. py:attribute:: processingFactory

            *obj*

            Instance of sub-class of *eopy.product.productProcessing.AbstractProcessingTool.AbstractProcessingTool* for
            processing for converting given Sentinel-2 data with units of radiance to reflectance

    :Methods:
        .. py:method:: setProcessingFactory(...):

            Return the appropriate processing factory for a Sentinel-2 *eopy.product.productIO.Product.Product* object.

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
        Return the appropriate processing factory for a Sentinel-2 *eopy.product.productIO.Product.Product* object.

        :type product_string: str
        :param product_string: *eopy.product.productIO.Product.Product* object "product_string" entry of its attributes
        dictionary

        :return:
            :ProcessingFactory: *cls*

            Processing Factory suitable for Sentinel-2 *eopy.product.productIO.Product.Product* object.

            *If no suitable processing factory in processor implementation available returns None*
        """

        # Return generic SnappySubsetFactory if product Sentinel-2 product

        # MSI L1c Reflectance
        if product_string == "S2_MSI_Level-1C":
            # todo - Write specific subset factory for MSI L1C type products?
            return SnappySubsetFactory
        # MSI L2a
        if product_string == "S2_MSI_Level-2A":
            # todo - Write specific subset factory for MSI L2A type products?
            return SnappySubsetFactory

        return None


if __name__ == "__main__":
    pass
 

