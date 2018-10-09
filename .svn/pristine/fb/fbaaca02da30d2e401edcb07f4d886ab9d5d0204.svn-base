"""
Data factory for opening Sentinel-2/MSI L2 products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from MSISharedFactory import MSISharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/09/2018"
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


DATA_VARIABLE_NAMES_10m = ['B2', 'B3', 'B4', 'B8']
DATA_VARIABLE_NAMES_20m = ['B5', 'B6', 'B7', 'B8A', 'B11', 'B12']
DATA_VARIABLE_NAMES_60m = ['B1', 'B9', 'B10']
MASK_VARIABLE_NAMES_10m = ["opaque_clouds_10m", "cirrus_clouds_10m", "detector_footprint-B02-01",
                           "detector_footprint-B02-02", "detector_footprint-B02-03", "detector_footprint-B02-04",
                           "detector_footprint-B02-05", "detector_footprint-B02-06", "detector_footprint-B03-01",
                           "detector_footprint-B03-02", "detector_footprint-B03-03", "detector_footprint-B03-04",
                           "detector_footprint-B03-05", "detector_footprint-B03-06", "detector_footprint-B04-01",
                           "detector_footprint-B04-02", "detector_footprint-B04-03", "detector_footprint-B04-04",
                           "detector_footprint-B04-05", "detector_footprint-B04-06", "detector_footprint-B08-01",
                           "detector_footprint-B08-02", "detector_footprint-B08-03", "detector_footprint-B08-04",
                           "detector_footprint-B08-05", "detector_footprint-B08-06", "nodata_B2",
                           "partially_corrected_crosstalk_B2", "nodata_B3", "partially_corrected_crosstalk_B3",
                           "nodata_B4", "partially_corrected_crosstalk_B4", "nodata_B8",
                           "partially_corrected_crosstalk_B8", "saturated_l1a_B2", "saturated_l1b_B2",
                           "saturated_l1a_B3", "saturated_l1b_B3", "saturated_l1a_B4", "saturated_l1b_B4",
                           "saturated_l1a_B8", "saturated_l1b_B8", "defective_B2", "defective_B3", "defective_B4",
                           "defective_B8", "ancillary_lost_B2", "ancillary_degraded_B2", "msi_lost_B2",
                           "msi_degraded_B2", "ancillary_lost_B3", "ancillary_degraded_B3", "msi_lost_B3",
                           "msi_degraded_B3", "ancillary_lost_B4", "ancillary_degraded_B4", "msi_lost_B4",
                           "msi_degraded_B4", "ancillary_lost_B8", "ancillary_degraded_B8", "msi_lost_B8",
                           "msi_degraded_B8"]
MASK_VARIABLE_NAMES_20m = ["opaque_clouds_20m", "cirrus_clouds_20m", "detector_footprint-B05-01",
                           "detector_footprint-B05-02", "detector_footprint-B05-03", "detector_footprint-B05-04",
                           "detector_footprint-B05-05", "detector_footprint-B05-06", "detector_footprint-B06-01",
                           "detector_footprint-B06-02", "detector_footprint-B06-03", "detector_footprint-B06-04",
                           "detector_footprint-B06-05", "detector_footprint-B06-06", "detector_footprint-B07-01",
                           "detector_footprint-B07-02", "detector_footprint-B07-03", "detector_footprint-B07-04",
                           "detector_footprint-B07-05", "detector_footprint-B07-06", "detector_footprint-B8A-01",
                           "detector_footprint-B8A-02", "detector_footprint-B8A-03", "detector_footprint-B8A-04",
                           "detector_footprint-B8A-05", "detector_footprint-B8A-06", "detector_footprint-B11-01",
                           "detector_footprint-B11-02", "detector_footprint-B11-03", "detector_footprint-B11-04",
                           "detector_footprint-B11-05", "detector_footprint-B11-06", "detector_footprint-B12-01",
                           "detector_footprint-B12-02", "detector_footprint-B12-03", "detector_footprint-B12-04",
                           "detector_footprint-B12-05", "detector_footprint-B12-06", "nodata_B5",
                           "partially_corrected_crosstalk_B5", "nodata_B6", "partially_corrected_crosstalk_B6",
                           "nodata_B7", "partially_corrected_crosstalk_B7", "nodata_B8A",
                           "partially_corrected_crosstalk_B8A", "nodata_B11", "partially_corrected_crosstalk_B11",
                           "nodata_B12", "partially_corrected_crosstalk_B12", "saturated_l1a_B5", "saturated_l1b_B5",
                           "saturated_l1a_B6", "saturated_l1b_B6", "saturated_l1a_B7", "saturated_l1b_B7",
                           "saturated_l1a_B8A", "saturated_l1b_B8A", "saturated_l1a_B11", "saturated_l1b_B11",
                           "saturated_l1a_B12", "saturated_l1b_B12", "defective_B5", "defective_B6", "defective_B7",
                           "defective_B8A", "defective_B11", "defective_B12", "ancillary_lost_B5",
                           "ancillary_degraded_B5", "msi_lost_B5", "msi_degraded_B5", "ancillary_lost_B6",
                           "ancillary_degraded_B6", "msi_lost_B6", "msi_degraded_B6", "ancillary_lost_B7",
                           "ancillary_degraded_B7", "msi_lost_B7", "msi_degraded_B7", "ancillary_lost_B8A",
                           "ancillary_degraded_B8A", "msi_lost_B8A", "msi_degraded_B8A", "ancillary_lost_B11",
                           "ancillary_degraded_B11", "msi_lost_B11", "msi_degraded_B11", "ancillary_lost_B12",
                           "ancillary_degraded_B12", "msi_lost_B12", "msi_degraded_B12"]
MASK_VARIABLE_NAMES_60m = ["opaque_clouds_60m", "cirrus_clouds_60m", "detector_footprint-B01-01",
                           "detector_footprint-B01-02", "detector_footprint-B01-03", "detector_footprint-B01-04",
                           "detector_footprint-B01-05", "detector_footprint-B01-06", "detector_footprint-B09-01",
                           "detector_footprint-B09-02", "detector_footprint-B09-03", "detector_footprint-B09-04",
                           "detector_footprint-B09-05", "detector_footprint-B09-06", "detector_footprint-B10-01",
                           "detector_footprint-B10-02", "detector_footprint-B10-03", "detector_footprint-B10-04",
                           "detector_footprint-B10-05", "detector_footprint-B10-06", "nodata_B1",
                           "partially_corrected_crosstalk_B1", "nodata_B9", "partially_corrected_crosstalk_B9",
                           "nodata_B10", "partially_corrected_crosstalk_B10", "saturated_l1a_B1", "saturated_l1b_B1",
                           "defective_B1", "ancillary_lost_B1", "ancillary_degraded_B1", "msi_lost_B1",
                           "msi_degraded_B1", "saturated_l1a_B9", "saturated_l1b_B9", "saturated_l1a_B10",
                           "saturated_l1b_B10", "defective_B9", "defective_B10", "ancillary_lost_B9",
                           "ancillary_degraded_B9", "msi_lost_B9", "msi_degraded_B9", "ancillary_lost_B10",
                           "ancillary_degraded_B10", "msi_lost_B10", "msi_degraded_B10"]
INFO_VARIABLE_NAMES_10m = ['view_zenith_mean', 'view_azimuth_mean', 'sun_zenith', 'sun_azimuth',
                           'view_zenith_B2', 'view_azimuth_B2',
                           'view_zenith_B3', 'view_azimuth_B3',
                           'view_zenith_B4', 'view_azimuth_B4',
                           'view_zenith_B8', 'view_azimuth_B8',
                           'quality_aot', 'quality_wvp', 'quality_cloud_confidence', 'quality_snow_confidence']
INFO_VARIABLE_NAMES_20m = ['view_zenith_mean', 'view_azimuth_mean', 'sun_zenith', 'sun_azimuth',
                           'view_zenith_B5', 'view_azimuth_B5',
                           'view_zenith_B6', 'view_azimuth_B6',
                           'view_zenith_B7', 'view_azimuth_B7',
                           'view_zenith_B8A', 'view_azimuth_B8A',
                           'view_zenith_B11', 'view_azimuth_B11',
                           'view_zenith_B12', 'view_azimuth_B12'
                           'quality_aot', 'quality_wvp', 'quality_cloud_confidence', 'quality_snow_confidence']
INFO_VARIABLE_NAMES_60m = ['view_zenith_mean', 'view_azimuth_mean', 'sun_zenith', 'sun_azimuth',
                           'view_zenith_B1', 'view_azimuth_B1',
                           'view_zenith_B9', 'view_azimuth_B9',
                           'view_zenith_B10', 'view_azimuth_B10'
                           'quality_aot', 'quality_wvp', 'quality_cloud_confidence', 'quality_snow_confidence']


class MSIL2Factory(MSISharedFactory):
    """
    MSIL2Factory is a sub-class of SnappySharedFactory for opening MSI L2a products

    :Methods:
        :readAttributes(product):
            Return dictionary with product attributes. Used to assign attributes attribute.

        :inherited from eopy.product.productIO.snappy_shared.SnappySharedFactory.SnappySharedFactory:
            :__init__():
                Initialises attributes

            :openProduct(product_path):
                Opens an in-memory representation of data product specified by product_path.

            :getData(product, variables, attributes, variable, [variable2, variable3, ...]):
                Returns variable[s] of in-memory product as an xarray data structure.

            :readVariables(product):
                Return dictionary with entry per variable for which data can be returned by getData(variable) method.
                Entry has variable name as key and dictionary of variables attributes as value. Used to assign variables
                attribute.

            :getPixelValues(product, variables, attributes, variable):
                Returns pixel values of variable of in-memory product as a numpy.ndarray

            :simplify_attrs(...):
                Return a simplified form of input attributes dictionary suitable for netcdf file attributes
    """

    def getDataVariableNames(self, product):
        """
        Returns list of product "data" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :return:
            :data_variable_names: *list*

            List of product "data" type variable names
        """

        h = product.getSceneRasterHeight()

        # 10m resolution
        if h == 10980:
            return self.return_available_variables(product, DATA_VARIABLE_NAMES_10m)

        # 20m resolution
        elif h == 5490:
            return self.return_available_variables(product, DATA_VARIABLE_NAMES_20m)

        # 20m resolution
        elif h == 1830:
            return self.return_available_variables(product, DATA_VARIABLE_NAMES_60m)

    def getMaskVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :mask_variable_names: *list*

            List of product "mask" type variable names
        """

        h = product.getSceneRasterHeight()

        # 10m resolution
        if h == 10980:
            return self.return_available_variables(product, MASK_VARIABLE_NAMES_10m)

        # 20m resolution
        elif h == 5490:
            return self.return_available_variables(product, MASK_VARIABLE_NAMES_20m)

        # 20m resolution
        elif h == 1830:
            return self.return_available_variables(product, MASK_VARIABLE_NAMES_60m)

    def getMeteorologicalVariableNames(self, product):
        """
        Returns list of product "meteorological" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :meteorological_variable_names: *list*

            List of product "meteorological" type variable names
        """

        meteorological_variable_names = []

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

        return []

    def getInfoVariableNames(self, product):
        """
        Returns list of product "info" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :info_variable_names: *list*

            List of product "info" type variable names
        """

        h = product.getSceneRasterHeight()

        # 10m resolution
        if h == 10980:
            return self.return_available_variables(product, INFO_VARIABLE_NAMES_10m)

        # 20m resolution
        elif h == 5490:
            return self.return_available_variables(product, INFO_VARIABLE_NAMES_20m)

        # 20m resolution
        elif h == 1830:
            return self.return_available_variables(product, INFO_VARIABLE_NAMES_60m)
        return []


if __name__ == "__main__":
    pass
