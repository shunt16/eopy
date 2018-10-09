"""
Test class for Subset
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import abspath, dirname, exists
from os.path import join as pjoin

'''___Third-Party Modules___'''
from numpy import arange

'''___NPL Modules___'''
from test_Processor_functions import *

sys.path.append(dirname(dirname(__file__)))

dataIO_directory = pjoin(dirname(dirname(dirname(__file__))), "dataIO")
sys.path.append(pjoin(dataIO_directory, "tests"))
from test_reader_functions import *

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


# Constants
test_processor_directory = abspath(pjoin(dirname(dirname(__file__)), "testProcessor"))
sys.path.append(test_processor_directory)

test_reader_directory = abspath(pjoin(dataIO_directory, "test_reader"))
test_data_path = pjoin(dirname(__file__), "test_data", "test_file.nc")
test_variable_name = "data"
test_data = arange(16).reshape((4, 4))

# Create test data and reader
createTestProcessor(test_processor_directory)
createTestReader_netCDF_with_product_string(test_reader_directory)
writeTestData(test_data_path, test_data, test_variable_name)


class TestProcessingTool(unittest.TestCase):
    def test_run(self):

        # Ensure test processing tool, data reader and data generated
        self.assertTrue(exists(test_processor_directory), "Test subset tool missing")
        self.assertTrue(exists(test_reader_directory), "Test data missing")
        self.assertTrue(exists(test_data_path), "Test data missing")

        # Import test processing tool and data reader
        from Product import Product
        from TestProcessor import TestProcessor

        # Open test product
        testProduct = Product(test_data_path)

        # Test correct data found
        test_data_opened = testProduct.getData(test_variable_name)
        for row, test_row in zip(test_data, test_data_opened):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)

        # Operate on product with processing tool
        p_op = TestProcessor()
        subsetProduct = p_op.run(testProduct)

        # Test data still the same as input
        test_data_subset = subsetProduct.getData(test_variable_name)
        for row, test_row in zip(test_data, test_data_subset):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)

        # Close product
        testProduct.product.close()

        # Remove test data reader
        shutil.rmtree(test_reader_directory)
        shutil.rmtree(dirname(test_data_path))
        shutil.rmtree(test_processor_directory)


if __name__ == "__main__":
    unittest.main()

