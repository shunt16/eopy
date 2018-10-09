"""
SnappySharedFactory class test
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname, abspath, exists

'''___Third-Party Modules___'''
from numpy import arange, zeros
import snappy

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
sys.path.append(dirname(dirname(__file__)))
sys.path.append(dirname(dirname(dirname(__file__))))
from Variable import Variable
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "22/07/2018"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

# todo - get data from tiepointgrid
# todo - time
# todo - masks
# todo - SRF

w = 15
h = 10
band1_array = arange(w*h).reshape((w, h)) / 100.0
band2_array = (arange(w*h).reshape((w, h)) + 100.0) / 100.0


longitude_array = zeros((w, h))
for i in range(h):
    longitude_array[:, i] = i

latitude_array = zeros((w, h))
for i in range(w):
    latitude_array[-i-1, :] = i

def setup():
    from SnappySharedFactory import SnappySharedFactory
    factory = SnappySharedFactory()

    product = snappy.Product("product", "type", 15, 10)
    band1 = product.addBand("band1", "double")
    band1.ensureRasterData()
    band1.setPixels(0, 0, band1_array.shape[0], band1_array.shape[1], band1_array.flatten())
    band1.setSpectralWavelength(500.0)
    band1.setSpectralBandwidth(20.0)
    band1.setUnit("radiance")

    band2 = product.addBand("band2", "double")
    band2.setUnit("unit")
    band2.ensureRasterData()
    band2.setPixels(0, 0, band2_array.shape[0], band2_array.shape[1], band2_array.flatten())

    tiepointgrid1 = snappy.TiePointGrid("tiepointgrid1", w, h, 0, 0, 1, 1)
    tiepointgrid1.setUnit("Pa")
    product.addTiePointGrid(tiepointgrid1)

    longitude = product.addBand("longitude", "double")
    longitude.setUnit("degrees")
    longitude.ensureRasterData()
    longitude.setPixels(0, 0, longitude_array.shape[0], longitude_array.shape[1], longitude_array.flatten())

    latitude = product.addBand("latitude", "double")
    latitude.setUnit("degrees")
    latitude.ensureRasterData()
    latitude.setPixels(0, 0, latitude_array.shape[0], latitude_array.shape[1], latitude_array.flatten())

    band1_variable_dict = {'name': "band1",
                           'dtype': 'float',
                           'vtype': 'data',
                           'units': 'radiance',
                           'ndims': 2,
                           'shape': (15, 10),
                           'wavelength': 500.0,
                           'bandwidth': 20.0,
                           'srf': None}

    band2_variable_dict = {'name': "band2",
                           'dtype': 'float',
                           'vtype': 'data',
                           'units': 'unit',
                           'ndims': 2,
                           'shape': (15, 10)}

    tiepointgrid1_variable_dict = {'name': "tiepointgrid1",
                                   'dtype': 'float',
                                   'vtype': 'data',
                                   'units': 'Pa',
                                   'ndims': 2,
                                   'shape': (15, 10)}

    latitude_variable_dict = {'name': "latitude",
                              'dtype': 'float',
                              'vtype': 'info',
                              'units': 'degrees',
                              'ndims': 2,
                              'shape': (15, 10)}

    longitude_variable_dict = {'name': "longitude",
                               'dtype': 'float',
                               'vtype': 'info',
                               'units': 'degrees',
                               'ndims': 2,
                               'shape': (15, 10)}

    variables = [SpectralVariable(band1_variable_dict), Variable(band2_variable_dict),
                 Variable(tiepointgrid1_variable_dict),
                 Variable(latitude_variable_dict), Variable(longitude_variable_dict)]

    attributes = {"product_string": "type"}

    return factory, product, variables, attributes


class TestSnappySharedFactory(unittest.TestCase):
    def test_openProduct(self):
        self.assertEqual(True, True)

    def test_getVariableNames(self):
        factory, product, _, _ = setup()

        expected_variable_names = ["band1", "band2", "longitude", "latitude", "tiepointgrid1"]
        variable_names = factory.getVariableNames(product)

        self.assertItemsEqual(expected_variable_names, variable_names)

    def test_getVariableInfo_band1(self):
        factory, product, variables, _ = setup()

        variable_info = [v for v in variables if v.name == "band1"][0].return_variable_dict()
        test_variable_info = factory.getVariableInfo(variables, "band1")

        self.assertEqual(len(variable_info.keys()), len(test_variable_info.keys()))

        for key in test_variable_info.keys():
            self.assertEqual(variable_info[key], test_variable_info[key])

    def test_getVariableInfo_latitude(self):
        factory, product, variables, _ = setup()

        variable_info = [v for v in variables if v.name == "latitude"][0].return_variable_dict()
        test_variable_info = factory.getVariableInfo(variables, "latitude")

        self.assertEqual(len(variable_info.keys()), len(test_variable_info.keys()))

        for key in test_variable_info.keys():
            self.assertEqual(variable_info[key], test_variable_info[key])

    def test_createSpectralDataVariable(self):
        factory, product, variables, _ = setup()

        expected_data_variable = variables[0]
        data_variable = factory.createDataVariable(product, expected_data_variable.name)

        for key in expected_data_variable.__dict__.keys():
            self.assertEquals(getattr(expected_data_variable, key), getattr(data_variable, key))

    def test_createDataVariable(self):
        factory, product, variables, _ = setup()

        expected_data_variable = variables[1]
        data_variable = factory.createDataVariable(product, expected_data_variable.name)

        for key in expected_data_variable.__dict__.keys():
            self.assertEquals(getattr(expected_data_variable, key), getattr(data_variable, key))

    def test_getDataVariableNames(self):
        factory, product, _, _ = setup()

        expected_data_variable_names = ["band1", "band2", "tiepointgrid1"]
        data_variable_names = factory.getDataVariableNames(product)

        self.assertEqual(expected_data_variable_names, data_variable_names)

    def test_createMaskVariable(self):
        factory, product, _, _ = setup()
        mask_variable_dict = {'name': 'band2',
                              'dtype': 'float',
                              'vtype': 'mask',
                              'units': None,
                              'ndims': 2,
                              'shape': (15, 10)}

        expected_mask_variable = Variable(mask_variable_dict)
        mask_variable = factory.createMaskVariable(product, mask_variable_dict['name'])

        for key in expected_mask_variable.__dict__.keys():
            self.assertEquals(getattr(expected_mask_variable, key), getattr(mask_variable, key))

    def test_getMaskVariableNames(self):
        factory, product, _, _ = setup()
        self.assertItemsEqual(factory.getMaskVariableNames(product), [])

    def test_createMeteorologicalVariable(self):
        factory, product, _, _ = setup()
        meteorological_variable_dict = {'name': 'band2',
                                        'dtype': 'float',
                                        'vtype': 'meteorological',
                                        'units': 'unit',
                                        'ndims': 2,
                                        'shape': (15, 10)}

        expected_meteorological_variable = Variable(meteorological_variable_dict)
        meteorological_variable = factory.createMeteorologicalVariable(product, meteorological_variable_dict['name'])

        for key in expected_meteorological_variable.__dict__.keys():
            self.assertEquals(getattr(expected_meteorological_variable, key), getattr(meteorological_variable, key))

    def test_getMeteorologicalVariableNames(self):
        factory, product, _, _ = setup()
        self.assertItemsEqual(factory.getMeteorologicalVariableNames(product), [])

    def test_createSensorVariable(self):
        factory, product, _, _ = setup()
        sensor_variable_dict = {'name': 'band2',
                                'dtype': 'float',
                                'vtype': 'sensor',
                                'units': 'unit',
                                'ndims': 2,
                                'shape': (15, 10)}

        expected_sensor_variable = Variable(sensor_variable_dict)
        sensor_variable = factory.createSensorVariable(product, sensor_variable_dict['name'])

        for key in expected_sensor_variable.__dict__.keys():
            self.assertEquals(getattr(expected_sensor_variable, key), getattr(sensor_variable, key))

    def test_getSensorVariableNames(self):
        factory, product, _, _ = setup()
        self.assertItemsEqual(factory.getSensorVariableNames(product), [])

    def test_createInfoVariable(self):
        factory, product, _, _ = setup()
        info_variable_dict = {'name': 'band2',
                              'dtype': 'float',
                              'vtype': 'info',
                              'units': 'unit',
                              'ndims': 2,
                              'shape': (15, 10)}

        expected_info_variable = Variable(info_variable_dict)
        info_variable = factory.createInfoVariable(product, info_variable_dict['name'])

        for key in expected_info_variable.__dict__.keys():
            self.assertEquals(getattr(expected_info_variable, key), getattr(info_variable, key))

    def test_getInfoVariableNames(self):
        factory, product, _, _ = setup()
        self.assertItemsEqual(factory.getInfoVariableNames(product), ["longitude", "latitude"])

    def test_readVariables(self):
        factory, product, variables, _ = setup()
        test_variables = factory.readVariables(product)

        self.assertEqual(len(variables), len(test_variables))
        for variable in variables:
            test_variable = [t_v for t_v in test_variables if t_v.name == variable.name][0]
            for key in variable.__dict__.keys():
                self.assertEquals(getattr(variable, key), getattr(test_variable, key))
                
    def test_readAttributes(self):
        factory, product, variables, attributes = setup()
        test_attributes = factory.readAttributes(product)

        self.assertItemsEqual(attributes.keys(), test_attributes.keys())

        for key in attributes.keys():
            self.assertEquals(attributes[key], test_attributes[key])

    def test_getPixelValues_band1(self):
        factory, product, variables, attributes = setup()

        test_band1_array = factory.getPixelValues(product, variables, attributes, "band1")

        self.assertEqual(band1_array.shape, test_band1_array.shape)

        for row, test_row in zip(band1_array, test_band1_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getPixelValues_band2(self):
        factory, product, variables, attributes = setup()

        test_band2_array = factory.getPixelValues(product, variables, attributes, "band2")

        self.assertEqual(band2_array.shape, test_band2_array.shape)

        for row, test_row in zip(band2_array, test_band2_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getPixelValues_longitude(self):
        factory, product, variables, attributes = setup()

        test_longitude_array = factory.getPixelValues(product, variables, attributes, "longitude")

        self.assertEqual(longitude_array.shape, test_longitude_array.shape)

        for row, test_row in zip(longitude_array, test_longitude_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getPixelValues_latitiude(self):
        factory, product, variables, attributes = setup()

        test_latitude_array = factory.getPixelValues(product, variables, attributes, "latitude")

        self.assertEqual(latitude_array.shape, test_latitude_array.shape)

        for row, test_row in zip(latitude_array, test_latitude_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getData_band1(self):

        factory, product, variables, attributes = setup()

        test_data = factory.getData(product, variables, attributes, "band1")

        # test attrs
        expected_attrs = factory.simplify_attr(factory.getVariableInfo(variables, "band1"))
        self.assertEqual(len(expected_attrs.keys()), len(test_data.attrs.keys()))
        for key in expected_attrs.keys():
            self.assertEqual(expected_attrs[key], test_data.attrs[key])

        # test data
        test_band1_array = test_data.values
        self.assertEqual(band1_array.shape, test_band1_array.shape)

        for row, test_row in zip(band1_array, test_band1_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getData_band1_band2(self):

        factory, product, variables, attributes = setup()

        test_data = factory.getData(product, variables, attributes, "band1", "band2")
        self.assertItemsEqual(test_data.variables.keys(), ["band1", "band2"])

        # Test band1

        test_data_band1 = test_data.variables['band1']

        # test attrs
        expected_attrs_band1 = factory.simplify_attr(factory.getVariableInfo(variables, "band1"))
        self.assertEqual(len(expected_attrs_band1.keys()), len(test_data_band1.attrs.keys()))
        for key in expected_attrs_band1.keys():
            self.assertEqual(expected_attrs_band1[key], test_data_band1.attrs[key])

        # test data
        test_band1_array = test_data_band1.values
        self.assertEqual(band1_array.shape, test_band1_array.shape)

        for row, test_row in zip(band1_array, test_band1_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

        # Test band2

        test_data_band2 = test_data.variables['band2']

        # test attrs
        expected_attrs_band2 = factory.simplify_attr(factory.getVariableInfo(variables, "band2"))
        self.assertEqual(len(expected_attrs_band2.keys()), len(test_data_band2.attrs.keys()))
        for key in expected_attrs_band2.keys():
            self.assertEqual(expected_attrs_band2[key], test_data_band2.attrs[key])

        # test data
        test_band2_array = test_data_band2.values
        self.assertEqual(band2_array.shape, test_band2_array.shape)

        for row, test_row in zip(band2_array, test_band2_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

    def test_getData_band1_longitude_latitude(self):

        factory, product, variables, attributes = setup()

        test_data = factory.getData(product, variables, attributes, "band1", "longitude", "latitude")

        # a. Test variables

        # Test expected variables present
        self.assertItemsEqual(test_data.variables.keys(), ["band1", "lon", "lat"])

        # i. Test band1
        test_data_band1 = test_data.variables['band1']

        # test attrs
        expected_attrs_band1 = factory.simplify_attr(factory.getVariableInfo(variables, "band1"))
        self.assertEqual(len(expected_attrs_band1.keys()), len(test_data_band1.attrs.keys()))
        for key in expected_attrs_band1.keys():
            self.assertEqual(expected_attrs_band1[key], test_data_band1.attrs[key])

        # test data
        test_band1_array = test_data_band1.values
        self.assertEqual(band1_array.shape, test_band1_array.shape)

        for row, test_row in zip(band1_array, test_band1_array):
            for elem, test_elem in zip(row, test_row):
                self.assertAlmostEquals(elem, test_elem, places=3)

        # b. Test Coords
        self.assertItemsEqual(test_data.coords.keys(), ["lon", "lat"])

        # i. test longitude

        test_data_longitude = test_data.coords['lon']

        # test attrs
        expected_attrs_longitude = factory.simplify_attr(factory.getVariableInfo(variables, "longitude"))
        self.assertEqual(len(expected_attrs_longitude.keys()), len(test_data_longitude.attrs.keys()))
        for key in expected_attrs_longitude.keys():
            self.assertEqual(expected_attrs_longitude[key], test_data_longitude.attrs[key])

        # test data
        test_longitude_array = test_data_longitude.values
        self.assertEqual(longitude_array.shape, test_longitude_array.shape)

        for row, test_row in zip(longitude_array, test_longitude_array):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)

        # ii. test latitude

        test_data_latitude = test_data.coords['lat']

        # test attrs
        expected_attrs_latitude = factory.simplify_attr(factory.getVariableInfo(variables, "latitude"))
        self.assertEqual(len(expected_attrs_latitude.keys()), len(test_data_latitude.attrs.keys()))
        for key in expected_attrs_latitude.keys():
            self.assertEqual(expected_attrs_latitude[key], test_data_latitude.attrs[key])

        # test data
        test_latitude_array = test_data_latitude.values
        self.assertEqual(latitude_array.shape, test_latitude_array.shape)

        for row, test_row in zip(latitude_array, test_latitude_array):
            for elem, test_elem in zip(row, test_row):
                self.assertEqual(elem, test_elem)


if __name__ == "__main__":
    unittest.main()
