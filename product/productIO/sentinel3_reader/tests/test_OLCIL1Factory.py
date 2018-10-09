"""
Tests for OLCIL1Factory class
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

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "02/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestOLCIL1Factory(unittest.TestCase):
    def test_openProduct(self):
        from OLCIL1Factory import OLCIL1Factory

        # Open product with OLCIL1Factory
        factory = OLCIL1Factory()
        product, variables, attributes = factory.openProduct(OLCIL1_test_path)

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
                self.assertAlmostEqual(attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

    def test_getData_valid_variables(self):
        from OLCIL1Factory import OLCIL1Factory

        # Open product with OLCIL1Factory
        factory = OLCIL1Factory()
        product, variables, attributes = factory.openProduct(OLCIL1_test_path)

        # for variable in attributes['variables'].keys():
        #     self.assertNotEqual(factory.getData(product, attributes, variable), None)

        with self.assertRaises(RuntimeError):
            factory.getData(product, variables, attributes, "anything")

    def test_getData_radiance_variable(self):
        from OLCIL1Factory import OLCIL1Factory

        # Open product with OLCIL1Factory
        factory = OLCIL1Factory()
        product, variables, attributes = factory.openProduct(OLCIL1_test_path)

        # Get Data
        data = factory.getData(product, variables, attributes, "Oa01_radiance")

        # Assert not None or 0
        self.assertEqual(str(type(data)), "<class 'xarray.core.dataarray.DataArray'>")

        # Assert attributes equal to variable attributes
        OLCIL1_test_var_simple = factory.simplify_attr(OLCIL1_test_variables['Oa01_radiance'])
        for key in OLCIL1_test_var_simple.keys():
            self.assertEqual(data.attrs[key], OLCIL1_test_var_simple[key], "Problem with %s" % key)

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(data.values[0,126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(data.values[342, 567]), 5), 94.15255)

        # Assert no coordinates
        self.assertTrue(data.coords == {})

    def test_Product_sentinel3_reader_OLCIL1_openProduct_getData_Oa01_radiance_long_lat(self):
        from OLCIL1Factory import OLCIL1Factory

        # Open product with OLCIL1Factory
        factory = OLCIL1Factory()
        product, variables, attributes = factory.openProduct(OLCIL1_test_path)

        # Get Data
        data = factory.getData(product, variables, attributes, "Oa01_radiance", "longitude", "latitude")

        # Assert attributes equal to test attributes
        OLCIL1_test_attributes_simple = factory.simplify_attr(OLCIL1_test_attributes)
        for key in OLCIL1_test_attributes_simple.keys():
            self.assertEqual(data.attrs[key], OLCIL1_test_attributes_simple[key], "Problem with %s" % key)

        # Assert Oa01_variables attributes equal to test variable attributes
        OLCIL1_test_var_simple = factory.simplify_attr(OLCIL1_test_variables['Oa01_radiance'])
        for key in OLCIL1_test_var_simple.keys():
            self.assertEqual(data.Oa01_radiance.attrs[key], OLCIL1_test_var_simple[key], "Problem with %s" % key)

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(data.Oa01_radiance.values[0, 126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(data.Oa01_radiance.values[342, 567]), 5), 94.15255)

        # Assert no coordinates
        self.assertItemsEqual(data.coords.keys(), ['longitude', 'latitude'])


if __name__ == "__main__":
    unittest.main()
