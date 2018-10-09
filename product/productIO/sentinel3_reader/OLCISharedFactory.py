"""
Data factory for opening Sentinel-3/OLCI products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
import re

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(pjoin(dirname(dirname(__file__)), "snappy_shared"))
from SnappySharedFactory import SnappySharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/09/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


def convert_cc2sc(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class OLCISharedFactory(SnappySharedFactory):
    """
    OLCISharedFactory is a sub-class of AbstractDataFactory for opening OLCI products

    :Methods:
        :readAttributes(product):
            Return dictionary with product attributes. Used to assign attributes attribute.

        :inherited from eopy.product.productIO.snappy_shared.SnappySharedFactory.SnappySharedFactory:
            :__init__():
                Initialises attributes

            :openProduct(product_path):
                Opens an in-memory representation of data product specified by product_path.

            :getData(product, variables, attributes, variable, [variable2, variable3, ...]):
                Returns variable[s] of in-memory product as an xarray data structure.

            :readVariables(product):
                Return dictionary with entry per variable for which data can be returned by getData(variable) method.
                Entry has variable name as key and dictionary of variables attributes as value. Used to assign variables
                attribute.

            :getPixelValues(product, variables, attributes, variable):
                Returns pixel values of variable of in-memory product as a numpy.ndarray

            :simplify_attrs(...):
                Return a simplified form of input attributes dictionary suitable for netcdf file attributes


    """

    def addAttributes(self, products, attributes):
        """
        Return updated dictionary of multiple products attributes

        :type products: dict
        :param products: Dictionary of in-memory representation of `opened snappy.Product` data product

        :type attributes: dict
        :param attributes: Dictionary of multiple products attributes

        :return:
            :products: *dict*

            Dictionary of in-memory representation of `opened snappy.Product` data product

            :attributes: *list*

            Dictionary of multiple products attributes
        """

        # Access metadata root
        product = products[0]["product"]
        metadata_root = product.getMetadataRoot()
        product_meta = metadata_root.getElement("Manifest").getElement("metadataSection")

        # > product attributes:
        info_meta = product_meta.getElement("olciProductInformation")

        # -- spatial sampling
        attributes['spatial_sampling_al'] = product_meta.getElement("olciProductInformation") \
                                                        .getElement("samplingParameters") \
                                                        .getAttributeDouble("alSpatialSampling")
        attributes['spatial_sampling_ac'] = product_meta.getElement("olciProductInformation") \
                                                        .getElement("samplingParameters") \
                                                        .getAttributeDouble("acSpatialSampling")
        # -- earth_sun_distance
        attributes['earth_sun_distance'] = int(info_meta.getAttributeString('earthSunDistance'))
        # -- OCL status
        attributes['ocl_status'] = bool(info_meta.getAttributeString('oclStatus'))

        # > platform meta
        platform_meta = product_meta.getElement("platform")
        #   -- platform
        attributes["platform"] = platform_meta.getAttributeString("familyName") + \
                                 platform_meta.getAttributeString("number")
        #   -- instrument
        attributes["instrument"] = platform_meta.getElement('Instrument') \
                                                .getElement("familyName") \
                                                .getAttributeString("abbreviation")

        # > pixel quality attributes:
        quality_meta = info_meta.getElement("pixelQualitySummary")
        for elem in quality_meta.getElementNames():
            attributes[convert_cc2sc(elem)+"_percentage"] = quality_meta.getElement(elem) \
                                                                        .getAttributeDouble("percentage")

        # > pixel classification attributes:
        classification_meta = info_meta.getElement("classificationSummary")
        for elem in classification_meta.getElementNames():
            attributes[convert_cc2sc(elem)+"_percentage"] = classification_meta.getElement(elem) \
                                                                               .getAttributeDouble("percentage")

        return products,  attributes


if __name__ == "__main__":
    pass
