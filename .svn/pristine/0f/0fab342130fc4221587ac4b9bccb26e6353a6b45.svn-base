"""
Data factory for opening Sentinel-3/SLSTR L1b data
"""


'''___Built-In Modules___'''
import sys
from os.path import dirname
from copy import deepcopy
import re

# todo - use warnings to quiet snappy runtime errors
import warnings

'''___Third-Party Modules___'''
from os.path import join as pjoin

'''___NPL Modules___'''
sys.path.append(pjoin(dirname(dirname(__file__)), "snappy_shared"))
from SnappySharedFactory import SnappySharedFactory

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "18/06/2018"
__credits__ = []
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


DATA_VARIABLE_NAMES_1km = ["F1_BT_in", "F1_exception_in", "F1_BT_io", "F1_exception_io", "F2_BT_in", "F2_exception_in",
                           "F2_BT_io", "F2_exception_io", "S7_BT_in", "S7_exception_in", "S7_BT_io", "S7_exception_io",
                           "S8_BT_in", "S8_exception_in", "S8_BT_io", "S8_exception_io", "S9_BT_in", "S9_exception_in",
                           "S9_BT_io", "S9_exception_io"]
DATA_VARIABLE_NAMES_500m = ["S1_exception_an", "S1_radiance_an", "S1_exception_ao", "S1_radiance_ao", "S2_exception_an",
                            "S2_radiance_an", "S2_exception_ao", "S2_radiance_ao", "S3_exception_an", "S3_radiance_an",
                            "S3_exception_ao", "S3_radiance_ao", "S4_exception_an", "S4_radiance_an", "S4_exception_ao",
                            "S4_radiance_ao", "S4_exception_bn", "S4_radiance_bn", "S4_exception_bo", "S4_radiance_bo",
                            "S4_exception_cn", "S4_radiance_cn", "S4_exception_co", "S4_radiance_co", "S5_exception_an",
                            "S5_radiance_an", "S5_exception_ao", "S5_radiance_ao", "S5_exception_bn", "S5_radiance_bn",
                            "S5_exception_bo", "S5_radiance_bo", "S5_exception_cn", "S5_radiance_cn", "S5_exception_co",
                            "S5_radiance_co", "S6_exception_an", "S6_radiance_an", "S6_exception_ao", "S6_radiance_ao",
                            "S6_exception_bn", "S6_radiance_bn", "S6_exception_bo", "S6_radiance_bo", "S6_exception_cn",
                            "S6_radiance_cn", "S6_exception_co", "S6_radiance_co"]
MASK_VARIABLE_NAMES_1km = ["F1_exception_in_ISP_absent", "F1_exception_in_pixel_absent",
                           "F1_exception_in_not_decompressed", "F1_exception_in_no_signal",
                           "F1_exception_in_saturation", "F1_exception_in_invalid_radiance",
                           "F1_exception_in_no_parameters", "F1_exception_in_unfilled_pixel",
                           "F1_exception_io_ISP_absent", "F1_exception_io_pixel_absent",
                           "F1_exception_io_not_decompressed", "F1_exception_io_no_signal",
                           "F1_exception_io_saturation", "F1_exception_io_invalid_radiance",
                           "F1_exception_io_no_parameters", "F1_exception_io_unfilled_pixel",
                           "F2_exception_in_ISP_absent", "F2_exception_in_pixel_absent",
                           "F2_exception_in_not_decompressed", "F2_exception_in_no_signal",
                           "F2_exception_in_saturation", "F2_exception_in_invalid_radiance",
                           "F2_exception_in_no_parameters", "F2_exception_in_unfilled_pixel",
                           "F2_exception_io_ISP_absent", "F2_exception_io_pixel_absent",
                           "F2_exception_io_not_decompressed", "F2_exception_io_no_signal",
                           "F2_exception_io_saturation", "F2_exception_io_invalid_radiance",
                           "F2_exception_io_no_parameters", "F2_exception_io_unfilled_pixel",
                           "bayes_in_single_low", "bayes_in_single_moderate", "bayes_in_dual_low",
                           "bayes_in_dual_moderate", "cloud_in_visible", "cloud_in_1_37_threshold",
                           "cloud_in_1_6_small_histogram", "cloud_in_1_6_large_histogram",
                           "cloud_in_2_25_small_histogram", "cloud_in_2_25_large_histogram",
                           "cloud_in_11_spatial_coherence", "cloud_in_gross_cloud", "cloud_in_thin_cirrus",
                           "cloud_in_medium_high", "cloud_in_fog_low_stratus", "cloud_in_11_12_view_difference",
                           "cloud_in_3_7_11_view_difference", "cloud_in_thermal_histogram", "confidence_in_coastline",
                           "confidence_in_ocean", "confidence_in_tidal", "confidence_in_land",
                           "confidence_in_inland_water", "confidence_in_unfilled", "confidence_in_cosmetic",
                           "confidence_in_duplicate", "confidence_in_day", "confidence_in_twilight",
                           "confidence_in_sun_glint", "confidence_in_snow", "confidence_in_summary_cloud",
                           "confidence_in_summary_pointing", "pointing_in_FlipMirrorAbsoluteError",
                           "pointing_in_FlipMirrorIntegratedError", "pointing_in_FlipMirrorRMSError",
                           "pointing_in_ScanMirrorAbsoluteError", "pointing_in_ScanMirrorIntegratedError",
                           "pointing_in_ScanMirrorRMSError", "pointing_in_ScanTimeError", "pointing_in_Platform_Mode",
                           "bayes_io_single_low", "bayes_io_single_moderate", "bayes_io_dual_low",
                           "bayes_io_dual_moderate", "cloud_io_visible", "cloud_io_1_37_threshold",
                           "cloud_io_1_6_small_histogram", "cloud_io_1_6_large_histogram",
                           "cloud_io_2_25_small_histogram", "cloud_io_2_25_large_histogram",
                           "cloud_io_11_spatial_coherence", "cloud_io_gross_cloud", "cloud_io_thin_cirrus",
                           "cloud_io_medium_high", "cloud_io_fog_low_stratus", "cloud_io_11_12_view_difference",
                           "cloud_io_3_7_11_view_difference", "cloud_io_thermal_histogram", "confidence_io_coastline",
                           "confidence_io_ocean", "confidence_io_tidal", "confidence_io_land",
                           "confidence_io_inland_water", "confidence_io_unfilled", "confidence_io_cosmetic",
                           "confidence_io_duplicate", "confidence_io_day", "confidence_io_twilight",
                           "confidence_io_sun_glint", "confidence_io_snow", "confidence_io_summary_cloud",
                           "confidence_io_summary_pointing", "pointing_io_FlipMirrorAbsoluteError",
                           "pointing_io_FlipMirrorIntegratedError", "pointing_io_FlipMirrorRMSError",
                           "pointing_io_ScanMirrorAbsoluteError", "pointing_io_ScanMirrorIntegratedError",
                           "pointing_io_ScanMirrorRMSError", "pointing_io_ScanTimeError", "pointing_io_Platform_Mode",
                           "S7_exception_in_ISP_absent", "S7_exception_in_pixel_absent",
                           "S7_exception_in_not_decompressed", "S7_exception_in_no_signal",
                           "S7_exception_in_saturation", "S7_exception_in_invalid_radiance",
                           "S7_exception_in_no_parameters", "S7_exception_in_unfilled_pixel",
                           "S7_exception_io_ISP_absent", "S7_exception_io_pixel_absent",
                           "S7_exception_io_not_decompressed", "S7_exception_io_no_signal",
                           "S7_exception_io_saturation", "S7_exception_io_invalid_radiance",
                           "S7_exception_io_no_parameters", "S7_exception_io_unfilled_pixel",
                           "S8_exception_in_ISP_absent", "S8_exception_in_pixel_absent",
                           "S8_exception_in_not_decompressed", "S8_exception_in_no_signal",
                           "S8_exception_in_saturation", "S8_exception_in_invalid_radiance",
                           "S8_exception_in_no_parameters", "S8_exception_in_unfilled_pixel",
                           "S8_exception_io_ISP_absent", "S8_exception_io_pixel_absent",
                           "S8_exception_io_not_decompressed", "S8_exception_io_no_signal",
                           "S8_exception_io_saturation", "S8_exception_io_invalid_radiance",
                           "S8_exception_io_no_parameters", "S8_exception_io_unfilled_pixel",
                           "S9_exception_in_ISP_absent", "S9_exception_in_pixel_absent",
                           "S9_exception_in_not_decompressed", "S9_exception_in_no_signal",
                           "S9_exception_in_saturation", "S9_exception_in_invalid_radiance",
                           "S9_exception_in_no_parameters", "S9_exception_in_unfilled_pixel",
                           "S9_exception_io_ISP_absent", "S9_exception_io_pixel_absent",
                           "S9_exception_io_not_decompressed", "S9_exception_io_no_signal",
                           "S9_exception_io_saturation", "S9_exception_io_invalid_radiance",
                           "S9_exception_io_no_parameters", "S9_exception_io_unfilled_pixel"]
