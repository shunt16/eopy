"""
Gets product reader appropriate for a given data product
"""

'''___Built-In Modules___'''
from glob import glob
from os.path import basename, dirname, splitext, abspath
from os.path import join as pjoin
import imp

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "05/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class ProductDataReader:
    """
    Provides functionality to return appropriate product reader for a data product at a specified file path

    :Methods:
        .. py:method:: setDataReader(...):

            Return the appropriate data reader for a data product at a specified file path

        .. py:method:: getDataReaderPaths(...):

            Return paths of all available data readers in *eopy.dataIO* package
    """

    def setDataReader(self, product_path):
        """
        Return the appropriate data reader for a data product at a specified file path

        :type product_path: str
        :param product_path: The data product file path

        :return:
            :DataReader: *eopy.dataIO.AbstractDataReader.AbstractDataReader*

            Product Data reader
        """

        # Get paths of available product readers in eopy.dataIO package
        dataReaderPaths = self.getDataReaderPaths()

        # Check if any found product readers suitable for data product specified by product_path
        for dataReaderPath in dataReaderPaths:

            # Open specified product reader
            dataReaderName = splitext(basename(dataReaderPath))[0]
            dataReaderModule = imp.load_source(dataReaderName, dataReaderPath)
            dataReader = getattr(dataReaderModule, dataReaderName)

            # Test to find if product reader can find appropriate product factory
            testDataReader = dataReader()
            testProductFactory = testDataReader.setDataFactory(product_path)

            # If test instantiation of product reader can find appropriate product factory return data reader
            if testProductFactory is not None:
                return dataReader

        return None

    def getDataReaderPaths(self):
        """
        Return paths of all available data readers in eopy.dataIO package

        :return:
            :dataReaderPaths: *list:str*

            List of all available data readers in eopy.dataIO package
        """

        # Full path of eco-core.dataIO package
        productIO_path = dirname(__file__)

        # Initialise list for p
        dataReaderPaths = []

        # Search dataIO for DataReaders
        for folder in glob(productIO_path + "/*/"):
            if ("_reader" in folder) and (glob(pjoin(folder, "*DataReader.py")) != []):
                dataReaderPaths.append(abspath(glob(pjoin(folder, "*DataReader.py"))[0]))

        return dataReaderPaths


if __name__ == "__main__":
    pass
