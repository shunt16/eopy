"""
Functions to generate test data and reader
"""

'''___Built-In Modules___'''
import sys
from os import makedirs
from os.path import dirname, basename, splitext, isdir
from os.path import join as pjoin
import shutil

'''___Third-Party Modules___'''
from netCDF4 import Dataset

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "09/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


def makeTestParsingFactory(test_factory_path):
    """
    Write test data factory

    :param test_factory_path: str
         Test factory path
    """

    className = splitext(basename(test_factory_path))[0]

    with open(test_factory_path, 'w') as f:
        f.write("""\
'''
Test product parsing factory class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataParsingTool_directory = dirname(dirname(dirname(__file__)))
sys.path.append(dataParsingTool_directory)
from AbstractParsingFactory import AbstractParsingFactory


class %s(AbstractParsingFactory):

    def parseProduct(self, product_path, detail, **kwargs):
        attributes = {}
        return attributes


if __name__ == "__main__":
    pass
""" %(className))

    return 0


def makeTestParsingTool(test_reader_path):
    """
    Write test data factory python script to

    :param test_reader_path: str
        Test reader path
    """

    className = splitext(basename(test_reader_path))[0]

    with open(test_reader_path, 'w') as f:
        f.write("""\
'''
Test product parsing tool class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
sys.path.append(dirname(__file__))
from TestParsingFactory import TestParsingFactory

dataParsingTool_directory = dirname(dirname(dirname(__file__)))
sys.path.append(dataParsingTool_directory)
from AbstractParsingTool import AbstractParsingTool


class %s(AbstractParsingTool):

    def setParsingFactory(self, path):
        parsingFactory = TestParsingFactory
        return parsingFactory


if __name__ == "__main__":
    pass
""" %(className))

    return 0


def createTestParsingTool(test_parser_directory):
    """
    Create test reader in specified directory which utilises netCDF4 module netcdf file reading functionality

    :param test_parser_directory:
        directory to create test parser in
    """

    test_parsing_tool_path = pjoin(test_parser_directory, "TestParsingTool.py")
    test_parsing_factory_path = pjoin(test_parser_directory, "TestParsingFactory.py")

    # Generate test parser
    if isdir(test_parser_directory):
        shutil.rmtree(test_parser_directory)
    makedirs(test_parser_directory)

    makeTestParsingTool(test_parsing_tool_path)
    makeTestParsingFactory(test_parsing_factory_path)



if __name__ == "__main__":
    pass