MASK_VARIABLE_NAMES_500m = ["bayes_an_single_low", "bayes_an_single_moderate", "bayes_an_dual_low",
                            "bayes_an_dual_moderate", "cloud_an_visible", "cloud_an_1_37_threshold",
                            "cloud_an_1_6_small_histogram", "cloud_an_1_6_large_histogram",
                            "cloud_an_2_25_small_histogram", "cloud_an_2_25_large_histogram",
                            "cloud_an_11_spatial_coherence", "cloud_an_gross_cloud", "cloud_an_thin_cirrus",
                            "cloud_an_medium_high", "cloud_an_fog_low_stratus", "cloud_an_11_12_view_difference",
                            "cloud_an_3_7_11_view_difference", "cloud_an_thermal_histogram", "confidence_an_coastline",
                            "confidence_an_ocean", "confidence_an_tidal", "confidence_an_land",
                            "confidence_an_inland_water", "confidence_an_unfilled", "confidence_an_cosmetic",
                            "confidence_an_duplicate", "confidence_an_day", "confidence_an_twilight",
                            "confidence_an_sun_glint", "confidence_an_snow", "confidence_an_summary_cloud",
                            "confidence_an_summary_pointing", "pointing_an_FlipMirrorAbsoluteError",
                            "pointing_an_FlipMirrorIntegratedError", "pointing_an_FlipMirrorRMSError",
                            "pointing_an_ScanMirrorAbsoluteError", "pointing_an_ScanMirrorIntegratedError",
                            "pointing_an_ScanMirrorRMSError", "pointing_an_ScanTimeError", "pointing_an_Platform_Mode",
                            "bayes_ao_single_low", "bayes_ao_single_moderate", "bayes_ao_dual_low",
                            "bayes_ao_dual_moderate", "cloud_ao_visible", "cloud_ao_1_37_threshold",
                            "cloud_ao_1_6_small_histogram", "cloud_ao_1_6_large_histogram",
                            "cloud_ao_2_25_small_histogram", "cloud_ao_2_25_large_histogram",
                            "cloud_ao_11_spatial_coherence", "cloud_ao_gross_cloud", "cloud_ao_thin_cirrus",
                            "cloud_ao_medium_high", "cloud_ao_fog_low_stratus", "cloud_ao_11_12_view_difference",
                            "cloud_ao_3_7_11_view_difference", "cloud_ao_thermal_histogram", "confidence_ao_coastline",
                            "confidence_ao_ocean", "confidence_ao_tidal", "confidence_ao_land",
                            "confidence_ao_inland_water", "confidence_ao_unfilled", "confidence_ao_cosmetic",
                            "confidence_ao_duplicate", "confidence_ao_day", "confidence_ao_twilight",
                            "confidence_ao_sun_glint", "confidence_ao_snow", "confidence_ao_summary_cloud",
                            "confidence_ao_summary_pointing", "pointing_ao_FlipMirrorAbsoluteError",
                            "pointing_ao_FlipMirrorIntegratedError", "pointing_ao_FlipMirrorRMSError",
                            "pointing_ao_ScanMirrorAbsoluteError", "pointing_ao_ScanMirrorIntegratedError",
                            "pointing_ao_ScanMirrorRMSError", "pointing_ao_ScanTimeError", "pointing_ao_Platform_Mode",
                            "bayes_bn_single_low", "bayes_bn_single_moderate", "bayes_bn_dual_low",
                            "bayes_bn_dual_moderate", "cloud_bn_visible", "cloud_bn_1_37_threshold",
                            "cloud_bn_1_6_small_histogram", "cloud_bn_1_6_large_histogram",
                            "cloud_bn_2_25_small_histogram", "cloud_bn_2_25_large_histogram",
                            "cloud_bn_11_spatial_coherence", "cloud_bn_gross_cloud", "cloud_bn_thin_cirrus",
                            "cloud_bn_medium_high", "cloud_bn_fog_low_stratus", "cloud_bn_11_12_view_difference",
                            "cloud_bn_3_7_11_view_difference", "cloud_bn_thermal_histogram", "confidence_bn_coastline",
                            "confidence_bn_ocean", "confidence_bn_tidal", "confidence_bn_land",
                            "confidence_bn_inland_water", "confidence_bn_unfilled", "confidence_bn_cosmetic",
                            "confidence_bn_duplicate", "confidence_bn_day", "confidence_bn_twilight",
                            "confidence_bn_sun_glint", "confidence_bn_snow", "confidence_bn_summary_cloud",
                            "confidence_bn_summary_pointing", "pointing_bn_FlipMirrorAbsoluteError",
                            "pointing_bn_FlipMirrorIntegratedError", "pointing_bn_FlipMirrorRMSError",
                            "pointing_bn_ScanMirrorAbsoluteError", "pointing_bn_ScanMirrorIntegratedError",
                            "pointing_bn_ScanMirrorRMSError", "pointing_bn_ScanTimeError", "pointing_bn_Platform_Mode",
                            "bayes_bo_single_low", "bayes_bo_single_moderate", "bayes_bo_dual_low",
                            "bayes_bo_dual_moderate", "cloud_bo_visible", "cloud_bo_1_37_threshold",
                            "cloud_bo_1_6_small_histogram", "cloud_bo_1_6_large_histogram",
                            "cloud_bo_2_25_small_histogram", "cloud_bo_2_25_large_histogram",
                            "cloud_bo_11_spatial_coherence", "cloud_bo_gross_cloud", "cloud_bo_thin_cirrus",
                            "cloud_bo_medium_high", "cloud_bo_fog_low_stratus", "cloud_bo_11_12_view_difference",
                            "cloud_bo_3_7_11_view_difference", "cloud_bo_thermal_histogram", "confidence_bo_coastline",
                            "confidence_bo_ocean", "confidence_bo_tidal", "confidence_bo_land",
                            "confidence_bo_inland_water", "confidence_bo_unfilled", "confidence_bo_cosmetic",
                            "confidence_bo_duplicate", "confidence_bo_day", "confidence_bo_twilight",
                            "confidence_bo_sun_glint", "confidence_bo_snow", "confidence_bo_summary_cloud",
                            "confidence_bo_summary_pointing", "pointing_bo_FlipMirrorAbsoluteError",
                            "pointing_bo_FlipMirrorIntegratedError", "pointing_bo_FlipMirrorRMSError",
                            "pointing_bo_ScanMirrorAbsoluteError", "pointing_bo_ScanMirrorIntegratedError",
                            "pointing_bo_ScanMirrorRMSError", "pointing_bo_ScanTimeError", "pointing_bo_Platform_Mode",
                            "bayes_cn_single_low", "bayes_cn_single_moderate", "bayes_cn_dual_low",
                            "bayes_cn_dual_moderate", "cloud_cn_visible", "cloud_cn_1_37_threshold",
                            "cloud_cn_1_6_small_histogram", "cloud_cn_1_6_large_histogram",
                            "cloud_cn_2_25_small_histogram", "cloud_cn_2_25_large_histogram",
                            "cloud_cn_11_spatial_coherence", "cloud_cn_gross_cloud", "cloud_cn_thin_cirrus",
                            "cloud_cn_medium_high", "cloud_cn_fog_low_stratus", "cloud_cn_11_12_view_difference",
                            "cloud_cn_3_7_11_view_difference", "cloud_cn_thermal_histogram", "confidence_cn_coastline",
                            "confidence_cn_ocean", "confidence_cn_tidal", "confidence_cn_land",
                            "confidence_cn_inland_water", "confidence_cn_unfilled", "confidence_cn_cosmetic",
                            "confidence_cn_duplicate", "confidence_cn_day", "confidence_cn_twilight",
                            "confidence_cn_sun_glint", "confidence_cn_snow", "confidence_cn_summary_cloud",
                            "confidence_cn_summary_pointing", "pointing_cn_FlipMirrorAbsoluteError",
                            "pointing_cn_FlipMirrorIntegratedError", "pointing_cn_FlipMirrorRMSError",
                            "pointing_cn_ScanMirrorAbsoluteError", "pointing_cn_ScanMirrorIntegratedError",
                            "pointing_cn_ScanMirrorRMSError", "pointing_cn_ScanTimeError", "pointing_cn_Platform_Mode",
                            "bayes_co_single_low", "bayes_co_single_moderate", "bayes_co_dual_low",
                            "bayes_co_dual_moderate", "cloud_co_visible", "cloud_co_1_37_threshold",
                            "cloud_co_1_6_small_histogram", "cloud_co_1_6_large_histogram",
                            "cloud_co_2_25_small_histogram", "cloud_co_2_25_large_histogram",
                            "cloud_co_11_spatial_coherence", "cloud_co_gross_cloud", "cloud_co_thin_cirrus",
                            "cloud_co_medium_high", "cloud_co_fog_low_stratus", "cloud_co_11_12_view_difference",
                            "cloud_co_3_7_11_view_difference", "cloud_co_thermal_histogram", "confidence_co_coastline",
                            "confidence_co_ocean", "confidence_co_tidal", "confidence_co_land",
                            "confidence_co_inland_water", "confidence_co_unfilled", "confidence_co_cosmetic",
                            "confidence_co_duplicate", "confidence_co_day", "confidence_co_twilight",
                            "confidence_co_sun_glint", "confidence_co_snow", "confidence_co_summary_cloud",
                            "confidence_co_summary_pointing", "pointing_co_FlipMirrorAbsoluteError",
                            "pointing_co_FlipMirrorIntegratedError", "pointing_co_FlipMirrorRMSError",
                            "pointing_co_ScanMirrorAbsoluteError", "pointing_co_ScanMirrorIntegratedError",
                            "pointing_co_ScanMirrorRMSError", "pointing_co_ScanTimeError", "pointing_co_Platform_Mode",
                            "S1_exception_an_ISP_absent", "S1_exception_an_pixel_absent",
                            "S1_exception_an_not_decompressed", "S1_exception_an_no_signal",
                            "S1_exception_an_saturation", "S1_exception_an_invalid_radiance",
                            "S1_exception_an_no_parameters", "S1_exception_an_unfilled_pixel",
                            "S1_exception_ao_ISP_absent", "S1_exception_ao_pixel_absent",
                            "S1_exception_ao_not_decompressed", "S1_exception_ao_no_signal",
                            "S1_exception_ao_saturation", "S1_exception_ao_invalid_radiance",
                            "S1_exception_ao_no_parameters", "S1_exception_ao_unfilled_pixel",
                            "S2_exception_an_ISP_absent", "S2_exception_an_pixel_absent",
                            "S2_exception_an_not_decompressed", "S2_exception_an_no_signal",
                            "S2_exception_an_saturation", "S2_exception_an_invalid_radiance",
                            "S2_exception_an_no_parameters", "S2_exception_an_unfilled_pixel",
                            "S2_exception_ao_ISP_absent", "S2_exception_ao_pixel_absent",
                            "S2_exception_ao_not_decompressed", "S2_exception_ao_no_signal",
                            "S2_exception_ao_saturation", "S2_exception_ao_invalid_radiance",
                            "S2_exception_ao_no_parameters", "S2_exception_ao_unfilled_pixel",
                            "S3_exception_an_ISP_absent", "S3_exception_an_pixel_absent",
                            "S3_exception_an_not_decompressed", "S3_exception_an_no_signal",
                            "S3_exception_an_saturation", "S3_exception_an_invalid_radiance",
                            "S3_exception_an_no_parameters", "S3_exception_an_unfilled_pixel",
                            "S3_exception_ao_ISP_absent", "S3_exception_ao_pixel_absent",
                            "S3_exception_ao_not_decompressed", "S3_exception_ao_no_signal",
                            "S3_exception_ao_saturation", "S3_exception_ao_invalid_radiance",
                            "S3_exception_ao_no_parameters", "S3_exception_ao_unfilled_pixel",
                            "S4_exception_an_ISP_absent", "S4_exception_an_pixel_absent",
                            "S4_exception_an_not_decompressed", "S4_exception_an_no_signal",
                            "S4_exception_an_saturation", "S4_exception_an_invalid_radiance",
                            "S4_exception_an_no_parameters", "S4_exception_an_unfilled_pixel",
                            "S4_exception_ao_ISP_absent", "S4_exception_ao_pixel_absent",
                            "S4_exception_ao_not_decompressed", "S4_exception_ao_no_signal",
                            "S4_exception_ao_saturation", "S4_exception_ao_invalid_radiance",
                            "S4_exception_ao_no_parameters", "S4_exception_ao_unfilled_pixel",
                            "S4_exception_bn_ISP_absent", "S4_exception_bn_pixel_absent",
                            "S4_exception_bn_not_decompressed", "S4_exception_bn_no_signal",
                            "S4_exception_bn_saturation", "S4_exception_bn_invalid_radiance",
                            "S4_exception_bn_no_parameters", "S4_exception_bn_unfilled_pixel",
                            "S4_exception_bo_ISP_absent", "S4_exception_bo_pixel_absent",
                            "S4_exception_bo_not_decompressed", "S4_exception_bo_no_signal",
                            "S4_exception_bo_saturation", "S4_exception_bo_invalid_radiance",
                            "S4_exception_bo_no_parameters", "S4_exception_bo_unfilled_pixel",
                            "S4_exception_cn_ISP_absent", "S4_exception_cn_pixel_absent",
                            "S4_exception_cn_not_decompressed", "S4_exception_cn_no_signal",
                            "S4_exception_cn_saturation", "S4_exception_cn_invalid_radiance",
                            "S4_exception_cn_no_parameters", "S4_exception_cn_unfilled_pixel",
                            "S4_exception_co_ISP_absent", "S4_exception_co_pixel_absent",
                            "S4_exception_co_not_decompressed", "S4_exception_co_no_signal",
                            "S4_exception_co_saturation", "S4_exception_co_invalid_radiance",
                            "S4_exception_co_no_parameters", "S4_exception_co_unfilled_pixel",
                            "S5_exception_an_ISP_absent", "S5_exception_an_pixel_absent",
                            "S5_exception_an_not_decompressed", "S5_exception_an_no_signal",
                            "S5_exception_an_saturation", "S5_exception_an_invalid_radiance",
                            "S5_exception_an_no_parameters", "S5_exception_an_unfilled_pixel",
                            "S5_exception_ao_ISP_absent", "S5_exception_ao_pixel_absent",
                            "S5_exception_ao_not_decompressed", "S5_exception_ao_no_signal",
                            "S5_exception_ao_saturation", "S5_exception_ao_invalid_radiance",
                            "S5_exception_ao_no_parameters", "S5_exception_ao_unfilled_pixel",
                            "S5_exception_bn_ISP_absent", "S5_exception_bn_pixel_absent",
                            "S5_exception_bn_not_decompressed", "S5_exception_bn_no_signal",
                            "S5_exception_bn_saturation", "S5_exception_bn_invalid_radiance",
                            "S5_exception_bn_no_parameters", "S5_exception_bn_unfilled_pixel",
                            "S5_exception_bo_ISP_absent", "S5_exception_bo_pixel_absent",
                            "S5_exception_bo_not_decompressed", "S5_exception_bo_no_signal",
                            "S5_exception_bo_saturation", "S5_exception_bo_invalid_radiance",
                            "S5_exception_bo_no_parameters", "S5_exception_bo_unfilled_pixel",
                            "S5_exception_cn_ISP_absent", "S5_exception_cn_pixel_absent",
                            "S5_exception_cn_not_decompressed", "S5_exception_cn_no_signal",
                            "S5_exception_cn_saturation", "S5_exception_cn_invalid_radiance",
                            "S5_exception_cn_no_parameters", "S5_exception_cn_unfilled_pixel",
                            "S5_exception_co_ISP_absent", "S5_exception_co_pixel_absent",
                            "S5_exception_co_not_decompressed", "S5_exception_co_no_signal",
                            "S5_exception_co_saturation", "S5_exception_co_invalid_radiance",
                            "S5_exception_co_no_parameters", "S5_exception_co_unfilled_pixel",
                            "S6_exception_an_ISP_absent", "S6_exception_an_pixel_absent",
                            "S6_exception_an_not_decompressed", "S6_exception_an_no_signal",
                            "S6_exception_an_saturation", "S6_exception_an_invalid_radiance",
                            "S6_exception_an_no_parameters", "S6_exception_an_unfilled_pixel",
                            "S6_exception_ao_ISP_absent", "S6_exception_ao_pixel_absent",
                            "S6_exception_ao_not_decompressed", "S6_exception_ao_no_signal",
                            "S6_exception_ao_saturation", "S6_exception_ao_invalid_radiance",
                            "S6_exception_ao_no_parameters", "S6_exception_ao_unfilled_pixel",
                            "S6_exception_bn_ISP_absent", "S6_exception_bn_pixel_absent",
                            "S6_exception_bn_not_decompressed", "S6_exception_bn_no_signal",
                            "S6_exception_bn_saturation", "S6_exception_bn_invalid_radiance",
                            "S6_exception_bn_no_parameters", "S6_exception_bn_unfilled_pixel",
                            "S6_exception_bo_ISP_absent", "S6_exception_bo_pixel_absent",
                            "S6_exception_bo_not_decompressed", "S6_exception_bo_no_signal",
                            "S6_exception_bo_saturation", "S6_exception_bo_invalid_radiance",
                            "S6_exception_bo_no_parameters", "S6_exception_bo_unfilled_pixel",
                            "S6_exception_cn_ISP_absent", "S6_exception_cn_pixel_absent",
                            "S6_exception_cn_not_decompressed", "S6_exception_cn_no_signal",
                            "S6_exception_cn_saturation", "S6_exception_cn_invalid_radiance",
                            "S6_exception_cn_no_parameters", "S6_exception_cn_unfilled_pixel",
                            "S6_exception_co_ISP_absent", "S6_exception_co_pixel_absent",
                            "S6_exception_co_not_decompressed", "S6_exception_co_no_signal",
                            "S6_exception_co_saturation", "S6_exception_co_invalid_radiance",
                            "S6_exception_co_no_parameters", "S6_exception_co_unfilled_pixel"]
