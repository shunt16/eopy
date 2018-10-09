"""
AbstractProductFactory class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname, abspath, exists

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
from Variable import Variable
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "21/07/2018"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


def setup():
    from AbstractDataFactory import AbstractDataFactory
    factory = AbstractDataFactory()
    return factory


def setup_edited():
    from AbstractDataFactory import AbstractDataFactory
    factory = AbstractDataFactory()

    def getDataVariableNames(product):
        return ['data_variable1', 'data_variable2']

    def getMaskVariableNames(product):
        return ['mask_variable1', 'mask_variable2']

    def getMeteorologicalVariableNames(product):
        return ['meteorological_variable1', 'meteorological_variable2']

    def getSensorVariableNames(product):
        return ['sensor_variable1', 'sensor_variable2']

    def getInfoVariableNames(product):
        return ['info_variable1', 'info_variable2']

    factory.getDataVariableNames = getDataVariableNames
    factory.getMaskVariableNames = getMaskVariableNames
    factory.getMeteorologicalVariableNames = getMeteorologicalVariableNames
    factory.getSensorVariableNames = getSensorVariableNames
    factory.getInfoVariableNames = getInfoVariableNames

    return factory


def createDataVariable(variable_name):
    data_variable_dict = {'name': variable_name,
                          'dtype': None,
                          'vtype': 'data',
                          'units': None,
                          'ndims': None,
                          'shape': None,
                          'wavelength': None,
                          'bandwidth': None,
                          'srf': None}

    data_variable = SpectralVariable(data_variable_dict)
    return data_variable


def createMaskVariable(variable_name):
    mask_variable_dict = {'name': variable_name,
                          'dtype': None,
                          'vtype': 'mask',
                          'units': None,
                          'ndims': None,
                          'shape': None}

    mask_variable = Variable(mask_variable_dict)
    return mask_variable


def createMeteorologicalVariable(variable_name):
    meteorological_variable_dict = {'name': variable_name,
                                    'dtype': None,
                                    'vtype': 'meteorological',
                                    'units': None,
                                    'ndims': None,
                                    'shape': None}

    meteorological_variable = Variable(meteorological_variable_dict)
    return meteorological_variable


def createSensorVariable(variable_name):
    sensor_variable_dict = {'name': variable_name,
                            'dtype': None,
                            'vtype': 'sensor',
                            'units': None,
                            'ndims': None,
                            'shape': None}

    sensor_variable = Variable(sensor_variable_dict)
    return sensor_variable


def createInfoVariable(variable_name):
    info_variable_dict = {'name': variable_name,
                          'dtype': None,
                          'vtype': 'info',
                          'units': None,
                          'ndims': None,
                          'shape': None}

    info_variable = Variable(info_variable_dict)
    return info_variable


class TestAbstractProductFactory(unittest.TestCase):
    def test_openProduct(self):
        factory = setup()
        product, variables, attributes = factory.openProduct(None)
        self.assertEqual(product, None)
        self.assertItemsEqual(variables, [])
        self.assertEqual(attributes, None)

    def test_readVariables(self):
        factory = setup_edited()

        expected_variables = factory.getDataVariables(None) + factory.getMaskVariables(None) \
                             + factory.getMeteorologicalVariables(None) + factory.getSensorVariables(None) \
                             + factory.getInfoVariables(None)
        variables = factory.readVariables(None)

        for v, e_v in zip(variables, expected_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_getDataVariables(self):
        factory = setup_edited()

        data_variables = factory.getDataVariables(None)
        expected_data_variables = [createDataVariable('data_variable1'), createDataVariable('data_variable2')]

        for v, e_v in zip(data_variables, expected_data_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_createDataVariable(self):
        factory = setup()

        expected_dict = {'name': 'test',
                         'dtype': None,
                         'vtype': 'data',
                         'vclass': 'spectral',
                         'units': None,
                         'ndims': None,
                         'shape': None,
                         'wavelength': None,
                         'bandwidth': None,
                         'srf': None}

        data_variable = factory.createDataVariable(None, expected_dict['name'])

        for key in expected_dict.keys():
            self.assertEquals(getattr(data_variable, key), expected_dict[key])

    def test_getDataVariableNames(self):
        factory = setup()
        expected_data_variable_names = []
        data_variable_names = factory.getDataVariableNames(None)
        self.assertEqual(expected_data_variable_names, data_variable_names)

    def test_editDataVariable(self):
        factory = setup()

        data_variable = createDataVariable('test')
        data_variable_edited = factory.editDataVariable(None, data_variable)

        for key in data_variable_edited.__dict__.keys():
            self.assertEquals(getattr(data_variable_edited, key), getattr(data_variable, key))

    def test_getMaskVariables(self):
        factory = setup_edited()

        mask_variables = factory.getMaskVariables(None)
        expected_mask_variables = [createMaskVariable('mask_variable1'), createMaskVariable('mask_variable2')]

        for v, e_v in zip(mask_variables, expected_mask_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_createMaskVariable(self):
        factory = setup()

        expected_dict = {'name': 'test',
                         'dtype': None,
                         'vtype': 'mask',
                         'vclass': 'default',
                         'units': None,
                         'ndims': None,
                         'shape': None}

        mask_variable = factory.createMaskVariable(None, expected_dict['name'])

        for key in expected_dict.keys():
            self.assertEquals(getattr(mask_variable, key), expected_dict[key])

    def test_getMaskVariableNames(self):
        factory = setup()
        expected_mask_variable_names = []
        mask_variable_names = factory.getMaskVariableNames(None)
        self.assertEqual(expected_mask_variable_names, mask_variable_names)

    def test_editMaskVariable(self):
        factory = setup()
        mask_variable = createMaskVariable("test")

        mask_variable_edited = factory.editMaskVariable(None, mask_variable)

        for key in mask_variable_edited.__dict__.keys():
            self.assertEquals(getattr(mask_variable_edited, key), getattr(mask_variable, key))

    def test_getMeteorologicalVariables(self):
        factory = setup_edited()

        meteorological_variables = factory.getMeteorologicalVariables(None)
        expected_meteorological_variables = [createMeteorologicalVariable('meteorological_variable1'),
                                             createMeteorologicalVariable('meteorological_variable2')]

        for v, e_v in zip(meteorological_variables, expected_meteorological_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_createMeteorologicalVariable(self):
        factory = setup()

        expected_dict = {'name': 'test',
                         'dtype': None,
                         'vtype': 'meteorological',
                         'vclass': 'default',
                         'units': None,
                         'ndims': None,
                         'shape': None}

        meteorological_variable = factory.createMeteorologicalVariable(None, expected_dict['name'])

        for key in expected_dict.keys():
            self.assertEquals(getattr(meteorological_variable, key), expected_dict[key])

    def test_getMeteorologicalVariableNames(self):
        factory = setup()
        expected_meteorological_variable_names = []
        meteorological_variable_names = factory.getMeteorologicalVariableNames(None)
        self.assertEqual(expected_meteorological_variable_names, meteorological_variable_names)

    def test_editMeteorologicalVariable(self):
        factory = setup()
        meteorological_variable = createMeteorologicalVariable("test")

        meteorological_variable_edited = factory.editMeteorologicalVariable(None, meteorological_variable)

        for key in meteorological_variable_edited.__dict__.keys():
            self.assertEquals(getattr(meteorological_variable_edited, key), getattr(meteorological_variable, key))

    def test_getSensorVariables(self):
        factory = setup_edited()

        sensor_variables = factory.getSensorVariables(None)
        expected_sensor_variables = [createSensorVariable('sensor_variable1'), createSensorVariable('sensor_variable2')]

        for v, e_v in zip(sensor_variables, expected_sensor_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_createSensorVariable(self):
        factory = setup()

        expected_dict = {'name': 'test',
                         'dtype': None,
                         'vtype': 'sensor',
                         'vclass': 'default',
                         'units': None,
                         'ndims': None,
                         'shape': None}

        sensor_variable = factory.createSensorVariable(None, expected_dict['name'])

        for key in expected_dict.keys():
            self.assertEquals(getattr(sensor_variable, key), expected_dict[key])

    def test_getSensorVariableNames(self):
        factory = setup()
        expected_sensor_variable_names = []
        sensor_variable_names = factory.getSensorVariableNames(None)
        self.assertEqual(expected_sensor_variable_names, sensor_variable_names)

    def test_editSensorVariable(self):
        factory = setup()
        sensor_variable = createSensorVariable("test")

        sensor_variable_edited = factory.editSensorVariable(None, sensor_variable)

        for key in sensor_variable_edited.__dict__.keys():
            self.assertEquals(getattr(sensor_variable_edited, key), getattr(sensor_variable, key))
        self.assertEqual(True, True)

    def test_getInfoVariables(self):
        factory = setup_edited()

        info_variables = factory.getInfoVariables(None)
        expected_info_variables = [createInfoVariable('info_variable1'), createInfoVariable('info_variable2')]

        for v, e_v in zip(info_variables, expected_info_variables):
            for key in v.__dict__.keys():
                self.assertEquals(getattr(v, key), getattr(e_v, key))

    def test_createInfoVariable(self):
        factory = setup()

        expected_dict = {'name': 'test',
                         'dtype': None,
                         'vtype': 'info',
                         'vclass': 'default',
                         'units': None,
                         'ndims': None,
                         'shape': None}

        info_variable = factory.createInfoVariable(None, expected_dict['name'])

        for key in expected_dict.keys():
            self.assertEquals(getattr(info_variable, key), expected_dict[key])

    def test_getInfoVariableNames(self):
        factory = setup()
        expected_info_variable_names = []
        info_variable_names = factory.getInfoVariableNames(None)
        self.assertEqual(expected_info_variable_names, info_variable_names)

    def test_editInfoVariable(self):
        factory = setup()
        info_variable = createInfoVariable("test")

        info_variable_edited = factory.editInfoVariable(None, info_variable)

        for key in info_variable_edited.__dict__.keys():
            self.assertEquals(getattr(info_variable_edited, key), getattr(info_variable, key))

    def test_readAttributes(self):
        factory = setup()
        attributes = factory.readAttributes(None)
        self.assertEqual(attributes, None)

    def test_getData(self):
        factory = setup()
        data = factory.getData(None, None, None, None)
        self.assertEqual(data, None)

if __name__ == "__main__":
    unittest.main()
