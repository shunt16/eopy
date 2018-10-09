"""
Test class for Sentinel3SubsetTool
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from test_OLCIL1_subset_data import roi, OLCIL1_subset_test_attributes

sentinel3_subset_directory = dirname(dirname(__file__))
sys.path.append(sentinel3_subset_directory)

subset_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(subset_directory)

dataIO_directory = pjoin(dirname(dirname(dirname(dirname(dirname(dirname(__file__)))))), "dataIO")
sys.path.append(dataIO_directory)

sys.path.append(pjoin(dataIO_directory, "sentinel3_reader", "tests"))
from test_OLCIL1_data import OLCIL1_test_path, OLCIL1_test_attributes, OLCIL1_type_string, OLCIL1_test_variables


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "21/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestSentinel3SubsetTool(unittest.TestCase):
    def test_Product_sentinel3_reader_OLCIL1_openProduct_getData_Oa01_radiance(self):
        from Subset import Subset
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
        # Subset product and test
        ################################################################################################################

        # Initialise subset operator
        S_Op = Subset()
        subsetProduct = S_Op.run(testProduct, roi=roi)

        # 1. Test product attribute
        # Get Data for Oa01 radiance subset
        Oa01_radiance_s = subsetProduct.getData('Oa01_radiance')

        # Assert specific pixel values
        self.assertAlmostEqual(round(float(Oa01_radiance_s.values[0, 0]), 5), 89.77336)
        self.assertAlmostEqual(round(float(Oa01_radiance_s.values[4, 4]), 5), 86.20306)

        # 2. Test variables attribute
        # Assert opened variables are the same as the original variables, should be unchanged in subset process
        for key in OLCIL1_test_variables:
            if type(OLCIL1_test_variables[key]) == list:
                self.assertItemsEqual(subsetProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)
            else:
                self.assertEqual(subsetProduct.variables[key], OLCIL1_test_variables[key], "Problem with %s" % key)

        # 3. Test attributes attribute
        # Assert opened attributes are the same as the true attributes
        for key in OLCIL1_subset_test_attributes.keys():
            if type(OLCIL1_subset_test_attributes[key]) == list:
                self.assertItemsEqual(subsetProduct.attributes[key], OLCIL1_subset_test_attributes[key],
                                      "Problem with %s" % key)
            elif type(OLCIL1_subset_test_attributes[key]) == float:
                self.assertAlmostEqual(subsetProduct.attributes[key], OLCIL1_subset_test_attributes[key]) #, "Problem with %s" % key)

            else:
                self.assertEqual(subsetProduct.attributes[key], OLCIL1_subset_test_attributes[key]) #, "Problem with %s" % key)

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
