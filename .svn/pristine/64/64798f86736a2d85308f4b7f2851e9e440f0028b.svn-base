"""
Parse class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname, abspath, exists

'''___Third-Party Modules___'''


'''___NPL Modules___'''
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from test_parse_functions import *


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "DD/MM/YYYY"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestParse(unittest.TestCase):
    def test_Parse(self):
        from Parse import Parse

        # Create parser
        test_parser_directory = abspath(pjoin(dirname(dirname(__file__)), "tools", "test"))
        createTestParsingTool(test_parser_directory)

        # Ensure test data reader generated
        self.assertTrue(exists(test_parser_directory), "Test parser missing")

        # Parse test product
        testParse = Parse("")

        # Assert attributes expected
        self.assertEqual(testParse.attributes, {})

        # Remove test data parser
        shutil.rmtree(test_parser_directory)


if __name__ == "__main__":
    unittest.main()
