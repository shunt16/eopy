"""
Data factory for opening Sentinel-3/OLCI L2 Land data
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from OLCISharedFactory import OLCISharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/09/2018"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

DATA_VARIABLE_NAMES = ["IWV", "IWV_err", "LQSF", "OGVI", "OGVI_err", "OTCI", "OTCI_err", "OTCI_quality_flags",
                       "RC681", "RC681_err", "RC865", "RC865_err"]
MASK_VARIABLE_NAMES = ['LQSF_INVALID', 'LQSF_WATER', 'LQSF_LAND', 'LQSF_CLOUD', 'LQSF_CLOUD_AMBIGUOUS',
                       'LQSF_CLOUD_MARGIN', 'LQSF_SNOW_ICE', 'LQSF_INLAND_WATER', 'LQSF_TIDAL', 'LQSF_COSMETIC',
                       'LQSF_SUSPECT', 'LQSF_HISOLZEN', 'LQSF_SATURATED', 'LQSF_WV_FAIL', 'LQSF_OGVI_FAIL',
                       'LQSF_OTCI_FAIL', 'LQSF_LRAYFAIL', 'LQSF_OGVI_CLASS_BAD', 'LQSF_OGVI_CLASS_WS',
                       'LQSF_OGVI_CLASS_CSI', 'LQSF_OGVI_CLASS_BRIGHT', 'LQSF_OGVI_CLASS_INVAL_REC', 'LQSF_OTCI_BAD_IN',
                       'LQSF_OTCI_CLASS_ANG', 'LQSF_OTCI_CLASS_CLSN', 'OTCI_quality_flags_Soil_flag_1',
                       'OTCI_quality_flags_Soil_flag_2', 'OTCI_quality_flags_Angle_flag_1',
                       'OTCI_quality_flags_Angle_flag_2', 'OTCI_quality_flags_Radiometry_flag',
                       'OTCI_quality_flags_TCI_flag']
METEOROLOGICAL_VARIABLE_NAMES = ["horizontal_wind_vector_1", "horizontal_wind_vector_2", "humidity",
                                 "sea_level_pressure", "total_columnar_water_vapour", "total_ozone",
                                 "atmospheric_temperature_profile_pressure_level_1",
                                 "atmospheric_temperature_profile_pressure_level_2",
                                 "atmospheric_temperature_profile_pressure_level_3",
                                 "atmospheric_temperature_profile_pressure_level_4",
                                 "atmospheric_temperature_profile_pressure_level_5",
                                 "atmospheric_temperature_profile_pressure_level_6",
                                 "atmospheric_temperature_profile_pressure_level_7",
                                 "atmospheric_temperature_profile_pressure_level_8",
                                 "atmospheric_temperature_profile_pressure_level_9",
                                 "atmospheric_temperature_profile_pressure_level_10",
                                 "atmospheric_temperature_profile_pressure_level_11",
                                 "atmospheric_temperature_profile_pressure_level_12",
                                 "atmospheric_temperature_profile_pressure_level_13",
                                 "atmospheric_temperature_profile_pressure_level_14",
                                 "atmospheric_temperature_profile_pressure_level_15",
                                 "atmospheric_temperature_profile_pressure_level_16",
                                 "atmospheric_temperature_profile_pressure_level_17",
                                 "atmospheric_temperature_profile_pressure_level_18",
                                 "atmospheric_temperature_profile_pressure_level_19",
                                 "atmospheric_temperature_profile_pressure_level_20",
                                 "atmospheric_temperature_profile_pressure_level_21",
                                 "atmospheric_temperature_profile_pressure_level_22",
                                 "atmospheric_temperature_profile_pressure_level_23",
                                 "atmospheric_temperature_profile_pressure_level_24",
                                 "atmospheric_temperature_profile_pressure_level_25"]
SENSOR_VARIABLE_NAMES = ["detector_index", "FWHM_band_1", "FWHM_band_2", "FWHM_band_3", "FWHM_band_4", "FWHM_band_5",
                         "FWHM_band_6", "FWHM_band_7", "FWHM_band_8", "FWHM_band_9", "FWHM_band_10", "FWHM_band_11",
                         "FWHM_band_12", "FWHM_band_13", "FWHM_band_14", "FWHM_band_15", "FWHM_band_16", "FWHM_band_17",
                         "FWHM_band_18", "FWHM_band_19", "FWHM_band_20", "FWHM_band_21", "frame_offset",
                         "lambda0_band_1", "lambda0_band_2", "lambda0_band_3", "lambda0_band_4", "lambda0_band_5",
                         "lambda0_band_6", "lambda0_band_7", "lambda0_band_8", "lambda0_band_9", "lambda0_band_10",
                         "lambda0_band_11", "lambda0_band_12", "lambda0_band_13", "lambda0_band_14", "lambda0_band_15",
                         "lambda0_band_16", "lambda0_band_17", "lambda0_band_18", "lambda0_band_19", "lambda0_band_20",
                         "lambda0_band_21"]
INFO_VARIABLE_NAMES = ["altitude", "latitude", "longitude", "solar_flux_band_1", "solar_flux_band_2",
                       "solar_flux_band_3", "solar_flux_band_4", "solar_flux_band_5", "solar_flux_band_6",
                       "solar_flux_band_7", "solar_flux_band_8", "solar_flux_band_9", "solar_flux_band_10",
                       "solar_flux_band_11", "solar_flux_band_12", "solar_flux_band_13", "solar_flux_band_14",
                       "solar_flux_band_15", "solar_flux_band_16", "solar_flux_band_17", "solar_flux_band_18",
                       "solar_flux_band_19", "solar_flux_band_20", "solar_flux_band_21", "TP_latitude", "TP_longitude",
                       "OAA", "OZA", "SAA", "SZA"]


class OLCIL2LFactory(OLCISharedFactory):
    """
    OLCIL2LFactory is a sub-class of OLCISharedFactory for opening OLCI L2 Land products

    :Methods:
        .. py:method:: getDataVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: getMaskVariableNames(...):

            Returns list of product "mask" type variable names

        .. py:method:: getMeteorologicalVariableNames(...):

            Returns list of product "meteorological" type variable names

        .. py:method:: getSensorVariableNames(...):

            Returns list of product "sensor" type variable names

        .. py:method:: getInfoVariableNames(...):

            Returns list of product "data" type variable names

        :inherited from eopy.product.productIO.sentinel3_reader.OLCISharedFactory.OLCISharedFactory:
            .. py:method:: readAttributes(...):
                Return dictionary with product attributes. Used to assign attributes attribute.

            :inherited from eopy.product.productIO.snappy_shared.SnappySharedFactory.SnappySharedFactory:
                .. py:method:: openProduct(...):
                    Opens an in-memory representation of data product specified by product_path.

                .. py:method:: createDataVariable(...):

                    Returns "data" type `SpectralVariable` class objects, for given product variable

                .. py:method:: createMaskVariable(...):

                    Returns "mask" type `Variable` class objects, for given product variable

                .. py:method:: createMeteorologicalVariable(...):

                    Returns "meteorological" type `Variable` class objects, for given product variable

                .. py:method:: createSensorVariable(...):

                    Returns "sensor" type `Variable` class objects, for given product variable

                .. py:method:: createInfoVariable(...):

                    Returns "info" type `Variable` class objects, for given product variable

                .. py:method:: return_available_variables(...):

                    Return variables available in data product from expected list

                .. py:method:: getData(...):
                    Returns variable[s] of in-memory product as an xarray data structure.

                .. py:method:: getPixelValues(...):
                    Returns pixel values of variable of in-memory product as a numpy.ndarray

                .. py:method:: simplify_attrs(...):
                    Return a simplified form of input attributes dictionary suitable for netcdf file attributes

                :inherited from eopy.product.productIO.productIO.AbstractDataFactory.AbstractDataFactory:
                    .. py:method:: __init__(...):
                        Initialises attributes

                    .. py:method:: readVariables(...):

                        Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

                    .. py:method:: getDataVariables(...):

                        Returns list of product "data" type variables as ``Variable`` or `SpectralVariable` class
                        objects.

                    .. py:method:: editDataVariable(...):

                        Returns 'data' variable objects with attributes edited compared to default values obtained from
                        product

                    .. py:method:: getMaskVariables(...):

                        Returns list of product "mask" type variables as ``Variable`` class objects.

                    .. py:method:: editMaskVariable(...):

                        Returns 'mask' variable objects with attributes edited compared to default values obtained from
                        product

                    .. py:method:: getMeteorologicalVariables(...):

                        Returns list of product "meteorological" type variables as ``Variable`` class objects.

                    .. py:method:: editMeteorologicalVariable(...):

                        Returns 'meteorological' variable objects with attributes edited compared to default values
                        obtained from product

                    .. py:method:: getSensorVariables(...):

                        Returns list of product "sensor" type variables as ``Variable`` class objects.

                    .. py:method:: editSensorVariable(...):

                        Returns 'sensor' variable objects with attributes edited compared to default values obtained from
                        product

                    .. py:method:: getInfoVariables(...):

                        Returns list of product "info" type variables as ``Variable`` class objects.

                    .. py:method:: editInfoVariable(...):

                        Returns 'info' variable objects with attributes edited compared to default values obtained from
                        product
    """

    # Constants
    FACTORY_STRING = "OLCIL2LFactory"
    TYPE_STRING = "OL_2_LFR"

    def getDataVariableNames(self, product):
        """
        Returns list of product "data" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :data_variable_names: *list*

            List of product "data" type variable names
        """

        data_variable_names = self.return_available_variables(product, DATA_VARIABLE_NAMES)

        return data_variable_names

    def getMaskVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :mask_variable_names: *list*

            List of product "mask" type variable names
        """

        mask_variable_names = self.return_available_variables(product, MASK_VARIABLE_NAMES)

        return mask_variable_names

    def getMeteorologicalVariableNames(self, product):
        """
        Returns list of product "meteorological" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :meteorological_variable_names: *list*

            List of product "meteorological" type variable names
        """

        meteorological_variable_names = self.return_available_variables(product, METEOROLOGICAL_VARIABLE_NAMES)

        return meteorological_variable_names

    def getSensorVariableNames(self, product):
        """
        Returns list of product "sensor" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :sensor_variable_names: *list*

            List of product "sensor" type variable names
        """

        sensor_variable_names = self.return_available_variables(product, SENSOR_VARIABLE_NAMES)

        return sensor_variable_names

    def getInfoVariableNames(self, product):
        """
        Returns list of product "info" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :info_variable_names: *list*

            List of product "info" type variable names
        """

        info_variable_names = self.return_available_variables(product, INFO_VARIABLE_NAMES)

        return info_variable_names


if __name__ == "__main__":
    pass
