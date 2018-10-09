"""
Product class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname, abspath, exists

'''___Third-Party Modules___'''
from numpy import arange

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from test_reader_functions import *
from AbstractDataFactory import AbstractDataFactory
from Variable import Variable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "DD/MM/YYYY"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


# Constants
test_reader_directory = abspath(pjoin(dirname(dirname(__file__)), "test_reader"))
test_data_path = pjoin(dirname(__file__), "test_data", "test_file.nc")
test_variable_name = "data"
test_data = arange(16).reshape((4,4))
# ADF = AbstractDataFactory()
# test_variables = ADF.variables
# test_attributes = ADF.attributes


def return_test_variables():

    data_variable_dict = {"name": "data_variable_name",
                          "ndims": 2,
                          "shape": (1500, 1100),
                          "dtype": "float",
                          "vtype": "data",
                          "vclass": "default",
                          "units": "Wm-2"}

    mask_variable_dict = {"name": "mask_variable_name",
                          "ndims": 2,
                          "shape": (1500, 1100),
                          "dtype": "bool",
                          "vtype": "mask",
                          "vclass": "default",
                          "units": "-"}

    meteorological_variable_dict = {"name": "meteorological_variable_name",
                                    "ndims": 2,
                                    "shape": (1500, 1100),
                                    "dtype": "float",
                                    "vtype": "meteorological",
                                    "vclass": "default",
                                    "units": "Pa"}

    sensor_variable_dict = {"name": "sensor_variable_name",
                                    "ndims": 2,
                                    "shape": (1500, 1100),
                                    "dtype": "float",
                                    "vtype": "sensor",
                                    "vclass": "default",
                                    "units": "-"}

    info_variable_dict = {"name": "info_variable_name",
                                    "ndims": 2,
                                    "shape": (1500, 1100),
                                    "dtype": "float",
                                    "vtype": "info",
                                    "vclass": "default",
                                    "units": "-"}

    variables = [Variable(data_variable_dict), Variable(mask_variable_dict), Variable(meteorological_variable_dict),
                 Variable(sensor_variable_dict), Variable(info_variable_dict)]

    return variables


class TestProduct(unittest.TestCase):
    def test_openProduct(self):
        from Product import Product

        # Create test data and reader
        createTestReader_netCDF(test_reader_directory)
        writeTestData(test_data_path, test_data, test_variable_name)

        # Ensure test data reader generated
        self.assertTrue(exists(test_reader_directory), "Test reader missing")
        self.assertTrue(exists(test_data_path), "Test data missing")

        # Open test product
        testProduct = Product(test_data_path)

        # Test correct data found
        test_data_opened = testProduct.getData(test_variable_name)
        for row, test_row in zip(test_data, test_data_opened):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)

        # Assert varaibles default
        self.assertEqual(testProduct.variables, test_variables)

        # Test attributes found correct
        test_attributes_opened = testProduct.attributes
        for key in testProduct.attributes.keys():
            self.assertEqual(test_attributes[key], test_attributes_opened[key], key + "incorrect")

        # Close product
        testProduct.product.close()

        # Remove test data reader
        shutil.rmtree(test_reader_directory)
        shutil.rmtree(dirname(test_data_path))

    def test_getVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["data_variable_name", "mask_variable_name", "meteorological_variable_name",
                                          "sensor_variable_name", "info_variable_name"])

    def test_getDataVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getDataVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["data_variable_name"])

    def test_getMaskVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getMaskVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["mask_variable_name"])

    def test_getMeteorologicalVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getMeteorologicalVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["meteorological_variable_name"])

    def test_getSensorVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getSensorVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["sensor_variable_name"])

    def test_getInfoVariableNames(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        vars_list = prod.getInfoVariableNames()

        # Test output
        self.assertItemsEqual(vars_list, ["info_variable_name"])

    def test_getVariableInfo(self):

        from Product import Product

        # Initialise variables
        variables = return_test_variables()

        # Initialise test product object and give it variables
        prod = Product()
        prod.variables = variables

        # Run test code
        var_dict = prod.getVariableInfo("data_variable_name")

        # Test output
        expected_dict = variables[0].return_variable_dict()

        self.assertItemsEqual(var_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
