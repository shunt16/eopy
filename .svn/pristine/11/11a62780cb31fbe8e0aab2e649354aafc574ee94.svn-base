"""
Tests for ProductReader class
"""

'''___Built-In Modules___'''
import unittest
from os.path import abspath, exists
from os.path import join as pjoin

'''___Third-Party Modules___'''
from numpy import arange

'''___NPL Modules___'''
from test_reader_functions import *
sys.path.append(dirname(dirname(__file__)))
from AbstractDataFactory import AbstractDataFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "05/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


# Constants
test_reader_directory = abspath(pjoin(dirname(dirname(__file__)), "test_reader"))
test_data_path = pjoin(dirname(__file__), "test_data", "test_file.nc")
test_variable_name = "data"
test_data = arange(16).reshape((4,4))
ADF = AbstractDataFactory()
test_variables = ADF.variables
test_attributes = ADF.attributes

class TestProductDataReader(unittest.TestCase):
    def test_getDataReaderPaths(self):
        from ProductDataReader import ProductDataReader

        # Known productReaderPaths - Keep Updated!
        dataIO_directory = dirname(dirname(__file__))
        dataReadersPaths_expected = [pjoin(dataIO_directory, "sentinel3_reader", "Sentinel3DataReader.py")]

        # productReaderPaths determined by function
        testProductDataReader = ProductDataReader()
        dataReaderPaths = testProductDataReader.getDataReaderPaths()

        # Require known and determined paths lists equal
        self.assertItemsEqual(dataReaderPaths, dataReadersPaths_expected)

    def test_getDataReader_withDataFactory(self):
        from ProductDataReader import ProductDataReader

        for i in range(2):
            if i == 0:
                createTestReader_xarray(test_reader_directory)
            elif i == 1:
                createTestReader_netCDF(test_reader_directory)
            writeTestData(test_data_path, test_data, test_variable_name)

            # Ensure test data reader generated
            self.assertTrue(exists(test_reader_directory), "Test reader missing")
            self.assertTrue(exists(test_data_path), "Test data missing")

            # Check ProductDataReader can find ProductDataReader
            testProductDataReader = ProductDataReader()
            dataReader = testProductDataReader.setDataReader(test_data_path)

            # Test data reader found
            self.assertNotEqual(dataReader, None)

            # Test data factory found
            dR = dataReader(test_data_path)
            product, variables, attributes = dR.openProduct(test_data_path)
            data = dR.getData(product, variables, attributes, test_variable_name)

            # Assert data opened test data
            for row, test_row in zip(data[:], test_data):
                for elem, test_elem in zip(row, test_row):
                    self.assertEqual(elem, test_elem)

            # Assert variables default
            self.assertEqual(variables, test_variables)

            # Assert attributes expected
            for key in attributes.keys():
                self.assertEqual(test_attributes[key], attributes[key], key + "incorrect")

            product.close()

            # Remove test data reader
            shutil.rmtree(test_reader_directory)
            shutil.rmtree(dirname(test_data_path))


if __name__ == "__main__":
    unittest.main()