METEOROLOGICAL_VARIABLE_NAMES = ["cloud_fraction_tx", "dew_point_tx", "east_west_stress_tx_time_1_tx",
                                 "east_west_stress_tx_time_2_tx", "east_west_stress_tx_time_3_tx",
                                 "east_west_stress_tx_time_4_tx", "east_west_stress_tx_time_5_tx",
                                 "latent_heat_tx_time_1_tx", "latent_heat_tx_time_2_tx", "latent_heat_tx_time_3_tx",
                                 "latent_heat_tx_time_4_tx", "latent_heat_tx_time_5_tx", "surface_pressure_tx",
                                 "north_south_stress_tx_time_1_tx", "north_south_stress_tx_time_2_tx",
                                 "north_south_stress_tx_time_3_tx", "north_south_stress_tx_time_4_tx",
                                 "north_south_stress_tx_time_5_tx", "sea_ice_fraction_tx", "sea_surface_temperature_tx",
                                 "sensible_heat_tx_time_1_tx", "sensible_heat_tx_time_2_tx",
                                 "sensible_heat_tx_time_3_tx", "sensible_heat_tx_time_4_tx",
                                 "sensible_heat_tx_time_5_tx", "skin_temperature_tx", "snow_albedo_tx", "snow_depth_tx",
                                 "soil_wetness_tx", "solar_radiation_tx_time_1_tx", "solar_radiation_tx_time_2_tx",
                                 "solar_radiation_tx_time_3_tx", "solar_radiation_tx_time_4_tx",
                                 "solar_radiation_tx_time_5_tx", "specific_humidity_tx_pressure_level_1_tx",
                                 "specific_humidity_tx_pressure_level_2_tx", "specific_humidity_tx_pressure_level_3_tx",
                                 "specific_humidity_tx_pressure_level_4_tx", "specific_humidity_tx_pressure_level_5_tx",
                                 "specific_humidity_tx_pressure_level_6_tx", "specific_humidity_tx_pressure_level_7_tx",
                                 "specific_humidity_tx_pressure_level_8_tx", "specific_humidity_tx_pressure_level_9_tx",
                                 "specific_humidity_tx_pressure_level_10_tx",
                                 "specific_humidity_tx_pressure_level_11_tx",
                                 "specific_humidity_tx_pressure_level_12_tx",
                                 "specific_humidity_tx_pressure_level_13_tx",
                                 "specific_humidity_tx_pressure_level_14_tx",
                                 "specific_humidity_tx_pressure_level_15_tx",
                                 "specific_humidity_tx_pressure_level_16_tx",
                                 "specific_humidity_tx_pressure_level_17_tx",
                                 "specific_humidity_tx_pressure_level_18_tx",
                                 "specific_humidity_tx_pressure_level_19_tx",
                                 "specific_humidity_tx_pressure_level_20_tx",
                                 "specific_humidity_tx_pressure_level_21_tx",
                                 "specific_humidity_tx_pressure_level_22_tx",
                                 "specific_humidity_tx_pressure_level_23_tx",
                                 "specific_humidity_tx_pressure_level_24_tx",
                                 "specific_humidity_tx_pressure_level_25_tx",
                                 "temperature_profile_tx_pressure_level_1_tx",
                                 "temperature_profile_tx_pressure_level_2_tx",
                                 "temperature_profile_tx_pressure_level_3_tx",
                                 "temperature_profile_tx_pressure_level_4_tx",
                                 "temperature_profile_tx_pressure_level_5_tx",
                                 "temperature_profile_tx_pressure_level_6_tx",
                                 "temperature_profile_tx_pressure_level_7_tx",
                                 "temperature_profile_tx_pressure_level_8_tx",
                                 "temperature_profile_tx_pressure_level_9_tx",
                                 "temperature_profile_tx_pressure_level_10_tx",
                                 "temperature_profile_tx_pressure_level_11_tx",
                                 "temperature_profile_tx_pressure_level_12_tx",
                                 "temperature_profile_tx_pressure_level_13_tx",
                                 "temperature_profile_tx_pressure_level_14_tx",
                                 "temperature_profile_tx_pressure_level_15_tx",
                                 "temperature_profile_tx_pressure_level_16_tx",
                                 "temperature_profile_tx_pressure_level_17_tx",
                                 "temperature_profile_tx_pressure_level_18_tx",
                                 "temperature_profile_tx_pressure_level_19_tx",
                                 "temperature_profile_tx_pressure_level_20_tx",
                                 "temperature_profile_tx_pressure_level_21_tx",
                                 "temperature_profile_tx_pressure_level_22_tx",
                                 "temperature_profile_tx_pressure_level_23_tx",
                                 "temperature_profile_tx_pressure_level_24_tx",
                                 "temperature_profile_tx_pressure_level_25_tx",
                                 "temperature_tx", "thermal_radiation_tx_time_1_tx", "thermal_radiation_tx_time_2_tx",
                                 "thermal_radiation_tx_time_3_tx", "thermal_radiation_tx_time_4_tx",
                                 "thermal_radiation_tx_time_5_tx", "total_column_ozone_tx",
                                 "total_column_water_vapour_tx", "u_wind_tx_time_1_tx", "u_wind_tx_time_2_tx",
                                 "u_wind_tx_time_3_tx", "u_wind_tx_time_4_tx", "u_wind_tx_time_5_tx",
                                 "v_wind_tx_time_1_tx", "v_wind_tx_time_2_tx", "v_wind_tx_time_3_tx",
                                 "v_wind_tx_time_4_tx", "v_wind_tx_time_5_tx"]
