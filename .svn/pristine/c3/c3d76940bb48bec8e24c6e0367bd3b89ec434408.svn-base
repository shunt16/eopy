"""
Subset factory for Sentinel-3 eopy.dataIO.Product objects
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from os.path import join as pjoin
from copy import deepcopy
from datetime import datetime as dt
from datetime import timedelta

'''___Third-Party Modules___'''
import snappy
from numpy import count_nonzero

'''___NPL Modules___'''
sys.path.append(pjoin(dirname(dirname(dirname(__file__))), "snappy_shared"))
from SnappySubsetFactory import SnappySubsetFactory


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "21/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.0"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class OLCIL1SubsetFactory(SnappySubsetFactory):
    """
    OLCIL1SubsetFactory is a sub-class of SnappySubsetFactory for subsetting Sentinel-3 OLCI L1
    *eopy.dataIO.Product.Product* objects

    :Methods:

        .. py:method:: updateAttributes(...):

            Returns updated ``attributes`` dictionary attribute of subsetted Sentinel *eopy.dataIO.Product.Product* data
            product

        :inherited from *eopy.dataProcessing.subset.snappy_shared.SnappySubsetFactory.SnappySubsetFactory*:

            .. py:method:: processProduct(...):

                Returns input *eopy.dataIO.Product.Product* OLCI L1 data object in units of reflectance

            .. py:method:: wktProduct(...):

                Returns region of interest subset of Sentinel *eopy.dataIO.Product.Product* ``product`` attribute, defined
                by *Well Known Text* polygon.

            .. py:method:: pixProduct(...):

                Returns region of interest subset of Sentinel *eopy.dataIO.Product.Product* ``product`` attribute, defined
                by pixel location.

            .. py:method:: updateVariables(self, product_subset, product):

                Returns updated ``variables`` dictionary attribute of subsetted Sentinel *eopy.dataIO.Product.Product* data
                product

            .. py:method:: pos2pix(...):

                Returns the pixel locations required by ``pixProduct`` method from a ``pos`` tuple defined as
                *(lon, lat, size)*

            :inherited from *eopy.dataProcessing.AbstractProcessingFactory.AbstractProcessingFactory*:

                .. py:method:: __init__():

                    Initialises the class
    """

    def updateSpecificAttributes(self, product_subset, product, **kwargs):
        """
        Returns updated ``attributes`` dictionary attribute of subsetted Sentinel *eopy.dataIO.Product.Product* data
        product

        :type product_subset: eopy.dataIO.Product.Product
        :param product_subset: subsetted data product

        :type product: eopy.dataIO.Product.Product
        :param product: original data product

        :type upper_left_x: int
        :param upper_left_x: Pixel location of the upper left corner of the region of interest in the x dimension

        :type upper_left_y: int
        :param upper_left_y: Pixel location of the upper left corner of the region of interest in the y dimension

        :type x_width: int
        :param x_width: Pixel width of the region of interest in the x dimension

        :type y_width: int
        :param y_width: Pixel width of the region of interest in the y dimension

        :type centre_x: int
        :param centre_x: Pixel location of the centre of the region of interest in the x dimension

        :type centre_y: int
        :param centre_y: Pixel location of the centre of the region of interest in the y dimension

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        new_attrs = deepcopy(product_subset.attributes)

        # Compute new pixel flag percentages
        flags = ["invalid", "cosmetic", "duplicated", "dubious", "fresh_inland_water", "bright", "tidal_region"]

        for flag in flags:
            data = product_subset.getData("quality_flags_"+flag).values
            new_attrs[flag+"_pixels_percentage"] = (float(count_nonzero(data))/float(data.size))*100.0

        # deal with saline water separately (1 -land)
        data = product_subset.getData("quality_flags_land").values
        new_attrs["saline_water_pixels_percentage"] = 100.0 - ((float(count_nonzero(data)) / float(data.size)) * 100.0)

        # todo - write update saturated pixels percentage entry
        new_attrs['saturated_pixels_percentage'] = None

        # todo - write update to coastal pixels percentage entry
        new_attrs["coastal_pixels_percentage"] = None

        return new_attrs


if __name__ == "__main__":
    pass
 

