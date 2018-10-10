"""
Collocate factory for *eopy.product.productIO.Product.Product* objects which contain instantiations of snappy products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from copy import deepcopy
import re

'''___Third-Party Modules___'''
from snappy import GPF
import jpy

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractProcessingFactory import AbstractProcessingFactory

from eopy import Product


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "01/10/2018"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.1"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class SnappyCollocateFactory(AbstractProcessingFactory):
    """
    SnappyCollocateFactory is a sub-class of *AbstractProcessingFactory* for collocating a pair of Sentinel
    *eopy.product.productIO.Product.Product* products.

    :Methods:
        .. py:method:: processProduct(...):

            Returns *eopy.product.productIO.Product.Product* product collocated with master product

        .. py:method:: updateProductName(...):

            Return product_name entry of processed *eopy.product.productIO.Product.Product* product dictionary attribute

        .. py:method:: collocateProducts(...):

            Returns *snappy.Product* product collocated with master product

        .. py:method:: updateProductVariablesAttributes(...):

            Return updates variables attribute of processed *eopy.product.productIO.Product.Product* product attribute.

        .. py:method:: updateCommonAttributes(...):

            Returns updated ``attributes`` attribute for collocated *eopy.product.productIO.Product.Product* product
            for common snappy product attributes

        .. py:method:: updateSpecificAttributes(...):

            Returns updated ``attributes`` attribute for collocated *eopy.product.productIO.Product.Product* product
            for specific individual products snappy product attributes (should be updated in subclasses)

        .. py:method:: updateAttributesProcessingLog(...):

            Returns ``attributes`` attribute of processed *eopy.product.productIO.Product.Product* product with updated
            "product_processing" log entry

        .. py:method:: updateVariables(...):

            Return update variables list attribute of processed *eopy.product.productIO.Product.Product* data product.

        .. py:method:: updateVariables(...):

            Return update variables dictionary attribute of processed *eopy.product.productIO.Product.Product* object.

        :inherited from eopy.dataProcessing.AbstractProcessingFactory.AbstractProcessingFactory:

            .. py:method:: __init__():

                Initialises the class
    """

    def processProduct(self, product, **kwargs):
        """
        Returns *eopy.product.productIO.Product.Product* product collocated with master product

        :type product: eopy.product.productIO.Product.Product
        :param product: Data product to collocate

        :type master: eopy.product.productIO.Product.Product
        :param master: Data product to collocate product to (pixel values conserved)

        :param resampling: str
        :param resampling: resampling method to use on product in collocation process. Options

        * "nearest_neighbour" (default)
        * "bilinear_interpolation"
        * "cubic_convolution"
        * "bisinc_interpolation"
        * "bicubic_interpolation"

        :return:
            :product_processed: *eopy.product.productIO.Product.Product*

            Collocated data product
        """

        # Initialise subset empty subset product
        product_processed = Product()
        product_processed.dataReader = product.dataReader
        product_processed.product = [{} for i in range(len(product.product))]

        ################################################################################################################
        # 1. Update product attribute
        ################################################################################################################

        # Loop through products in product attribute and update dictionary entries

        master_product = kwargs["master"]
        resampling = kwargs["resampling"] if "resampling" in kwargs.keys() else "nearest_neighbour"

        for i, (p, m_p) in enumerate(zip(product.product, master_product.product)):

            # Collocate products
            product_processed.product[i]["product_name"] = self.updateProductName(p["product_name"])
            product_processed.product[i]["product"] = self.collocateProducts(p["product"], m_p["product"],
                                                                             resampling=resampling)
            product_processed.product[i]["variables"] = self.updateProductVariablesAttributes(p["variables"])

        ################################################################################################################
        # 2. Update attributes attributes and variables
        ################################################################################################################

        product_processed.variables = self.updateVariables(product_processed, product)

        # Update common snappy product attributes
        product_processed.attributes = self.updateCommonAttributes(product_processed, product)

        # Update processing log
        product_processed.attributes = self.updateAttributesProcessingLog(product_processed, "collocate",
                                                                          {"slave_product": product.
                                                                                             attributes["product_name"],
                                                                           "master_product": master_product.
                                                                                             attributes["product_name"],
                                                                           "resampling": resampling})

        # Update product specific attributes - should be updated in product specific sub-classes
        product_processed.attributes = self.updateSpecificAttributes(product_processed, product)

        return product_processed

    def updateProductName(self, original_product_name):
        """
        Return product_name entry of processed *eopy.product.productIO.Product.Product* product dictionary attribute.

        :type original_product_name: str
        :param original_product_name: Product name entry of original *eopy.product.productIO.Product.Product* product
        dictionary attribute

        :return:
            :new_product_name: *str*

            Updated product name entry *eopy.product.productIO.Product.Product* product dictionary attribute for
            processed product
        """

        return original_product_name

    def collocateProducts(self, product, master, resampling="nearest_neighbour"):
        """
        Returns *snappy.Product* product collocated with master product

        :type product: *snappy.Product*
        :param product: In-memory data product

        :type master: eopy.product.productIO.Product.Product
        :param master: Data product to collocate product to (pixel values conserved)

        :param resampling: str
        :param resampling: resampling method to use on product in collocation process. Options

        * "nearest_neighbour" (default)
        * "bilinear_interpolation"
        * "cubic_convolution"
        * "bisinc_interpolation"
        * "bicubic_interpolation"

        :return:
            :product_processed: *snappy.Product*

            Collocated data product
        """

        HashMap = jpy.get_type('java.util.HashMap')

        source_products = HashMap()
        source_products.put('master', master)
        source_products.put('slave', product)

        params = HashMap()
        params.put("targetProductType", "collocate")
        params.put("renameMasterComponents", "true")
        params.put("renameSlaveComponents", "false")
        params.put("masterComponentPattern", "${ORIGINAL_NAME}_M")
        # params.put("slaveComponentPattern", "${ORIGINAL_NAME}_S")
        params.put("rasamplingType", resampling.upper())

        product_processed = GPF.createProduct("Collocate", params, source_products)

        return product_processed

    def updateProductVariablesAttributes(self, original_product_variables_attrs):
        """
        Return updates variables attribute of processed *eopy.product.productIO.Product.Product* product attribute.

        :type original_product_variables_attrs: list
        :param original_product_variables_attrs: Original data product product attribute variables attribute. Specifics
        the variables a particular product can open

        :return:
            :new_product_variables_attrs: *list*

            updated data product product attribute variables attribute
        """

        return original_product_variables_attrs

    def updateCommonAttributes(self, product_processed, product):
        """
        Returns updated ``attributes`` attribute for collocated *eopy.product.productIO.Product.Product* product
        for common snappy product attributes

        :type product_processed: `eopy.product.productIO.Product.Product`
        :param product_processed: data product with units converted from radiance to reflectance

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        # Duplicate original
        new_attrs = deepcopy(product.attributes)

        return new_attrs

    def updateSpecificAttributes(self, product_processed, product, **kwargs):
        """
        Returns updated ``attributes`` attribute for collocated *eopy.product.productIO.Product.Product* product
        for specific individual products snappy product attributes (should be updated in subclasses)

        :type product_processed: `eopy.product.productIO.Product.Product`
        :param product_processed: data product with units converted from radiance to reflectance

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        # Duplicate original
        new_attrs = deepcopy(product_processed.attributes)

        return new_attrs

    def updateAttributesProcessingLog(self, product_processed, processing_name, processing_parameter):
        """
        Returns ``attributes`` attribute of processed *eopy.product.productIO.Product.Product* product with updated
        "product_processing" log entry

        :type product_processed: `eopy.product.productIO.Product.Product`
        :param product_processed: processed data product

        :type processing_name: str
        :param processing_name: name of processing

        :type processing_parameter: dict
        :param processing_parameter: processing parameter, to describe processing

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        # Duplicate original
        new_attrs = deepcopy(product_processed.attributes)

        if len(product_processed.product) > 1:
            # Attach log of processing
            for p in product_processed.product:
                new_attrs["product_processing_" + p["product_name"]].append({"processing_name": processing_name,
                                                                             "processing_parameters":
                                                                                            processing_parameter})
        else:
            new_attrs["product_processing"].append({"processing_name": processing_name,
                                                    "processing_parameters": processing_parameter})

        return new_attrs

    def updateVariables(self, product_processed, product):
        """
        Return update variables list attribute of processed *eopy.product.productIO.Product.Product* data product.

        :type product_processed: `eopy.product.productIO.Product.Product`
        :param product_processed: data product with units converted from radiance to reflectance

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_variables: *list*

            updated list of all data product variable objects
        """

        # Start by initialising copy of original attributes
        new_variables = deepcopy(product.variables)

        return new_variables


if __name__ == "__main__":
    pass
 

