"""
 class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname, abspath, exists
from os.path import join as pjoin
import shutil

'''___Third-Party Modules___'''
from numpy import arange

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from product.productIO.AbstractDataFactory import AbstractDataFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "DD/MM/YYYY"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


# Constants
test_reader_directory = pjoin(abspath(dirname(dirname(__file__))), "main", "eopy", "product", "productIO", "test_reader")

test_data_path = pjoin("test_data", "test_file.nc")
test_variable_name = "data"
test_data = arange(16).reshape((4, 4))
ADF = AbstractDataFactory()
test_variables = ADF.variables
test_attributes = ADF.attributes


class TestEOPy(unittest.TestCase):
    def test_eopy_testfile(self):

        ################################################################################################################
        # 1. Prepare test files
        ################################################################################################################

        from product.productIO.tests.test_reader_functions import createTestReader_netCDF, writeTestData

        # Create test product and test data
        createTestReader_netCDF(test_reader_directory)
        writeTestData(test_data_path, test_data, test_variable_name)

        # Ensure test data reader generated
        self.assertTrue(exists(test_reader_directory), "Test reader missing")
        self.assertTrue(exists(test_data_path), "Test data missing")

        ################################################################################################################
        # 2. Run test script
        ################################################################################################################

        from product.productIO.Product import Product

        # Open test product
        testProduct = Product(test_data_path)
        test_data_opened = testProduct.getData(test_variable_name)

        # Assert correct data found
        for row, test_row in zip(test_data, test_data_opened):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)

        # Assert variables found correct
        self.assertEqual(testProduct.variables, test_variables)

        # Assert attributes found correct
        test_attributes_opened = testProduct.attributes
        for key in testProduct.attributes.keys():
            self.assertEqual(test_attributes[key], test_attributes_opened[key], key + " incorrect")

        # Close product
        testProduct.product.close()

        # Remove test data reader
        shutil.rmtree(test_reader_directory)
        shutil.rmtree(dirname(test_data_path))

if __name__ == "__main__":
    unittest.main()
