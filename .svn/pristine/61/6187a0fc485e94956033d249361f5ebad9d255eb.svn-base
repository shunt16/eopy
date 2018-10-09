"""
Variable Class
"""

'''___Built-In Modules___'''

'''___Third-Party Modules___'''

'''___NPL Modules___'''

'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "17/07/2018"
__credits__ = ["Niall Origo"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class Variable:
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
        self.vclass = "default"
        self.units = None

        if variable_dict is not None:

            # todo - should test for valid input
            self.name = variable_dict["name"]
            self.ndims = variable_dict["ndims"]
            self.shape = variable_dict["shape"]
            self.dtype = variable_dict["dtype"]
            self.vtype = variable_dict["vtype"]
            self.units = variable_dict["units"]

    def return_variable_dict(self):
        """
        Returns dictionary of variable information

        :return:
            :variable_dict: *dict*

            dictionary of variable information
        """
        return vars(self)

    def __repr__(self):
        return 'eopy.product.productIO.'+str(self.__class__)+' "'+self.name+'"'

if __name__ == "__main__":
    pass
