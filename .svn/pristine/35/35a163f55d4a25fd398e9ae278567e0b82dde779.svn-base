"""
Test class for Sentinel3ParseTool
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
dataParse_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(dataParse_directory)


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
        from test_RVUS_parse_data import RVUS_test_path, RVUS_test_attributes
        from Parse import Parse

        s3parse = Parse(RVUS_test_path)

        # Test attributes attribute
        # Assert opened attributes are the same as the true attributes
        for key in RVUS_test_attributes.keys():
            if type(RVUS_test_attributes[key]) == list:
                self.assertItemsEqual(s3parse.attributes[key], RVUS_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertEqual(s3parse.attributes[key], RVUS_test_attributes[key], "Problem with %s" % key)


if __name__ == "__main__":
    unittest.main()
