"""
Data factory for opening Sentinel-3/OLCI L2 Water data
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

DATA_VARIABLE_NAMES = ["Oa01_reflectance", "Oa01_reflectance_err", "Oa02_reflectance", "Oa02_reflectance_err",
                       "Oa03_reflectance", "Oa03_reflectance_err", "Oa04_reflectance", "Oa04_reflectance_err",
                       "Oa05_reflectance", "Oa05_reflectance_err", "Oa06_reflectance", "Oa06_reflectance_err",
                       "Oa07_reflectance", "Oa07_reflectance_err", "Oa08_reflectance", "Oa08_reflectance_err",
                       "Oa09_reflectance", "Oa09_reflectance_err", "Oa10_reflectance", "Oa10_reflectance_err",
                       "Oa11_reflectance", "Oa11_reflectance_err", "Oa12_reflectance", "Oa12_reflectance_err",
                       "Oa16_reflectance", "Oa16_reflectance_err", "Oa17_reflectance", "Oa17_reflectance_err",
                       "Oa18_reflectance", "Oa18_reflectance_err", "Oa21_reflectance", "Oa21_reflectance_err",
                       "CHL_OC4ME", "CHL_OC4ME_err", "CHL_NN", "CHL_NN_err", "TSM_NN", "TSM_NN_err", "KD490_M07",
                       "KD490_M07_err", "ADG443_NN", "ADG443_NN_err", "PAR", "PAR_err", "T865", "T865_err", "A865",
                       "A865_err", "IWV", "IWV_err", "WQSF_lsb", "WQSF_msb"]
MASK_VARIABLE_NAMES = ['WQSF_lsb_INVALID', 'WQSF_lsb_WATER', 'WQSF_lsb_LAND', 'WQSF_lsb_CLOUD', 'WQSF_lsb_SNOW_ICE',
                       'WQSF_lsb_INLAND_WATER', 'WQSF_lsb_TIDAL', 'WQSF_lsb_COSMETIC', 'WQSF_lsb_SUSPECT',
                       'WQSF_lsb_HISOLZEN', 'WQSF_lsb_SATURATED', 'WQSF_lsb_MEGLINT', 'WQSF_lsb_RISKGLINT',
                       'WQSF_lsb_WHITECAPS', 'WQSF_lsb_ADJAC', 'WQSF_lsb_WV_FAIL', 'WQSF_lsb_PAR_FAIL',
                       'WQSF_lsb_AC_FAIL', 'WQSF_lsb_OC4ME_FAIL', 'WQSF_lsb_OCNN_FAIL', 'WQSF_lsb_KDM_FAIL',
                       'WQSF_lsb_BPAC_ON', 'WQSF_lsb_WHITE_SCATT', 'WQSF_lsb_LOWRW', 'WQSF_lsb_HIGHRW',
                       'WQSF_msb_ANNOT_ANGSTROM', 'WQSF_msb_ANNOT_AERO_B', 'WQSF_msb_ANNOT_ABSO_D',
                       'WQSF_msb_ANNOT_ACLIM', 'WQSF_msb_ANNOT_ABSOA', 'WQSF_msb_ANNOT_MIXR1', 'WQSF_msb_ANNOT_DROUT',
                       'WQSF_msb_ANNOT_TAU06', 'WQSF_msb_RWNEG_O1', 'WQSF_msb_RWNEG_O2', 'WQSF_msb_RWNEG_O3',
                       'WQSF_msb_RWNEG_O4', 'WQSF_msb_RWNEG_O5', 'WQSF_msb_RWNEG_O6', 'WQSF_msb_RWNEG_O7',
                       'WQSF_msb_RWNEG_O8', 'WQSF_msb_RWNEG_O9', 'WQSF_msb_RWNEG_O10', 'WQSF_msb_RWNEG_O11',
                       'WQSF_msb_RWNEG_O12', 'WQSF_msb_RWNEG_O16', 'WQSF_msb_RWNEG_O17', 'WQSF_msb_RWNEG_O18',
                       'WQSF_msb_RWNEG_O21']
METEOROLOGICAL_VARIABLE_NAMES = ["horizontal_wind_vector_1", "horizontal_wind_vector_2", "sea_level_pressure",
                                 "total_ozone", "humidity", "total_columnar_water_vapour",
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
SENSOR_VARIABLE_NAMES = ["detector_index", "frame_offset", "lambda0_band_1", "lambda0_band_2", "lambda0_band_3",
                         "lambda0_band_4", "lambda0_band_5", "lambda0_band_6", "lambda0_band_7", "lambda0_band_8",
                         "lambda0_band_9", "lambda0_band_10", "lambda0_band_11", "lambda0_band_12", "lambda0_band_13",
                         "lambda0_band_14", "lambda0_band_15", "lambda0_band_16", "lambda0_band_17", "lambda0_band_18",
                         "lambda0_band_19", "lambda0_band_20", "lambda0_band_21", "FWHM_band_1", "FWHM_band_2",
                         "FWHM_band_3", "FWHM_band_4", "FWHM_band_5", "FWHM_band_6", "FWHM_band_7", "FWHM_band_8",
                         "FWHM_band_9", "FWHM_band_10", "FWHM_band_11", "FWHM_band_12", "FWHM_band_13", "FWHM_band_14",
                         "FWHM_band_15", "FWHM_band_16", "FWHM_band_17", "FWHM_band_18", "FWHM_band_19", "FWHM_band_20",
                         "FWHM_band_21"]
INFO_VARIABLE_NAMES = ["longitude", "latitude", "altitude", "solar_flux_band_1", "solar_flux_band_2",
                       "solar_flux_band_3", "solar_flux_band_4", "solar_flux_band_5", "solar_flux_band_6",
                       "solar_flux_band_7", "solar_flux_band_8", "solar_flux_band_9", "solar_flux_band_10",
                       "solar_flux_band_11", "solar_flux_band_12", "solar_flux_band_13", "solar_flux_band_14",
                       "solar_flux_band_15", "solar_flux_band_16", "solar_flux_band_17", "solar_flux_band_18",
                       "solar_flux_band_19", "solar_flux_band_20", "solar_flux_band_21", "TP_longitude", "TP_latitude",
                       "SZA", "SAA", "OZA", "OAA"]


class OLCIL2WFactory(OLCISharedFactory):
    """
    OLCIL2WFactory is a sub-class of OLCIL2WFactory for opening OLCI L2 Water products

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
    FACTORY_STRING = "OLCIL2WFactory"
    TYPE_STRING = "OL_2_WFR"

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