SENSOR_VARIABLE_NAMES_500m = ["detector_an", "pixel_an", "scan_an", "detector_ao", "pixel_ao", "scan_ao", "detector_bn",
                              "pixel_bn", "scan_bn", "detector_bo", "pixel_bo", "scan_bo", "detector_cn", "pixel_cn",
                              "scan_cn", "detector_co", "pixel_co", "scan_co"]
SENSOR_VARIABLE_NAMES_1km = ["detector_in", "pixel_in", "scan_in", "detector_io", "pixel_io", "scan_io"]
INFO_VARIABLE_NAMES_500m = ["x_an", "y_an", "x_ao", "y_ao", "x_bn", "y_bn", "x_bo", "y_bo", "x_cn", "y_cn", "x_co",
                            "y_co", "elevation_an", "latitude_an", "longitude_an",
                            "elevation_ao", "latitude_ao", "longitude_ao", "elevation_bn", "latitude_bn",
                            "longitude_bn", "elevation_bo", "latitude_bo", "longitude_bo", "elevation_cn",
                            "latitude_cn", "longitude_cn", "elevation_co", "latitude_co", "longitude_co",
                            "x_tx", "y_tx", "latitude_tx", "longitude_tx", "sat_azimuth_tn",
                            "sat_path_tn", "sat_zenith_tn", "solar_azimuth_tn", "solar_path_tn", "solar_zenith_tn",
                            "sat_azimuth_to", "sat_path_to", "sat_zenith_to", "solar_azimuth_to", "solar_path_to",
                            "solar_zenith_to", "bayes_an", "cloud_an", "confidence_an", "pointing_an", "bayes_ao",
                            "cloud_ao", "confidence_ao", "pointing_ao", "bayes_bn", "cloud_bn", "confidence_bn",
                            "pointing_bn", "bayes_bo", "cloud_bo", "confidence_bo", "pointing_bo", "bayes_cn",
                            "cloud_cn", "confidence_cn", "pointing_cn", "bayes_co", "cloud_co", "confidence_co",
                            "pointing_co",]
