"""
SLSTRL1Factory class tests
"""

'''___Built-In Modules___'''
import unittest
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''
import snappy

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from test_SLSTRL1_data import SLSTRL1_test_path, SLSTRL1_test_attributes, SLSTRL1_type_string, SLSTRL1_display_name_500m, SLSTRL1_display_name_1km, expected_mask_variable_names_500m, expected_mask_variable_names_1km

sys.path.append(dirname(dirname(__file__)))
sys.path.append(dirname(dirname(dirname(__file__))))
from Variable import Variable
from SpectralVariable import SpectralVariable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "18/06/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

def setup_500m():
    from SLSTRL1Factory import SLSTRL1Factory
    reader_500m = snappy.ProductIO.getProductReader('Sen3_SLSTRL1B_500m')
    product = reader_500m.readProductNodes(SLSTRL1_test_path, None)
    factory = SLSTRL1Factory()
    return factory, product


def setup_1km():
    from SLSTRL1Factory import SLSTRL1Factory
    product = snappy.ProductIO.readProduct(SLSTRL1_test_path)
    factory = SLSTRL1Factory()
    return factory, product


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


class TestSlSTRL1Factory(unittest.TestCase):
    # def test_openProduct(self):
    #     from SLSTRL1Factory import SLSTRL1Factory
    #
    #     # Open product with OLCIL1Factory
    #     factory = SLSTRL1Factory()
    #     product, variables, attributes = factory.openProduct(SLSTRL1_test_path)
    #
    #     # Assert product an SLSTR L1 data product
    #     self.assertEqual(product[0].getDisplayName(), SLSTRL1_display_name_500m, "product[0] not an SLSTR L1 500m Product")
    #     self.assertEqual(product[1].getDisplayName(), SLSTRL1_display_name_1km, "product[1] not an SLSTR L1 1km Product")
    #
    #     # Assert opened variables are the same as the variables retrieved by variables method
    #     expected_variables = factory.readVariables(product[1])
    #     for key in expected_variables:
    #         if type(SLSTRL1_test_variables[key]) == list:
    #             self.assertItemsEqual(variables[key], expected_variables[key], "Problem with %s" % key)
    #         else:
    #             self.assertEqual(variables[key], expected_variables[key], "Problem with %s" % key)
    #
    #     # Assert opened attributes are the same as the true attributes
    #     expected_attributes = factory.readAttributes(product[1])
    #     for key in expected_attributes.keys():
    #         if type(expected_attributes[key]) == list:
    #             self.assertItemsEqual(attributes[key], expected_attributes[key], "Problem with %s" % key)
    #         else:
    #             self.assertAlmostEqual(attributes[key], expected_attributes[key], "Problem with %s" % key)

    def test_readAttributes(self):
        factory, product = setup_1km()
        attributes = factory.readAttributes(product)
        # Assert opened attributes are the same as the true attributes
        for key in SLSTRL1_test_attributes.keys():
            if type(SLSTRL1_test_attributes[key]) == list:
                self.assertItemsEqual(attributes[key], SLSTRL1_test_attributes[key], "Problem with %s" % key)
            else:
                self.assertAlmostEqual(attributes[key], SLSTRL1_test_attributes[key], "Problem with %s" % key)

    def test_getDataVariableNames_1km(self):
        factory, product = setup_1km()

        expected_data_variable_names = ['F1_BT_in', 'F1_BT_io', 'F2_BT_in', 'F2_BT_io', 'S7_BT_in',
                                        'S7_BT_io', 'S8_BT_in', 'S8_BT_io', 'S9_BT_in', 'S9_BT_io']

        data_variable_names = factory.getDataVariableNames(product)

        self.assertItemsEqual(expected_data_variable_names, data_variable_names)

    def test_getDataVariableNames_500m(self):

        factory, product = setup_500m()

        expected_data_variable_names = ['S1_radiance_an', 'S1_radiance_ao', 'S2_radiance_an', 'S2_radiance_ao',
                                        'S3_radiance_an', 'S3_radiance_ao', 'S4_radiance_an', 'S4_radiance_ao',
                                        'S4_radiance_bn', 'S4_radiance_bo', 'S4_radiance_cn', 'S4_radiance_co',
                                        'S5_radiance_an', 'S5_radiance_ao', 'S5_radiance_bn', 'S5_radiance_bo',
                                        'S5_radiance_cn', 'S5_radiance_co', 'S6_radiance_an', 'S6_radiance_ao',
                                        'S6_radiance_bn', 'S6_radiance_bo', 'S6_radiance_cn', 'S6_radiance_co',
                                        'F1_BT_in', 'F1_BT_io', 'F2_BT_in', 'F2_BT_io',
                                        'S7_BT_in', 'S7_BT_io', 'S8_BT_in',
                                        'S8_BT_io', 'S9_BT_in', 'S9_BT_io']
        data_variable_names = factory.getDataVariableNames(product)

        self.assertItemsEqual(expected_data_variable_names, data_variable_names)

    def test_editDataVariable_500m_radiance(self):
        factory, product = setup_500m()
        data_variable = createDataVariable("S3_radiance_an")

        expected_data_variable_edited = createDataVariable("S3_radiance_an")
        data_variable_edited = factory.editDataVariable(product, data_variable)

        for key in expected_data_variable_edited.__dict__.keys():
            self.assertEquals(getattr(data_variable_edited, key), getattr(expected_data_variable_edited, key))

    def test_editDataVariable_500m_BT(self):
        factory, product = setup_500m()
        data_variable = createDataVariable("S8_BT_io")

        expected_data_variable_edited = createDataVariable("S8_BT_io_500m")
        data_variable_edited = factory.editDataVariable(product, data_variable)

        for key in expected_data_variable_edited.__dict__.keys():
            self.assertEquals(getattr(data_variable_edited, key), getattr(expected_data_variable_edited, key))

    def test_editDataVariable_1km_BT(self):
        factory, product = setup_1km()
        data_variable = createDataVariable("S8_BT_io")

        expected_data_variable_edited = createDataVariable("S8_BT_io")
        data_variable_edited = factory.editDataVariable(product, data_variable)

        for key in expected_data_variable_edited.__dict__.keys():
            self.assertEquals(getattr(data_variable_edited, key), getattr(expected_data_variable_edited, key))

    def test_getMaskVariableNames_1km(self):
        factory, product = setup_1km()

        mask_variable_names = factory.getMaskVariableNames(product)

        self.assertItemsEqual(expected_mask_variable_names_1km, mask_variable_names)

    def test_getMaskVariableNames_500m(self):

        factory, product = setup_500m()

        mask_variable_names = factory.getMaskVariableNames(product)

        self.assertItemsEqual(expected_mask_variable_names_500m, mask_variable_names)

    def test_editMaskVariable_500m(self):
        factory, product = setup_500m()
        mask_variable = createMaskVariable("mask")

        expected_mask_variable_edited = createMaskVariable("mask")
        mask_variable_edited = factory.editMaskVariable(product, mask_variable)

        for key in expected_mask_variable_edited.__dict__.keys():
            self.assertEquals(getattr(mask_variable_edited, key), getattr(expected_mask_variable_edited, key))

    def test_editMaskVariable_1km(self):
        factory, product = setup_500m()
        mask_variable = createMaskVariable("mask")

        expected_mask_variable_edited = createMaskVariable("mask")
        mask_variable_edited = factory.editMaskVariable(product, mask_variable)

        for key in expected_mask_variable_edited.__dict__.keys():
            self.assertEquals(getattr(mask_variable_edited, key), getattr(expected_mask_variable_edited, key))

    def test_getMeteorologicalVariableNames_1km(self):
        factory, product = setup_1km()

        expected_meteorological_variable_names = []

        meteorological_variable_names = factory.getMeteorologicalVariableNames(product)

        self.assertItemsEqual(expected_meteorological_variable_names, meteorological_variable_names)

    def test_getMeteorologicalVariableNames_500m(self):

        factory, product = setup_500m()

        expected_meteorological_variable_names = []
        meteorological_variable_names = factory.getMeteorologicalVariableNames(product)

        self.assertItemsEqual(expected_meteorological_variable_names, meteorological_variable_names)

    def test_editMeteorologicalVariable_500m(self):
        factory, product = setup_500m()
        meteorological_variable = createMeteorologicalVariable("meteorological")

        expected_meteorological_variable_edited = createMeteorologicalVariable("meteorological")
        meteorological_variable_edited = factory.editMeteorologicalVariable(product, meteorological_variable)

        for key in expected_meteorological_variable_edited.__dict__.keys():
            self.assertEquals(getattr(meteorological_variable_edited, key),
                              getattr(expected_meteorological_variable_edited, key))

    def test_editMeteorologicalVariable_1km(self):
        factory, product = setup_500m()
        meteorological_variable = createMeteorologicalVariable("meteorological")

        expected_meteorological_variable_edited = createMeteorologicalVariable("meteorological")
        meteorological_variable_edited = factory.editMeteorologicalVariable(product, meteorological_variable)

        for key in expected_meteorological_variable_edited.__dict__.keys():
            self.assertEquals(getattr(meteorological_variable_edited, key),
                              getattr(expected_meteorological_variable_edited, key))

    def test_getSensorVariableNames_1km(self):
        factory, product = setup_1km()

        expected_sensor_variable_names = ["detector_in", "detector_io", "scan_in", "scan_io", "pixel_io", "pixel_in"]

        sensor_variable_names = factory.getSensorVariableNames(product)

        self.assertItemsEqual(expected_sensor_variable_names, sensor_variable_names)

    def test_getSensorVariableNames_500m(self):

        factory, product = setup_500m()

        expected_sensor_variable_names = ['pixel_an', 'pixel_ao', 'pixel_bn', 'pixel_bo', 'pixel_cn', 'pixel_co',
                                          'pixel_in', 'pixel_io', 'detector_an', 'detector_ao', 'detector_bn',
                                          'detector_bo', 'detector_cn', 'detector_co', 'detector_in', 'detector_io',
                                          'scan_an', 'scan_ao', 'scan_bn', 'scan_bo', 'scan_cn', 'scan_co', 'scan_in',
                                          'scan_io']

        sensor_variable_names = factory.getSensorVariableNames(product)

        self.assertItemsEqual(expected_sensor_variable_names, sensor_variable_names)

    def test_editSensorVariable_500m(self):
        factory, product = setup_500m()
        sensor_variable = createSensorVariable("sensor")

        expected_sensor_variable_edited = createSensorVariable("sensor")
        sensor_variable_edited = factory.editMaskVariable(product, sensor_variable)

        for key in expected_sensor_variable_edited.__dict__.keys():
            self.assertEquals(getattr(sensor_variable_edited, key), getattr(expected_sensor_variable_edited, key))

    def test_editSensorVariable_1km(self):
        factory, product = setup_500m()
        sensor_variable = createSensorVariable("sensor")

        expected_sensor_variable_edited = createSensorVariable("sensor")
        sensor_variable_edited = factory.editSensorVariable(product, sensor_variable)

        for key in expected_sensor_variable_edited.__dict__.keys():
            self.assertEquals(getattr(sensor_variable_edited, key), getattr(expected_sensor_variable_edited, key))

    def test_getInfoVariableNames_1km(self):
        factory, product = setup_1km()

        expected_info_variable_names = []

        info_variable_names = factory.getInfoVariableNames(product)

        self.assertItemsEqual(expected_info_variable_names, info_variable_names)

    def test_getInfoVariableNames_500m(self):

        factory, product = setup_500m()

        expected_info_variable_names = []
        info_variable_names = factory.getInfoVariableNames(product)

        self.assertItemsEqual(expected_info_variable_names, info_variable_names)

    def test_editInfoVariable_500m(self):
        factory, product = setup_500m()
        info_variable = createInfoVariable("info")

        expected_info_variable_edited = createInfoVariable("info")
        info_variable_edited = factory.editInfoVariable(product, info_variable)

        for key in expected_info_variable_edited.__dict__.keys():
            self.assertEquals(getattr(info_variable_edited, key), getattr(expected_info_variable_edited, key))

    def test_editInfoVariable_1km(self):
        factory, product = setup_500m()
        info_variable = createMaskVariable("info")

        expected_info_variable_edited = createMaskVariable("info")
        info_variable_edited = factory.editInfoVariable(product, info_variable)

        for key in expected_info_variable_edited.__dict__.keys():
            self.assertEquals(getattr(info_variable_edited, key), getattr(expected_info_variable_edited, key))

    # def test_getData_valid_variables(self):
    #     from SLSTRL1Factory import SLSTRL1Factory
    #
    #     # Open product with OLCIL1Factory
    #     factory = SLSTRL1Factory()
    #     product, variables, attributes = factory.openProduct(SLSTRL1_test_path)
    #
    #     # for variable in attributes['variables'].keys():
    #     #     self.assertNotEqual(factory.getData(product, attributes, variable), None)
    #
    #     with self.assertRaises(RuntimeError):
    #         factory.getData(product, variables, attributes, "anything")
    #
    # def test_getData_radiance_variable(self):
    #     from SLSTRL1Factory import SLSTRL1Factory
    #
    #     # Open product with OLCIL1Factory
    #     factory = SLSTRL1Factory()
    #     product, variables, attributes = factory.openProduct(SLSTRL1_test_path)
    #
    #     # Get Data
    #     data = factory.getData(product, variables, attributes, "Oa01_radiance")
    #
    #     # Assert not None or 0
    #     self.assertEqual(str(type(data)), "<class 'xarray.core.dataarray.DataArray'>")
    #
    #     # Assert attributes equal to variable attributes
    #     for key in SLSTRL1_test_variables['Oa01_radiance'].keys():
    #         self.assertEqual(data.attrs[key], SLSTRL1_test_variables['Oa01_radiance'][key], "Problem with %s" % key)
    #
    #     # Assert specific pixel values
    #     self.assertAlmostEqual(round(float(data.values[0,126]), 5), 52.06213)
    #     self.assertAlmostEqual(round(float(data.values[342, 567]), 5), 94.15255)
    #
    #     # Assert no coordinates
    #     self.assertTrue(data.coords == {})
    #
    # def test_Product_sentinel3_reader_OLCIL1_openProduct_getData_Oa01_radiance_long_lat(self):
    #     from SLSTRL1Factory import SLSTRL1Factory
    #
    #     # Open product with OLCIL1Factory
    #     factory = OLCIL1Factory()
    #     product, variables, attributes = factory.openProduct(OLCIL1_test_path)
    #
    #     # Get Data
    #     data = factory.getData(product, variables, attributes, "Oa01_radiance", "longitude", "latitude")
    #
    #     # Assert attributes equal to test attributes
    #     for key in OLCIL1_test_attributes.keys():
    #         self.assertEqual(data.attrs[key], OLCIL1_test_attributes[key], "Problem with %s" % key)
    #
    #     # Assert Oa01_variables attributes equal to test variable attributes
    #     for key in OLCIL1_test_variables['Oa01_radiance'].keys():
    #         self.assertEqual(data.Oa01_radiance.attrs[key], OLCIL1_test_variables['Oa01_radiance'][key], "Problem with %s" % key)
    #
    #     # Assert specific pixel values
    #     self.assertAlmostEqual(round(float(data.Oa01_radiance.values[0, 126]), 5), 52.06213)
    #     self.assertAlmostEqual(round(float(data.Oa01_radiance.values[342, 567]), 5), 94.15255)
    #
    #     # Assert no coordinates
    #     self.assertItemsEqual(data.coords.keys(), ['longitude', 'latitude'])


if __name__ == "__main__":
    unittest.main()
