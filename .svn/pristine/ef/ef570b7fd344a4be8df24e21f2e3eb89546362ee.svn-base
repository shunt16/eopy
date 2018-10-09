"""
Gets data processing tool appropriate for a given eopy.product.productIO.Product.Product object
"""

'''___Built-In Modules___'''
from glob import glob
from os.path import basename, splitext, abspath, basename
from os.path import join as pjoin
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


class ProductProcessingTool:
    """
    Provides functionality to return appropriate product Processing Tool for a *eopy.dataIO.Product.Product* instance
    with a specified *product_string* entry in it's attributes dictionary.

    :Methods:
        .. py:method:: setProcessingTool(...):

            Return the appropriate processing tool for a eopy.product.productIO.Product.Product object with a specified
            product_string entry in it's attributes dictionary attribute

        .. py:method:: getProcessingToolPaths(...):

            Return paths of all available processing tools for given eopy.dataProcessing.* processor
    """

    def setProcessingTool(self, processor_directory, product_string):
        """
        Return the appropriate processing tool for a *eopy.product.productIO.Product.Product* object with a specified
        product_string entry in it's attributes dictionary for a given *eopy.product.productProcessing* processor

        :type processor_directory: str
        :param processor_directory: Directory of *eopy.dataProcessing* processor package

        :type product_string: str
        :param product_string: *eopy.product.productIO.Product.Product* object "product_string" entry of its attributes dictionary

        :return:
            :ProcessingTool: *eopy.product.productProcessing.AbstractProcessingTool.AbstractProcessingTool:

            ProcessingTool for eopy.product.productIO.Product.Product object with specified "product_string"

            *If no suitable tool found returns None*
        """

        # Get paths of available tools in eopy.dataProcessing.* processor package
        processingToolPaths = self.getProcessingToolPaths(processor_directory)

        # Check if any found tools suitable for data product specified by product_string
        for processingToolPath in processingToolPaths:

            # Open specified processing tool
            processingToolName = splitext(basename(processingToolPath))[0]
            processingToolModule = imp.load_source(processingToolName, processingToolPath)
            ProcessingTool = getattr(processingToolModule, processingToolName)

            # Test to find if process tool can find appropriate processing factory
            testProcessingTool = ProcessingTool()
            testProcessingFactory = testProcessingTool.setProcessingFactory(product_string)

            # If test instantiation of processing tool can find appropriate processing factory return processing tool
            if testProcessingFactory is not None:
                return ProcessingTool

        return None

    def getProcessingToolPaths(self, processor_directory):
        """
        Return paths of all available in processing tools in *eopy.dataProcessing* processor package

        :type processor_directory: str
        :param processor_directory: Directory of processor package

        :return:
            :processingToolPaths: *list:str*

            List of all available in processing tools in *eopy.dataProcessing* processor package
        """

        # Initialise list for p
        processingToolPaths = []

        # Search eopy.dataProcessing.* processor package for processing tools
        for tool_directory in glob(abspath(processor_directory + "/tools/*/")):
            if ("__init__" not in basename(tool_directory)) and (basename(tool_directory) != "__pycache__")\
                    and (glob(pjoin(tool_directory, "*Tool.py")) != []):
                processingToolPaths.append(abspath(glob(pjoin(tool_directory, "*Tool.py"))[0]))

        return processingToolPaths


if __name__ == "__main__":
    pass
 

