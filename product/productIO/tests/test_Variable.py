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
from Variable import Variable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/07/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class TestVariable(unittest.TestCase):
    def test___init__(self):
        input_dict = {"name": "test_name",
                      "ndims": 2,
                      "shape": (5, 10),
                      "dtype": "int",
                      "vtype": "data",
                      "units": "m"}

        var = Variable(input_dict)

        expected_dict = {"name": "test_name",
                         "ndims": 2,
                         "shape": (5, 10),
                         "dtype": "int",
                         "vtype": "data",
                         "vclass": "default",
                         "units": "m"}

        for key in expected_dict.keys():
            self.assertEquals(getattr(var, key), expected_dict[key])

    def test_return_variable_dict(self):
        var = Variable()

        var.name = "test_name"
        var.ndims = 2
        var.shape = (5, 10)
        var.dtype = "int"
        var.vtype = "data"
        var.units = "m"

        expected_dict = {"name": "test_name",
                         "ndims": 2,
                         "shape": (5, 10),
                         "dtype": "int",
                         "vtype": "data",
                         "vclass": "default",
                         "units": "m"}

        output_dict = var.return_variable_dict()

        self.assertDictEqual(output_dict, expected_dict)

    def test___repr__(self):
        var = Variable()
        var.name = "test_name"

        expected_repr = 'eopy.product.productIO.Variable.Variable "test_name"'

        output_repr = var.__repr__()

        self.assertEqual(output_repr, expected_repr)

if __name__ == "__main__":
    unittest.main()
