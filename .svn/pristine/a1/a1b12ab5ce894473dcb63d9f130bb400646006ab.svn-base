"""
Variable Class
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''
from Variable import Variable

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/07/2018"
__credits__ = ["Niall Origo"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class SpectralVariable(Variable):
    """
    Variable instances contain information about data product variables

    :Attributes:
        .. py:attribute:: name

            *str*

            Variable name

        .. py:attribute:: ndims

            *int*

            Number of dimensions of variable data array

        .. py:attribute:: shape

            *tuple*

            Shape of variable data array

        .. py:attribute:: dtype

            *str*

            Data type of variable data array (i.e. int16, float32)

        .. py:attribute:: vtype

            *str*

            type of variable, can have values:

            * "data"
            * "mask"
            * "meteorological"

        .. py:attribute:: units

            *pint*

            unit of variable
    """

    def __init__(self, variable_dict=None):

        self.name = None
        self.ndims = None
        self.shape = None
        self.dtype = None
        self.vtype = None
        self.vclass = "spectral"
        self.units = None
        self.wavelength = None
        self.bandwidth = None
        self.srf = None

        if variable_dict is not None:

            # todo - should test for valid input
            self.name = variable_dict["name"]
            self.ndims = variable_dict["ndims"]
            self.shape = variable_dict["shape"]
            self.dtype = variable_dict["dtype"]
            self.vtype = variable_dict["vtype"]
            self.units = variable_dict["units"]
            self.wavelength = variable_dict["wavelength"]
            self.bandwidth = variable_dict["bandwidth"]
            self.srf = variable_dict["srf"]

    def add_srf(self, srf_path):
        # todo - write method for opening SpectralVariable srf as xarray
        pass


if __name__ == "__main__":
    pass
