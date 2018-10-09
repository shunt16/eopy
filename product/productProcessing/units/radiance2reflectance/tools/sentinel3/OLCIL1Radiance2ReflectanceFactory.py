"""
Processing factory for converting Sentinel-3 OLCI L1 eopy.product.productIO.Product.Product objects to reflectance units
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
from copy import deepcopy
import re

'''___Third-Party Modules___'''
from snappy import GPF
import jpy

'''___NPL Modules___'''
productProcessing_directory = dirname(dirname(dirname(dirname(dirname(__file__)))))
sys.path.append(productProcessing_directory)
from AbstractProcessingFactory import AbstractProcessingFactory

productIO_directory = pjoin(dirname(productProcessing_directory), "productIO")
sys.path.append(productIO_directory)
from Product import Product


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class OLCIL1Radiance2ReflectanceFactory(AbstractProcessingFactory):
    """
    OLCIL1Radiance2ReflectanceFactory is a sub-class of *AbstractProcessingFactory* for converting Sentinel-3 OLCI L1
    *eopy.product.productIO.Product.Product* objects to units of reflectance.

    :Methods:
        .. py:method:: processProduct(...):

            Returns input *eopy.product.productIO.Product.Product* OLCI L1 data object in units of reflectance

        .. py:method:: updateProductName(...):

            Return product_name entry of processed *eopy.product.productIO.Product.Product* product dictionary attribute

        .. py:method:: convertProduct(...):

            Return OLCI *snappy.Product* data product object with units converted to reflectance

        .. py:method:: updateProductVariablesAttributes(...):

            Return updates variables attribute of processed *eopy.product.productIO.Product.Product* product attribute.

        .. py:method:: updateCommonAttributes(...):

            Returns updated ``attributes`` attribute of OLCI L1 *eopy.product.productIO.Product.Product* product with
            units converted to for common snappy product attributes

        .. py:method:: updateSpecificAttributes(...):

            Returns updated ``attributes`` attribute of OLCI L1 *eopy.product.productIO.Product.Product* product with
            units converted to for specific OLCI L1 product attributes

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
        Returns input *eopy.product.productIO.Product.Product* OLCI L1 data object in units of reflectance

        :type product: eopy.product.productIO.Product.Product
        :param product: Data product to process

        :return:
            :product_processed: *eopy.product.productIO.Product.Product*

            Processed data product
        """

        # Initialise subset empty subset product
        product_processed = Product()
        product_processed.dataReader = product.dataReader
        product_processed.product = [{}] * len(product.product)

        ################################################################################################################
        # 1. Update product attribute
        ################################################################################################################

        # Loop through products in product attribute and update dictionary entries
        # (should be just one for OLCI products)
        for i, p in enumerate(product.product):

            # Convert units to reflectance
            product_processed.product[i]["product_name"] = self.updateProductName(p["product_name"])
            product_processed.product[i]["product"] = self.convertProduct(p["product"])
            product_processed.product[i]["variables"] = self.updateProductVariablesAttributes(p["variables"])

        ################################################################################################################
        # 2. Update attributes attributes and variables
        ################################################################################################################

        product_processed.variables = self.updateVariables(product_processed, product)

        # Update common snappy product attributes
        product_processed.attributes = self.updateCommonAttributes(product_processed, product)

        # Update processing log
        product_processed.attributes = self.updateAttributesProcessingLog(product_processed, "rad2refl", {})

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

    def convertProduct(self, product, sensor="OLCI"):
        """
        Return OLCI *snappy.Product* data product object with units converted to reflectance

        :type product: *snappy.Product*
        :param product: In-memory OLCI L1 data product

        :param type: str
        :param sensor: name of product sensor (default "OLCI")

        :return:
            :product_processed: *snappy.Product*

            In-memory OLCI L1 data product with units converted to reflectance
        """

        HashMap = jpy.get_type('java.util.HashMap')
        params = HashMap()
        params.put("sensor", sensor)
        params.put("conversionMode", "RAD_TO_REFL")
        params.put("copyNonSpectralBands", "true")

        product_processed = GPF.createProduct("Rad2Refl", params, product)

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

        # Start by initialising copy of original attributes
        new_product_variables_attrs = deepcopy(original_product_variables_attrs)

        # Replace radiance variable names to reflectance
        rad_var_name = re.compile(r"Oa.*_radiance.*")
        for i in range(len(new_product_variables_attrs)):
            if rad_var_name.match(new_product_variables_attrs[i]):
                new_product_variables_attrs[i] = new_product_variables_attrs[i].replace("radiance", "reflectance")

        return new_product_variables_attrs

    def updateCommonAttributes(self, product_processed, product):
        """
        Returns updated ``attributes`` attribute of OLCI L1 *eopy.product.productIO.Product.Product* product with units
        converted to for common snappy product attributes

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
        Returns updated ``attributes`` attribute of OLCI L1 *eopy.product.productIO.Product.Product* product with units
        converted to for specific OLCI L1 product attributes

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

        # Replace radiance variable names to reflectance
        rad_var_name = re.compile(r"Oa.*_radiance")
        for i in range(len(new_variables)):
            if rad_var_name.match(new_variables[i].name):

                # Copy radiance variables attributes
                new_variables[i].name = new_variables[i].name.replace("radiance", "reflectance")
                new_variables[i].units = ""

        return new_variables


if __name__ == "__main__":
    pass
 

