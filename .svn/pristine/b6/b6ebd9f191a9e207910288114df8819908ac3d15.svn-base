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


def makeTestFactory_netCDF_with_product_string(test_factory_path):
    """
    Write test data factory

    :param test_factory_path: str
         Test factory path
    """

    className = splitext(basename(test_factory_path))[0]

    with open(test_factory_path, 'w') as f:
        f.write("""\
'''
Test product factory class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''
from netCDF4 import Dataset
from numpy import arange
import xarray as xr

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractDataFactory import AbstractDataFactory


class %s(AbstractDataFactory):

    def openProduct(self, product_path):
        product = Dataset(product_path, "r")
        self.attributes["product_string"] = "test"
        return product, self.variables, self.attributes

    def getData(self, product, variables, attributes, variable, *args):
        data = product.variables[variable][:]

        long = arange(data.shape[0])
        lat = arange(data.shape[1])
        arr = xr.DataArray(data, coords=[("longitude", long), ("latitude", lat)])
        return arr


if __name__ == "__main__":
    pass
""" %(className))

    return 0

def makeTestFactory_netCDF(test_factory_path):
    """
    Write test data factory

    :param test_factory_path: str
         Test factory path
    """

    className = splitext(basename(test_factory_path))[0]

    with open(test_factory_path, 'w') as f:
        f.write("""\
'''
Test product factory class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''
from netCDF4 import Dataset
from numpy import arange
import xarray as xr

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractDataFactory import AbstractDataFactory


class %s(AbstractDataFactory):

    def openProduct(self, product_path):
        product = Dataset(product_path, "r")
        return product, self.variables, self.attributes

    def getData(self, product, variables, attributes, variable, *args):
        data = product.variables[variable][:]

        long = arange(data.shape[0])
        lat = arange(data.shape[1])
        arr = xr.DataArray(data, coords=[("longitude", long), ("latitude", lat)])
        return arr


if __name__ == "__main__":
    pass
""" %(className))

    return 0


def makeTestFactory_xarray(test_factory_path):
    """
    Write test data factory

    :param test_factory_path: str
         Test factory path
    """

    className = splitext(basename(test_factory_path))[0]

    with open(test_factory_path, 'w') as f:
        f.write("""\
'''
Test product factory class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''
from netCDF4 import Dataset
import xarray as xr

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractDataFactory import AbstractDataFactory


class %s(AbstractDataFactory):

    def openProduct(self, product_path):
        product = xr.open_dataset(product_path)
        return product, self.variables, self.attributes

    def getData(self, product, variables, attributes, variable, *args):
        data = product[variable]
        return data


if __name__ == "__main__":
    pass
""" %(className))

    return 0


def makeTestReader(test_reader_path):
    """
    Write test data factory python script to

    :param test_reader_path: str
        Test reader path
    """

    className = splitext(basename(test_reader_path))[0]

    with open(test_reader_path, 'w') as f:
        f.write("""\
'''
Test product reader class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataIO_directory = dirname(dirname(__file__))
sys.path.append(dataIO_directory)
sys.path.append(pjoin(dataIO_directory, 'test_reader'))
from AbstractDataReader import AbstractDataReader
from TestFactory import TestFactory


class %s(AbstractDataReader):

    def setDataFactory(self, path):
        dataFactory = TestFactory
        return dataFactory


if __name__ == "__main__":
    pass
""" %(className))

    return 0


def createTestReader_netCDF(test_reader_directory):
    """
    Create test reader in specified directory which utilises netCDF4 module netcdf file reading functionality

    :param test_reader_directory:
        directory to create test reader in
    """

    test_reader_path = pjoin(test_reader_directory, "TestDataReader.py")
    test_factory_path = pjoin(test_reader_directory, "TestFactory.py")

    # Generate test data reader
    if isdir(test_reader_directory):
        shutil.rmtree(test_reader_directory)
    makedirs(test_reader_directory)

    makeTestReader(test_reader_path)
    makeTestFactory_netCDF(test_factory_path)

def createTestReader_netCDF_with_product_string(test_reader_directory):
    """
    Create test reader in specified directory which utilises netCDF4 module netcdf file reading functionality

    :param test_reader_directory:
        directory to create test reader in
    """

    test_reader_path = pjoin(test_reader_directory, "TestDataReader.py")
    test_factory_path = pjoin(test_reader_directory, "TestFactory.py")

    # Generate test data reader
    if isdir(test_reader_directory):
        shutil.rmtree(test_reader_directory)
    makedirs(test_reader_directory)

    makeTestReader(test_reader_path)
    makeTestFactory_netCDF_with_product_string(test_factory_path)


def createTestReader_xarray(test_reader_directory):
    """
    Create test reader in specified directory which utilises xarray module netcdf file reading functionality

    :param test_reader_directory:
        directory to create test reader in
    """

    test_reader_path = pjoin(test_reader_directory, "TestDataReader.py")
    test_factory_path = pjoin(test_reader_directory, "TestFactory.py")

    # Generate test data reader
    if isdir(test_reader_directory):
        shutil.rmtree(test_reader_directory)
    makedirs(test_reader_directory)

    makeTestReader(test_reader_path)
    makeTestFactory_xarray(test_factory_path)


def writeTestData(test_data_path, test_data, variable_name):
    """
    Write test data netCDF file, values array([0.0, 1.0, 2.0, 3.0, 4.0]) in variable called arange

    :param test_data_path: str
        Path to write test_path to

    :param test_data: numpy.ndarray
        Test data to write

    :param variable_name: str
        Test variable name
    """

    test_data_directory = dirname(test_data_path)

    # Generate test data
    if isdir(test_data_directory):
        shutil.rmtree(test_data_directory)
    makedirs(test_data_directory)

    # create data values
    data_size = test_data.shape[0]

    # open netCDF file
    rootgrp = Dataset(test_data_path, 'w')

    # create dimension
    x = rootgrp.createDimension('x', test_data.shape[0])
    y = rootgrp.createDimension('y', test_data.shape[1])

    # create variable
    data_var = rootgrp.createVariable(variable_name, 'f8', ('x', 'y', ))

    # store data
    data_var[:] = test_data[:]

    # close netCDF file
    rootgrp.close()

    return 0


if __name__ == "__main__":
    pass
