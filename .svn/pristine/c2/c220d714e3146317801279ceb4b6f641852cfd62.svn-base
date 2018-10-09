"""
Variable class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/07/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestSpectralVariable(unittest.TestCase):
    def test___init__(self):
        input_dict = {"name": "test_name",
                      "ndims": 2,
                      "shape": (5, 10),
                      "dtype": "int",
                      "vtype": "data",
                      "units": "m",
                      "wavelength": 650,
                      "bandwidth": 15,
                      "srf": None}

        var = SpectralVariable(input_dict)

        expected_dict = {"name": "test_name",
                         "ndims": 2,
                         "shape": (5, 10),
                         "dtype": "int",
                         "vtype": "data",
                         "vclass": "spectral",
                         "units": "m",
                         "wavelength": 650,
                         "bandwidth": 15,
                         "srf": None}

        for key in expected_dict.keys():
            self.assertEquals(getattr(var, key), expected_dict[key])

    def test_add_srf(self):
        # todo - write test for adding srf
        pass

if __name__ == "__main__":
    unittest.main()
