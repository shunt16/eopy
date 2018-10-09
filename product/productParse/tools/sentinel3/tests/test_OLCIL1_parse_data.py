"""
Test OLCIL1 Product data for testing sentinel3_subset
For same test dataset as in eopy/dataIO/sentinel3_reader/tests/test_OLCIL1_data.py
@seh2: stored locally on my machine!
"""

'''___Built-In Modules___'''
from datetime import datetime as dt

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "DD/MM/YYYY"
__credits__ = [""]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"

OLCIL1_test_path = r"D:\Sentinel-3\OLCI\S3A_OL_1_EFR____20161023T100950_20161023T101250_20161023T120602_0179_010_122_1979_SVL_O_NR_002.SEN3\xfdumanifest.xml"

OLCIL1_test_attributes = {"product_string": "OL_1_EFR",
                          "date": dt(2016, 10, 23),
                          "start_time": dt(2016, 10, 23, 10, 9, 50),
                          "end_time": dt(2016, 10, 23, 10, 12, 50),
                          "creation_time": dt(2016, 10, 23, 12, 06, 02),
                          "mission": "Sentinel-3A",
                          "mission_type": "satellite",
                          "instrument": "OLCI"}

if __name__ == "__main__":
    pass
 

