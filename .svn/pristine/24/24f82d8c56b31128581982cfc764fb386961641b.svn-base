"""
Functions to generate test product processing tool, that returns input product
"""

'''___Built-In Modules___'''
import sys
from os import makedirs
from os.path import dirname, basename, splitext, isdir
from os.path import join as pjoin
import shutil

'''___Third-Party Modules___'''


'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "25/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


def makeTestProcessingFactory(test_processing_factory_path):
    """
    Write test processing factory python script

    :param test_processing_factory_path: str
        Test processing factory path
    """

    className = splitext(basename(test_processing_factory_path))[0]

    with open(test_processing_factory_path, 'w') as f:
        f.write("""\
'''
Test processing factory class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(dataProcessing_directory)
from AbstractProcessingFactory import AbstractProcessingFactory


class %s(AbstractProcessingFactory):

    def processProduct(self, product, **kwargs):
        return product


if __name__ == "__main__":
    pass
""" % (className))

    return 0


def makeTestProcessingTool(test_processing_tool_path, test_processing_factory_path):
    """
    Write test processing tool python script

    :param test_processing_tool_path: str
        Test processing tool path

    :param test_processing_factory_path: str
        Test processing factory path
    """

    className = splitext(basename(test_processing_tool_path))[0]
    factory_name = splitext(basename(test_processing_factory_path))[0]

    with open(test_processing_tool_path, 'w') as f:
        f.write("""\
'''
Test processing tool class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(dirname(dirname(__file__))))
sys.path.append(dataProcessing_directory)
from AbstractProcessingTool import AbstractProcessingTool

sys.path.append(dirname(__file__))
from %s import %s


class %s(AbstractProcessingTool):

    def setProcessingFactory(self, product_string):
        processingFactory = %s
        return processingFactory


if __name__ == "__main__":
    pass
""" % (factory_name, factory_name, className, factory_name))

    return 0


def makeTestProcessor(test_processor_path):
    """
    Write test processor python script

    :param test_processor_path: str
        Test processor path

    """

    className = splitext(basename(test_processor_path))[0]

    with open(test_processor_path, 'w') as f:
        f.write("""\
'''
Test processor class - should be deleted upon completion of test
'''

'''___Built-In Modules___'''
import sys
from os.path import dirname

'''___Third-Party Modules___'''

'''___NPL Modules___'''
dataProcessing_directory = dirname(dirname(__file__))
sys.path.append(dataProcessing_directory)
from AbstractProcessor import AbstractProcessor

class %s(AbstractProcessor):
    processor_directory = dirname(__file__)


if __name__ == "__main__":
    pass
""" % (className))

    return 0


def createTestProcessor(test_processor_directory):
    """
    Create test processor in specified directory

    :param test_proessor_directory:
        directory to create test processor in
    """

    test_processor_path = pjoin(test_processor_directory, "TestProcessor.py")
    test_processor_tool_directory = pjoin(test_processor_directory, "tools", "test")
    test_processing_tool_path = pjoin(test_processor_tool_directory, "TestProcessingTool.py")
    test_processing_factory_path = pjoin(test_processor_tool_directory, "TestProcessingFactory.py")

    # Generate test data reader
    if isdir(test_processor_directory):
        shutil.rmtree(test_processor_directory)
    makedirs(test_processor_tool_directory)

    makeTestProcessor(test_processor_path)
    makeTestProcessingTool(test_processing_tool_path, test_processing_factory_path)
    makeTestProcessingFactory(test_processing_factory_path)


if __name__ == "__main__":
    createTestProcessor(pjoin(dirname(dirname(__file__)), "testProcessor"))
