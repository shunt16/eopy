"""
Gets data processing tool appropriate for a given eopy.dataIO.Product.Product object
"""

'''___Built-In Modules___'''
from glob import glob
from os.path import basename, splitext, abspath, dirname
import imp

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class ProductParsingTool:
    """
    Provides functionality to return appropriate product parsing Tool for a for a product data with a specified
    ``product_path``

    :Methods:
        ..py:method:: setProcessingTool(...):

            Return the appropriate parsing tool for a product data with a specified ``product_path``

        ..py:method:: getProcessingToolPaths(...):

            Return paths of all available in parsing tools in *eopy.dataParsing* package
    """

    def setParsingTool(self, product_path):
        """
        Return the appropriate parsing tool for a product data with a specified ``product_path``

        :type product_path: str
        :param product_path: The data product path

        :return:
            :ParsingTool: *eopy.dataProcessing.AbstractParsingTool.AbstractParsingTool*

            ProcessingTool for eopy.dataIO.Product object with specified "product_path"

            *If no suitable tool found returns None*
        """

        # Get paths of available parsing tools in eopy.dataParse package
        parsingToolPaths = self.getParsingToolPaths()

        # Check if any found tools suitable for data product specified by product_path
        for parsingToolPath in parsingToolPaths:

            # Open specified parsing tool
            parsingToolName = splitext(basename(parsingToolPath))[0]
            parsingToolModule = imp.load_source(parsingToolName, parsingToolPath)
            ParsingTool = getattr(parsingToolModule, parsingToolName)

            # Test to find if parsing tool can find appropriate parsing factory
            testParsingTool = ParsingTool()
            testParsingFactory = testParsingTool.setParsingFactory(product_path)

            # If test instantiation of parsing tool can find appropriate parsing factory return parsing tool
            if testParsingFactory is not None:
                return ParsingTool

        return None

    def getParsingToolPaths(self):
        """
        Return paths of all available in parsing tools in *eopy.dataParsing* package

        :return:
            :parsingToolPaths: *list:str*

            List of all available in parsing tools in *eopy.dataParsing* package
        """

        # Full path of eco-core.dataIO package
        dataParsing_path = dirname(__file__)

        # Initialise list for parsing tools
        parsingToolPaths = []

        # Search eopy.dataProcessing.* processor package for processing tools
        for tool_directory in glob(abspath(dataParsing_path + "/tools/*/")):
            if (basename(tool_directory) != "__init__") and (basename(tool_directory) != "__pycache__"):
                parsingToolPaths.append(abspath(glob(tool_directory + "/*Tool.py")[0]))

        return parsingToolPaths


if __name__ == "__main__":
    pass
 

