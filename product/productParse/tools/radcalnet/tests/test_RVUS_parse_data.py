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

RVUS_test_path = r"D:\RVUS00_2015_320_v00.00.output"

RVUS_test_attributes = {"product_string": "RVUS",
                        "date": dt(2015, 11, 16),
                        "mission": "radcalnet",
                        "mission_type": "ground",
                        "site": "RVUS",
                        "site_config": "00"}

if __name__ == "__main__":
    pass
 

