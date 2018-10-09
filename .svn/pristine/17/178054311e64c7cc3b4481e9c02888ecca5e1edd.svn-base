"""
Tests for Sentinel3DataReader class
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from test_OLCIL1_data import OLCIL1_test_path, OLCIL1_test_attributes, OLCIL1_type_string, OLCIL1_test_variables

sys.path.append(dirname(dirname(__file__)))
sys.path.append(dirname(dirname(dirname(__file__))))


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

# Example product paths
test_paths = {"OLCIL1": pjoin("S3A_OL_1_EFR____20161023T100950_20161023T101250_20161023T120602_0179_010_122_1979_SVL_O_NR_002.SEN3", "xfdumanifest.xml")}


class TestSentinel3DataReader(unittest.TestCase):

    def test_Sentinel3DataReader_setDataFactory(self):
        from Sentinel3DataReader import Sentinel3DataReader

        for prod_type in test_paths.keys():
            dataReader = Sentinel3DataReader()
            dataFactory = dataReader.setDataFactory(test_paths[prod_type])

            # Test data reader found
            self.assertNotEqual(dataFactory, None, "Failed for "+prod_type)

    def test_ProductDataReader_setDataReader_sentinel3_reader(self):
        from ProductDataReader import ProductDataReader

        for prod_type in test_paths.keys():
            # Check ProductDataReader can find ProductDataReader
            testProductDataReader = ProductDataReader()
            dataReader = testProductDataReader.setDataReader(test_paths[prod_type])

            # Test data reader found
            self.assertNotEqual(dataReader, None, "Failed for "+prod_type)

    def test_ProductDataReader_setDataReader_sentinel3_reader_OLCIL1Factory_openProduct(self):
        from ProductDataReader import ProductDataReader

        # Use ProductDataReader to find ProductDataReader with OLCIL1Factory
        testProductDataReader = ProductDataReader()
        dataReader = testProductDataReader.setDataReader(OLCIL1_test_path)

        # Assert suitable data reader found
        self.assertNotEqual(dataReader, None, "Data reader not found")

        # Use reader to open OLCI L1 product
        dR = dataReader(OLCIL1_test_path)
        product, variables, attributes = dR.openProduct(OLCIL1_test_path)

        # Assert product an OLCI L1 data product
        self.assertEqual(product.getProductType(), OLCIL1_type_string, "Product not an OLCI L1 Product")

        # Assert opened variables are the same as the true variables
        for key in OLCIL1_test_variables:
            if type(OLCIL1_test_variables[key]) == list:
                self.assertItemsEqual(variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)

        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_test_attributes.keys():
            if type(OLCIL1_test_attributes[key]) == list:
                self.assertItemsEqual(attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertEqual(attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

    def test_Product_sentinel3_reader_OLCIL1_openProduct(self):
        from Product import Product

        # Open test product
        testProduct = Product(OLCIL1_test_path)
        product = testProduct.product
        variables = testProduct.variables
        attributes = testProduct.attributes

        # Assert product an OLCI L1 data product
        self.assertEqual(product.getProductType(), OLCIL1_type_string, "Product not an OLCI L1 Product")

        # Assert opened variables are the same as the true variables
        for key in OLCIL1_test_variables:
            if type(OLCIL1_test_variables[key]) == list:
                self.assertItemsEqual(variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)

        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_test_attributes.keys():
            if type(OLCIL1_test_attributes[key]) == list:
                self.assertItemsEqual(attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertEqual(attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

    def test_Product_sentinel3_reader_OLCIL1_openProduct_getData_Oa01_radiance(self):
        from Product import Product

        # Open test product
        testProduct = Product(OLCIL1_test_path)

        # Get Data for Oa01 radiance
        Oa01_radiance = testProduct.getData('Oa01_radiance')

        # Assert attributes equal to variable attributes
        for key in OLCIL1_test_variables['Oa01_radiance'].keys():
            self.assertEqual(Oa01_radiance.attrs[key], OLCIL1_test_variables['Oa01_radiance'][key], "Problem with %s" % key)

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_radiance.values[0,126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(Oa01_radiance.values[342, 567]), 5), 94.15255)

        # Assert no coordinates
        self.assertTrue(Oa01_radiance.coords == {})

    def test_Product_sentinel3_reader_OLCIL1_openProduct_getData_Oa01_radiance_long_lat(self):
        from Product import Product

        # Open test product
        testProduct = Product(OLCIL1_test_path)

        # Get Data for Oa01 radiance
        Oa01_radiance = testProduct.getData('Oa01_radiance', 'longitude', 'latitude')

        # Assert attributes equal to test attributes
        for key in OLCIL1_test_attributes.keys():
            self.assertEqual(Oa01_radiance.attrs[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

        # Assert Oa01_variables attributes equal to test variable attributes
        for key in OLCIL1_test_variables['Oa01_radiance'].keys():
            self.assertEqual(Oa01_radiance.Oa01_radiance.attrs[key], OLCIL1_test_variables['Oa01_radiance'][key], "Problem with %s" % key)

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_radiance.Oa01_radiance.values[0, 126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(Oa01_radiance.Oa01_radiance.values[342, 567]), 5), 94.15255)

        # Assert no coordinates
        self.assertItemsEqual(Oa01_radiance.coords.keys(), ['longitude', 'latitude'])


if __name__ == "__main__":
    unittest.main()