INFO_VARIABLE_NAMES_1km = ["x_in", "y_in", "x_io", "y_io", "elevation_in", "latitude_in", "longitude_in",
                           "elevation_io", "latitude_io", "longitude_io", "x_tx", "y_tx", "latitude_tx", "longitude_tx",
                           "sat_azimuth_tn", "sat_path_tn", "sat_zenith_tn", "solar_azimuth_tn", "solar_path_tn",
                           "solar_zenith_tn", "sat_azimuth_to", "sat_path_to", "sat_zenith_to", "solar_azimuth_to",
                           "solar_path_to", "solar_zenith_to", "bayes_in", "cloud_in", "confidence_in", "pointing_in",
                           "probability_cloud_dual_in", "probability_cloud_single_in", "bayes_io", "cloud_io",
                           "confidence_io", "pointing_io", "probability_cloud_dual_io", "probability_cloud_single_io"]


def convert_cc2sc(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


class SLSTRL1Factory(SnappySharedFactory):
    """
    SLSTRL1Factory is a class for reading SLSTR L1 BT products

    :Methods:
        .. py:method:: getDataVariableNames(...):

            Returns list of product "data" type variable names

        .. py:method:: getMeteorologicalVariableNames(...):

            Returns list of product "meteorological" type variable names

        .. py:method:: getSensorVariableNames(...):

            Returns list of product "sensor" type variable names

        .. py:method:: getInfoVariableNames(...):

            Returns list of product "data" type variable names

        . py:method:: readAttributes(...):

            Returns dictionary of product attributes

        :Inherited from ``eopy.product.productIO.snappy_shared.SnappySharedFactory.SnappySharedFactory:
            .. py:method:: openProduct(...):

                Opens an in-memory representation of data product specified by product_path.

            .. py:method:: readVariables(...):

                Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

            .. py:method:: createDataVariable(...):

                Returns "data" type `SpectralVariable` class objects, for given product variable

            .. py:method:: getMaskVariableNames(...):

                Returns list of product "mask" type variable names

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

                Returns pixel values of variable of in-memory product

            :Inherited from eopy.product.productIO.AbstractDataFactory.AbstractDataFactory:
                .. py:method:: readVariables(...):

                    Returns list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

                .. py:method:: getDataVariables(...):

                    Returns list of product "data" type variables as ``Variable`` or `SpectralVariable` class objects.

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

                    Returns 'meteorological' variable objects with attributes edited compared to default values obtained
                    from product

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
    FACTORY_STRING = "SLSTRL1Factory"
    TYPE_STRING = "SL_1_RBT"

    def openProduct(self, product_path):
        """
        Opens an in-memory represenation of snappy data product at specified path with metadata

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :product: *dict*

            List of product dictionaries - which themselves contain in-memory representation of opened `snappy.Product`
            data products, one for the 500m and one for the 1km products.

            :variables: *list*

            List of products variables as ``Variable`` or ``SpectralVariable`` class objects.

            :attributes: *dict*

            Dictionary of product attributes.
        """

        products = self.openMultipleProducts([{"product_name": "SLSLTRL1500m",
                                               "product_path": product_path,
                                               "product_reader": 'Sen3_SLSTRL1B_500m'},
                                              {"product_name": "SLSTRL11km",
                                               "product_path": product_path,
                                               "product_reader": 'Sen3_SLSTRL1B_1km'}])

        products, variables = self.readVariables(products)
        products, attributes = self.readAttributes(products)
        products, attributes = self.addAttributes(products, attributes)

        return products, variables, attributes

    def addAttributes(self, products, attributes):
        """
        Return dictionary of products attributes with additional entries specific to SLSTR

        :type product: dict
        :param product: Dictionary of in-memory representation of `opened snappy.Product` data product

        :type attributes: dict
        :param attributes: Dictionary of multiple products attributes

        :return:
            :products: *dict*

            Dictionary of in-memory representation of `opened snappy.Product` data product

            :attributes: *list*

            Dictionary of multiple products attributes
        """

        # Access metadata root
        product = products[0]["product"]
        metadata_root = product.getMetadataRoot()
        # product_meta = metadata_root.getElement("Manifest").getElement("metadataSection")
        #
        # > product attributes:
        # info_meta = product_meta.getElement("slstrProductInformation")
        #
        # -- spatial sampling
        #attributes['spatial_sampling_al'] = info_meta.getElement("samplingParameters") \
        #                                             .getAttributeDouble("alSpatialSampling")
        #attributes['spatial_sampling_ac'] = info_meta.getElement("samplingParameters") \
        #                                             .getAttributeDouble("acSpatialSampling")
        # -- earth_sun_distance
        # attributes['earth_sun_distance'] = int(info_meta.getAttributeString('earthSunDistance'))
        # # -- OCL status
        # attributes['ocl_status'] = bool(info_meta.getAttributeString('oclStatus'))
        #
        # # > platform meta
        # platform_meta = product_meta.getElement("platform")
        # #   -- platform
        # attributes["platform"] = platform_meta.getAttributeString("familyName") + \
        #                          platform_meta.getAttributeString("number")
        # #   -- instrument
        # attributes["instrument"] = platform_meta.getElement('Instrument') \
        #     .getElement("familyName") \
        #     .getAttributeString("abbreviation")
        #
        # # > pixel quality attributes:
        # quality_meta = info_meta.getElement("pixelQualitySummary")
        # for elem in quality_meta.getElementNames():
        #     attributes[convert_cc2sc(elem) + "_percentage"] = quality_meta.getElement(elem) \
        #         .getAttributeDouble("percentage")
        #
        # # > pixel classification attributes:
        # classification_meta = info_meta.getElement("classificationSummary")
        # for elem in classification_meta.getElementNames():
        #     attributes[convert_cc2sc(elem) + "_percentage"] = classification_meta.getElement(elem) \
        #         .getAttributeDouble("percentage")

        return products, attributes

    def getDataVariableNames(self, product):
        """
        Returns list of product "data" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product


        :return:
            :data_variable_names: *list*

            List of product "data" type variable names
        """

        product_resolution = product.getName().split("_")[-1]

        if product_resolution == "1km":
            return self.return_available_variables(product, DATA_VARIABLE_NAMES_1km)
        elif product_resolution == "500m":
            return self.return_available_variables(product, DATA_VARIABLE_NAMES_500m)
        return []

    def getMaskVariableNames(self, product):
        """
        Returns list of product "mask" type variable names

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :return:
            :mask_variable_names: *list*

            List of product "mask" type variable names
        """

        product_resolution = product.getName().split("_")[-1]

        if product_resolution == "1km":
            return self.return_available_variables(product, MASK_VARIABLE_NAMES_1km)
        elif product_resolution == "500m":
            return self.return_available_variables(product, MASK_VARIABLE_NAMES_500m)
        return []

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

        product_resolution = product.getName().split("_")[-1]

        if product_resolution == "1km":
            return self.return_available_variables(product, SENSOR_VARIABLE_NAMES_1km)
        elif product_resolution == "500m":
            return self.return_available_variables(product, SENSOR_VARIABLE_NAMES_500m)
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

        product_resolution = product.getName().split("_")[-1]

        if product_resolution == "1km":
            return self.return_available_variables(product, INFO_VARIABLE_NAMES_1km)
        elif product_resolution == "500m":
            return self.return_available_variables(product, INFO_VARIABLE_NAMES_500m)
        return []

    # def readAttributes(self, product):
    #     """
    #     Return dictionary with product attributes.
    #
    #     :type product: snappy.Product
    #     :param product: In memory representation of SLSTR L1 data product.
    #
    #     :return:
    #         :attributes: *dict*
    #         Dictionary of product attributes
    #     """
    #
    #     attributes = {}
    #
    #     # Access metadata root
    #     metadata_root = product.getMetadataRoot()
    #     product_meta = metadata_root.getElement("Manifest").getElement("metadataSection")
    #
    #     # > product attributes:
    #     info_meta = product_meta.getElement("slstrProductInformation")
    #     # -- product type string
    #     attributes["product_string"] = product.getProductType()
    #     if attributes["product_string"] != self.TYPE_STRING:
    #         raise RuntimeError("%s source product must be of type '%s' " % (self.FACTORY_STRING, self.TYPE_STRING))
    #     # -- product size
    #     # todo - what to do with different product grids in terms of product sizes
    #     # attributes["product_columns"] = info_meta.getElement("imageSize").getAttributeInt("columns")
    #     # attributes["product_rows"] = info_meta.getElement("imageSize").getAttributeDouble("rows")
    #     # -- acquisition time
    #     time_fmt = "%Y-%m-%dT%H:%M:%S.%fZ"
    #     attributes["start_time"] = dt.strptime(product_meta.getElement('acquisitionPeriod').getAttributeString('startTime'), time_fmt)
    #     attributes["end_time"] = dt.strptime(product_meta.getElement('acquisitionPeriod').getAttributeString('stopTime'), time_fmt)
    #     # -- spatial sampling
    #     # todo - what to do with different product spatial sampling in terms of product sizes
    #     # attributes['spatial_sampling_al'] = product_meta.getElement("olciProductInformation").getElement("samplingParameters").getAttributeDouble("alSpatialSampling")
    #     # attributes['spatial_sampling_ac'] = product_meta.getElement("olciProductInformation").getElement("samplingParameters").getAttributeDouble("acSpatialSampling")
    #
    #     # > platform meta
    #     platform_meta = product_meta.getElement("platform")
    #     #   -- platform
    #     attributes["platform"] = platform_meta.getAttributeString("familyName") + platform_meta.getAttributeString("number")
    #     #   -- instrument
    #     attributes["instrument"] = platform_meta.getElement('Instrument').getElement("familyName").getAttributeString("abbreviation")
    #
    #     # > band attributes:
    #     bands_meta = info_meta.getElement("bandDescriptions")
    #     #   -- band names
    #     attributes["band_names"] = [band_meta.getAttributeString('name') for band_meta in bands_meta.getElements()]
    #     #   -- band central wavelength
    #     attributes["band_central_wavelengths"] = [band_meta.getAttributeDouble('centralWavelength') for band_meta in bands_meta.getElements()]
    #     #   -- band widths
    #     attributes["band_widths"] = [band_meta.getAttributeDouble('bandWidth') for band_meta in bands_meta.getElements()]
    #
    #     # > pixel quality attributes:
    #     # todo - figure out what to do with pixel quality attributes
    #     # quality_meta = info_meta.getElement("pixelQualitySummary")
    #     # #   -- invalid pixels %
    #     # attributes["invalid_pixels_percentage"] = quality_meta.getElement("invalidPixels").getAttributeDouble("percentage")
    #     # #   -- cosmetic pixels %
    #     # attributes["cosmetic_pixels_percentage"] = quality_meta.getElement("cosmeticPixels").getAttributeDouble("percentage")
    #     # #   -- duplicated pixels %
    #     # attributes["duplicated_pixels_percentage"] = quality_meta.getElement("duplicatedPixels").getAttributeDouble("percentage")
    #     # #   -- saturated pixels %
    #     # attributes["saturated_pixels_percentage"] = quality_meta.getElement("saturatedPixels").getAttributeDouble("percentage")
    #     # #   -- dubious samples %
    #     # attributes["dubious_pixels_percentage"] = quality_meta.getElement("dubiousSamples").getAttributeDouble("percentage")
    #     #
    #     # # > pixel classification attributes:
    #     # classification_meta = info_meta.getElement("classificationSummary")
    #     # #   -- saline water pixels %
    #     # attributes["saline_water_pixels_percentage"] = classification_meta.getElement("salineWaterPixels").getAttributeDouble("percentage")
    #     # #   -- coastal pixels %
    #     # attributes["coastal_pixels_percentage"] = classification_meta.getElement("coastalPixels").getAttributeDouble("percentage")
    #     # #   -- fresh inland water pixels %
    #     # attributes["fresh_inland_water_pixels_percentage"] = classification_meta.getElement("freshInlandWaterPixels").getAttributeDouble("percentage")
    #     # #   -- tidal region pixels %
    #     # attributes["tidal_region_pixels_percentage"] = classification_meta.getElement("tidalRegionPixels").getAttributeDouble("percentage")
    #     # # -- tidal region pixels %
    #     # attributes["bright_pixels_percentage"] = classification_meta.getElement("brightPixels").getAttributeDouble("percentage")
    #
    #     return attributes

    def define_coords(self, product, variables, attributes, selected_variables):
        """
        Build `xarray.Dataset` coord dictionary from based on list of selected variables

        :type product: *snappy.Product*
        :param product: In memory representation of data product

        :type variables: list
        :param variables: list of product variables as ``Variable`` or ``SpectralVariable`` class objects.

        :type attributes: dict
        :param attributes: Dictionary of product attributes

        :type selected_variables: list
        :param selected_variables: List of requested variables

        :return:
            :coords: *dict*

            xarray.Dataset` coord dictionary

            :remaining_variables: *list*

            variables remaining from selected variables list not included in coords
        """

        coords = {}
        remaining_variables = deepcopy(selected_variables)

        # check required varis against dictionary of possible coordinate variables to see if any coords needed
        var_coords = {"lon": {"shape": ["x", "y"], "poss_names": ["longitude_an", "longitude_ao", "longitude_bn",
                                                                  "longitude_bo", "longitude_cn", "longitude_co",
                                                                  "longitude_in", "longitude_io"]},
                      "lat": {"shape": ["x", "y"], "poss_names": ["latitude_an", "latitude_ao", "latitude_bn",
                                                                  "latitude_bo", "latitude_cn", "latitude_co",
                                                                  "latitude_in", "latitude_io"]},
                      "alt": {"shape": ["x", "y"], "poss_names": ["elevation_an", "elevation_ao", "elevation_bn",
                                                                  "elevation_bo", "elevation_cn", "elevation_co",
                                                                  "elevation_in", "elevation_io"]},
                      "time_stamp": {"shape": ["x"], "poss_names": ["time_stamp"]}}

        for common_name in var_coords.keys():
            for poss_name in var_coords[common_name]["poss_names"]:
                if poss_name in selected_variables:
                    coords[common_name] = (var_coords[common_name]["shape"],
                                           self.getPixelValues(product, variables, attributes, poss_name),
                                           self.simplify_attr(self.getVariableInfo(variables, poss_name)))
                    remaining_variables.remove(poss_name)

        # If no coordinate variables required set coords to None
        if coords == {}:
            return None, remaining_variables
        return coords, remaining_variables


if __name__ == "__main__":
    pass
