"""
Test class for Sentinel3Radiance2ReflectanceTool
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from test_OLCIL1_radiance2reflectance_data import OLCIL1_test_reflectance_variables

sentinel3_radiance2reflectance_directory = dirname(dirname(__file__))
sys.path.append(sentinel3_radiance2reflectance_directory)

radiance2reflectance_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(radiance2reflectance_directory)

# get test data
dataIO_directory = pjoin(dirname(dirname(dirname(dirname(dirname(dirname(dirname(__file__))))))), "dataIO")
sys.path.append(dataIO_directory)
sys.path.append(pjoin(dataIO_directory, "sentinel3_reader", "tests"))
from test_OLCIL1_data import OLCIL1_test_path, OLCIL1_test_attributes, OLCIL1_type_string, OLCIL1_test_variables


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestSentinel3Radiance2ReflectancProcessor(unittest.TestCase):
    def test_run_OLCIL1_Oa01_radiance(self):
        from Radiance2Reflectance import Radiance2Reflectance
        from Product import Product

        ################################################################################################################
        # 1. Open input product and test
        ################################################################################################################

        # Open test product
        testProduct = Product(OLCIL1_test_path)

        # 1. Test product attribute
        # Get Data for Oa01 radiance
        Oa01_radiance = testProduct.getData('Oa01_radiance')

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_radiance.values[0, 126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(Oa01_radiance.values[342, 567]), 5), 94.15255)

        # 2. Test variables attribute
        # Assert opened variables are the same as the true variables
        for key in OLCIL1_test_variables:
            if type(OLCIL1_test_variables[key]) == list:
                self.assertItemsEqual(testProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(testProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)

        # 3. Test attributes attribute
        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_test_attributes.keys():
            if type(OLCIL1_test_attributes[key]) == list:
                self.assertItemsEqual(testProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertEqual(testProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

        ################################################################################################################
        # Convert units to radiance product and test
        ################################################################################################################

        # Initialise subset operator
        Rad2Refl_Op = Radiance2Reflectance()
        convertedProduct = Rad2Refl_Op.run(testProduct)

        # 1. Test product attribute
        # Get Data for Oa01 radiance subset
        Oa01_reflectance = convertedProduct.getData('Oa01_reflectance')

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_reflectance.values[0, 126]), 5), 0.49819)
        self.assertAlmostEqual(round(float(Oa01_reflectance.values[4, 130]), 5), 0.49898)

        # 2. Test variables attribute
        # Assert opened variables are the same as the original variables, should be unchanged in subset process
        for key in OLCIL1_test_reflectance_variables:
            if type(OLCIL1_test_reflectance_variables[key]) == list:
                self.assertItemsEqual(convertedProduct.variables[key], OLCIL1_test_reflectance_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(convertedProduct.variables[key], OLCIL1_test_reflectance_variables[key], "Problem with %s" % key)

        # 3. Test attributes attribute
        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_test_attributes.keys():
            if type(OLCIL1_test_attributes[key]) == list:
                self.assertItemsEqual(convertedProduct.attributes[key], OLCIL1_test_attributes[key],
                                      "Problem with %s" % key)
            elif type(OLCIL1_test_attributes[key]) == float:
                self.assertAlmostEqual(convertedProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

            else:
                self.assertEqual(convertedProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)

        ################################################################################################################
        # 3. Check input product unchanged
        ################################################################################################################

        # 1. Test product attribute
        # Get Data for Oa01 radiance
        Oa01_radiance = testProduct.getData('Oa01_radiance')

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_radiance.values[0, 126]), 5), 52.06213)
        self.assertAlmostEqual(round(float(Oa01_radiance.values[342, 567]), 5), 94.15255)

        # 2. Test variables attribute
        # Assert opened variables are the same as the true variables
        for key in OLCIL1_test_variables:
            if type(OLCIL1_test_variables[key]) == list:
                self.assertItemsEqual(testProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(testProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)

        # 3. Test attributes attribute
        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_test_attributes.keys():
            if type(OLCIL1_test_attributes[key]) == list:
                self.assertItemsEqual(testProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertEqual(testProduct.attributes[key], OLCIL1_test_attributes[key], "Problem with %s" % key)


if __name__ == "__main__":
    unittest.main()
