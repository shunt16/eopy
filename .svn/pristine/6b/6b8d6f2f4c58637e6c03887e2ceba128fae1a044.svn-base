"""
Common data factory for opening Sentinel-2/MSI L1/2 products
"""

# todo - end_time
# todo - ecmwf data

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
import re
from datetime import datetime as dt
from datetime import timedelta
from copy import deepcopy

'''___Third-Party Modules___'''
from snappy import GPF
from snappy import HashMap

'''___NPL Modules___'''
sys.path.append(pjoin(dirname(dirname(__file__)), "snappy_shared"))
from SnappySharedFactory import SnappySharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "23/09/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class MSISharedFactory(SnappySharedFactory):
    """
    MSISharedFactory is a sub-class of SnappySharedFactory for opening MSI products

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

    def openProduct(self, product_path):
        """
        Opens an in-memory represenation of snappy data product at specified path with metadata

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :products: *dict*

            List of product dictionaries - which themselves contain in-memory representation of opened `snappy.Product`
            data products, one resampled to each S2 band resolution

            :variables: *list*

            List of products variables as ``Variable`` or ``SpectralVariable`` class objects.

            :attributes: *dict*

            Dictionary of product attributes.
        """

        # Open S2 product 3 times, once for each spatial resolution
        products = self.openMultipleProducts([{"product_name": "10m_resolution",
                                               "product_path": product_path},
                                              {"product_name": "20m_resolution",
                                               "product_path": product_path},
                                              {"product_name": "60m_resolution",
                                               "product_path": product_path}])

        product_name = products[0]["product"].getName()

        # Resample the products to each of the instrument spatial resolutions
        for i, res in enumerate([10, 20, 60]):
            products[i]['product'] = self._resample_product(products[i]['product'], res)

        products, variables = self.readVariables(products)

        products, attributes = self.readAttributes(products)
        attributes["product_name"] = product_name
        products, attributes = self.addAttributes(products, attributes)
        for i, res in enumerate([10, 20, 60]):
            attributes["product_processing_" + products[i]['product_name']].append({"processing_name": "resample",
                                                                                    "processing_parameters":
                                                                                        {"resolution": res}})
        return products, variables, attributes

    def _resample_product(self, product, resolution):
        parameters = HashMap()
        parameters.put('targetResolution', resolution)
        parameters.put('upsampling', 'Bilinear')

        return GPF.createProduct('Resample', parameters, product)

    def addAttributes(self, products, attributes):
        """
        Return dictionary of product attributes

        :type products: *list*
        :param products: ist of product dictionaries

        :return:
            :attributes: *dict*

            dictionary of product attributes
        """

        attributes["instrument"] = "MSI"
        attributes["end_time"] = None

        # Quality Information
        metadata_root = products[0]["product"].getMetadataRoot()
        attributes["platform"] = metadata_root.getElement('Level-1C_User_Product').getElement('General_Info') \
                                              .getElement('Product_Info').getElement('Datatake') \
                                              .getAttributeString("SPACECRAFT_NAME")

        attributes["cloudy_pixels_percentage"] = list(metadata_root.getElement("Granules").getElements())[0] \
                                                                   .getElement("Quality_Indicators_Info") \
                                                                   .getElement("Image_Content_QI") \
                                                                   .getAttributeDouble("CLOUDY_PIXEL_PERCENTAGE")
        attributes["degraded_msi_data_percentage"] = list(metadata_root.getElement("Granules").getElements())[0] \
                                                                       .getElement("Quality_Indicators_Info") \
                                                                       .getElement("Image_Content_QI") \
                                                                       .getAttributeDouble("CLOUDY_PIXEL_PERCENTAGE")

        return products, attributes


if __name__ == "__main__":
    pass
