"""
Subset factory for *eopy.product.productIO.Product.Product* objects which contain instantiations of snappy products
"""

'''___Built-In Modules___'''
import sys
from os.path import dirname
from copy import deepcopy
import re
from datetime import datetime as dt

'''___Third-Party Modules___'''
import snappy
from PIL import Image, ImageDraw
import shapely.geometry
from numpy import linspace, bool_, array
import geog
from geopy.distance import geodesic

'''___NPL Modules___'''
sys.path.append(dirname(dirname(__file__)))
from AbstractProcessingFactory import AbstractProcessingFactory

from eopy import Product


'''___Authorship___'''
__author__ = "Sam Hunt"
__created__ = "23/06/2017"
__credits__ = ["Andrew Banks", "Javier Gorrono", "Niall Origo", "Tracy Scanlon"]
__version__ = "0.1"
__maintainer__ = "Sam Hunt"
__email__ = "sam.hunt@npl.co.uk"
__status__ = "Development"


class SnappySubsetFactory(AbstractProcessingFactory):
    """
    SnappySubsetFactory is a sub-class of *AbstractProcessingFactory* for subsetting Sentinel
     *eopy.dataIO.Product.Product*.

    :Methods:
        .. py:method:: processProduct(...):

            Returns subset of input *eopy.product.productIO.Product.Product* object, type of subset defined by kwargs.

        .. py:method:: wktProduct(...):

            Returns region of interest subset of `snappy.Product` object, defined by *Well Known Text* polygon.

        .. py:method:: pixProduct(...):

            Returns region of interest subset of `snappy.Product` object, defined in pixels.

        .. py:method:: updateAttributes(...):

            Returns updated ``attributes`` attribute of subsetted *eopy.product.productIO.Product.Product* project

        .. py:method:: updateVariables(self, product_subset, product):

            Returns updated ``variables`` attribute of subsetted *eopy.product.productIO.Product.Product* product

        .. py:method:: wkt2pixs(...):

            Returns the location of the upper left corner, height and width of the box containing the region defined by
            WKT with a mask cutting out the region within

        .. py:method:: pos2pixs(...):

            Returns the location of the upper left corner, height and width of the box containing the square region,
            size L m, region of interest centred on lon lat

        .. py:method:: pos2wkt(...):

            Return Well Known Text representation of region defined by 'pos' tuple

        .. py:method:: wkt2latlons(...):

            Return lats and lons from Well Known Text representation of region

        .. py:method:: latlon2pix(...):

            Return pixel indices of point in product given lat, lon

        .. py:method:: pix2latlon(...):

            Return lat lon of point in product given by pixel indices

        .. py:method:: return_spatial_sampling(...):

            Return pixel sampling around pixel at given index

        :inherited from eopy.product.productProcessing.AbstractProcessingFactory.AbstractProcessingFactory:

            .. py:method:: __init__():

                Initialises the class
    """

    def processProduct(self, product, **kwargs):
        """
        Returns subset of input *eopy.product.productIO.Product.Product* object, type of subset defined by kwargs.

        :type product: eopy.product.productIO.Product.Product
        :param product: Data product to process

        Keyword arguments define subset:

        :type pos: tuple
        :param pos: Definition of square, size L m, region of interest centre on lon lat - define as (lon, lat, L)

        :type wkt: str
        :param wkt: Definition of region of interest in Well Known Text

        :type shape: `shapely.geometry.Polygon`
        :param shape: Definition of region of interest of `shapely.geometry.Polygon`

        :return:
            :product_processed: *eopy.product.productIO.Product.Product*

            Processed data product
        """

        # Initialise subset empty subset product
        product_subset = Product()
        product_subset.dataReader = deepcopy(product.dataReader)

        # Populate product_subset object attribute by attribute
        product_subset.product = []
        for p in product.product:
            product_subset.product.append({"product_name": p["product_name"], "variables": p["variables"]})

        ################################################################################################################
        # 1. Process product
        ################################################################################################################

        # Process depending on subset definition in kwargs

        # a. "pos"
        if "pos" in kwargs:
            pos = kwargs['pos']

            # Process per product in product.product - will typically be one, in the simple case unless product opened
            # in different spatial resolutions (e.g. for Sentinel-2 products)
            for i, p in enumerate(product.product):

                # Determine the location of the upper left corner, height and width of the box
                upper_left_x, upper_left_y, x_width, y_width, centre_x, centre_y = self.pos2pixs(p["product"], pos)

                # Subset based on pixel geometries found
                product_subset.product[i]["product"] = self.pixProduct(p["product"],
                                                                       upper_left_x, upper_left_y,
                                                                       x_width, y_width)

            processing_parameter = {"pos": str(pos)}

        # b. "wkt" or "shape"
        elif ("wkt" in kwargs) or ("shape" in kwargs):

            # If defined by either shape.geometry.Polygon or WKT string process as WKT
            wkt = kwargs["shape"].wkt if "shape" in kwargs else kwargs['wkt']

            # Process per product in product.product - will typically be one, in the simple case unless product opened
            # in different spatial resolutions (e.g. for Sentinel-2 products)

            product_subset.dataReader.dataFactory.data_mask = [None] * len(product.product)

            for i, p in enumerate(product.product):

                # self.wkt2pix() finds the location of the upper left corner, height and width of the box containing
                # the region defined by WKT with a mask cutting out the region within
                upper_left_x, upper_left_y, x_width, y_width, centre_x, \
                        centre_y, subset_mask = self.wkt2pixs(p["product"], wkt)

                # Subset containing box of product and apply region of interest mask
                product_subset.product[i]["product"] = self.pixProduct(p["product"],
                                                                       upper_left_x, upper_left_y,
                                                                       x_width, y_width)
                product_subset.dataReader.dataFactory.data_mask = subset_mask

            processing_parameter = {"wkt": wkt}

        else:
            raise ValueError("No valid Subset specification keyword in kwargs")

        ################################################################################################################
        # 2. Update attributes attributes and variables
        ################################################################################################################

        product_subset.variables = self.updateVariables(product_subset, product)

        # Update common snappy product attributes
        product_subset.attributes = self.updateCommonAttributes(product_subset, product)

        # Update processing log
        product_subset.attributes = self.updateAttributesProcessingLog(product_subset, "subset", processing_parameter)

        # Update product specific attributes - should be updated in product specific sub-classes
        product_subset.attributes = self.updateSpecificAttributes(product_subset, product)

        return product_subset

    def wktProduct(self, product, wkt):
        """
        Returns region of interest subset of `snappy.Product` object, defined by *Well Known Text* polygon.

        :type product: snappy.Product
        :param product: In memory representation of data product

        :type wkt: str
        :param wkt: Region of interest polygon in WKT format

        :return:
            :product_subset: *snappy.Product*

            In memory representation of data product subsetted
        """

        # Get require SNAP tools
        SubsetOp = snappy.jpy.get_type('org.esa.snap.core.gpf.common.SubsetOp')
        WKTReader = snappy.jpy.get_type('com.vividsolutions.jts.io.WKTReader')

        # Define ROI
        try:
            geometry = WKTReader().read(wkt)
        except:
            raise RuntimeError('WKT Error: Failed to convert WKT into geometry')

        # Extract ROI
        op = SubsetOp()
        op.setSourceProduct(product)
        op.setGeoRegion(geometry)

        try:
            product_subset = op.getTargetProduct()
        except:
            raise RuntimeError('ROI Error: Unable to extract specified region of interest from input product')

        return product_subset

    def pixProduct(self, product, upper_left_x, upper_left_y, x_width, y_width):
        """
        Returns region of interest subset of `snappy.Product` object, defined in pixels

        :type product: snappy.Product
        :param product: In memory representation of data product

        :type upper_left_x: int
        :param upper_left_x: Pixel location of the upper left corner of the region of interest in the x dimension

        :type upper_left_y: int
        :param upper_left_y: Pixel location of the upper left corner of the region of interest in the y dimension

        :type x_width: int
        :param x_width: Pixel width of the region of interest in the x dimension

        :type y_width: int
        :param y_width: Pixel width of the region of interest in the y dimension

        :return:
            :product_subset: *snappy.Product*

            In memory representation of data product subsetted
        """

        # Get require SNAP tools
        SubsetOp = snappy.jpy.get_type('org.esa.snap.core.gpf.common.SubsetOp')

        # Extract ROI
        op = SubsetOp()
        op.setSourceProduct(product)
        op.setRegion(snappy.Rectangle(upper_left_x, upper_left_y, x_width, y_width))

        try:
            product_subset = op.getTargetProduct()
        except:
            raise RuntimeError('ROI Error: Unable to extract specified region of interest from input product')

        return product_subset

    def updateCommonAttributes(self, product_subset, product):
        """
        Returns updated ``attributes`` attribute of subsetted *eopy.product.productIO.Product.Product* product for
        attributes common to all snappy products

        :type product_subset: `eopy.product.productIO.Product.Product`
        :param product_subset: subsetted data product

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        # Duplicate original
        new_attrs = deepcopy(product.attributes)

        # Get new dimensions
        products = product_subset.product
        if len(products) > 1:
            for p in products:
                new_attrs["product_processing_" + p["product_name"]] = []
                new_attrs["product_columns_" + p["product_name"]] = p["product"].getSceneRasterWidth()
                new_attrs["product_rows_" + p["product_name"]] = p["product"].getSceneRasterHeight()
        else:
            new_attrs["product_processing"] = []
            new_attrs["product_columns"] = products[0]["product"].getSceneRasterWidth()
            new_attrs["product_rows"] = products[0]["product"].getSceneRasterHeight()

        # Update start and end time if possible/needed
        if "time_stamp" in product_subset.getVariableNames():

            original_start_time = product.attributes["start_time"]
            original_end_time = product.attributes["end_time"]

            original_product_rows = product.product[0]["product"].getSceneRasterHeight()
            subset_product_rows = product_subset.product[0]["product"].getSceneRasterHeight()

            row_time = (original_end_time - original_start_time) / (original_product_rows - 1)

            i_start = product_subset.product[0]["product"].getMetadataRoot().getElement("history") \
                                                          .getElement("SubsetInfo").getAttributeInt("SubRegion.y") - 1
            i_end = i_start + subset_product_rows

            new_attrs["start_time"] = original_start_time + i_start * row_time
            new_attrs["end_time"] = original_start_time + i_end * row_time

        return new_attrs

    def updateAttributesProcessingLog(self, product_processed, processing_name, processing_parameter):
        """
        Returns ``attributes`` attribute of processed *eopy.product.productIO.Product.Product* product with updated
        "product_processing" log entry

        :type product_processed: `eopy.product.productIO.Product.Product`
        :param product_processed: processed data product

        :type processing_name: str
        :param processing_name: name of processing

        :type processing_parameter: dict
        :param processing_parameter: processing parameter, to describe processing

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        # Duplicate original
        new_attrs = deepcopy(product_processed.attributes)

        if len(product_processed.product) > 1:
            # Attach log of processing
            for p in product_processed.product:
                new_attrs["product_processing_" + p["product_name"]].append({"processing_name": processing_name,
                                                                             "processing_parameters":
                                                                                            processing_parameter})
        else:
            new_attrs["product_processing"].append({"processing_name": processing_name,
                                                    "processing_parameters": processing_parameter})

        return new_attrs

    def updateSpecificAttributes(self, product_subset, product):
        """
        Returns updated ``attributes`` attribute of subsetted *eopy.product.productIO.Product.Product* product for
        product specific attributes, to be overridden in subclasses

        :type product_subset: `eopy.product.productIO.Product.Product`
        :param product_subset: subsetted data product

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_attrs: *dict*

            Updated attributes dictionary
        """

        return product_subset.attributes

    def updateVariables(self, product_subset, product):
        """
        Returns updated ``variables`` attribute of subsetted *eopy.product.productIO.Product.Product* product

        :type product_subset: `eopy.product.productIO.Product.Product`
        :param product_subset: subsetted data product

        :type product: `eopy.product.productIO.Product.Product`
        :param product: original data product

        :return:
            :new_vars: *dict*

            Updated variables dictionary
        """

        # todo - should update variable dimensions

        return deepcopy(product.variables)

    def wkt2pixs(self, product, wkt):
        """
        Returns the location of the upper left corner, height and width of the box containing the region defined by
        WKT with a mask cutting out the region within

        :type product: *snappy.Product*
        :param product: data product

        :type wkt: float
        :param wkt: Well Known Text definition of region of interest

        :return:
            :upper_left_x: *int*

            Pixel location of the upper left corner of the region of interest in the x dimension

            :upper_left_y: *int*

            Pixel location of the upper left corner of the region of interest in the y dimension

            :x_width: *int*

            Pixel width of the region of interest in the x dimension

            :y_width: *int*

            Pixel width of the region of interest in the y dimension

            :subset_mask: *numpy.ndarray*

            Mask of region of interest inside bounding box
        """

        lats, lons = self.wkt2latlons(wkt)
        xys = [self.latlon2pix(product, lat, lon) for lat, lon in zip(lats, lons)]
        xs = [xy[0] for xy in xys]
        ys = [xy[1] for xy in xys]

        upper_left_x = int(min(xs))
        upper_left_y = int(min(ys))
        x_width = int(max(xs) - min(xs))+1
        y_width = int(max(ys) - min(ys))+1
        centre_x = int(upper_left_x+(float(x_width)/2.0))
        centre_y = int(upper_left_y+(float(y_width)/2.0))

        # Determine mask
        polygon = [(x-upper_left_x, y-upper_left_y) for x, y in zip(xs, ys)]
        img = Image.new('L', (x_width, y_width), 0)
        ImageDraw.Draw(img).polygon(polygon, outline=1, fill=1)
        subset_mask = array(img, bool_)

        return upper_left_x, upper_left_y, x_width, y_width, centre_x, centre_y, subset_mask

    def pos2pixs(self, product, pos):
        """
        Returns the location of the upper left corner, height and width of the box containing the square region,
        size L m, region of interest centred on lon lat

        :type product: snappy.Product
        :param product: data product

        :type pos: tuple
        :param pos: Definition of square region, size L m, region of interest centred on lon lat (lon, lat, L)

        :return:
            :upper_left_x: *int*

            Pixel location of the upper left corner of the region of interest in the x dimension

            :upper_left_y: *int*

            Pixel location of the upper left corner of the region of interest in the y dimension

            :x_width: *int*

            Pixel width of the region of interest in the x dimension

            :y_width: *int*

            Pixel width of the region of interest in the y dimension

            :centre_x: *int*

            Pixel location of the centre of the region of interest in the x dimension

            :centre_y: *int*

            Pixel location of the centre of the region of interest in the y dimension
        """

        # Unpack parameters
        lon = pos[0]
        lat = pos[1]
        size = pos[2]

        # 1. Find pixel position of lon, lat
        x_centre, y_centre = self.latlon2pix(product, lat, lon)

        # 2. Find pixel position of the corners of the roi
        # determine spatial sample in x and y direction around the centre based on lat lon of pixels in that region

        spatial_sampling_ac, spatial_sampling_al = self.return_spatial_sampling(product, x_centre, y_centre)

        n_xpixels = int(float(size) / 2.0 / spatial_sampling_ac)
        n_ypixels = int(float(size) / 2.0 / spatial_sampling_al)

        # Find pixel positions of corners
        x_corners = [x_centre-n_xpixels, x_centre+n_xpixels, x_centre+n_xpixels, x_centre-n_xpixels]
        y_corners = [y_centre-n_ypixels, y_centre-n_ypixels, y_centre+n_ypixels, y_centre+n_ypixels]

        # Return parameters
        upper_left_x = int(x_corners[0])
        upper_left_y = int(y_corners[0])
        x_width = int(x_corners[1] - x_corners[0]) + 1
        y_width = int(y_corners[2] - y_corners[1]) + 1

        return upper_left_x, upper_left_y, x_width, y_width, int(x_centre), int(y_centre)

    def wkt2latlons(self, wkt):
        """
        Return lats and lons from Well Known Text representation of region

        :type wkt: str
        :param wkt:

        :return:
            :lats: *list*

            List of latitudes

            :lons: *list*

            List of longitudes
        """

        nums = re.findall(r'-?\d+(?:\.\d*)?', wkt.rpartition(',')[0])

        lonlats = zip(*[iter(nums)] * 2)

        lons = [float(p[0]) for p in lonlats]
        lats = [float(p[1]) for p in lonlats]

        return lats, lons

    def pos2wkt(self, pos):
        """
        Return Well Known Text representation of region defined by "pos" tuple

        :type pos: tuple
        :param pos: Definition of square region, size L m, region of interest centred on lon lat (lon, lat, L)

        :return:
            :wkt: *str*

            Well known text representation of pos
        """

        # Unpack parameters
        lon = pos[0]
        lat = pos[1]
        size = pos[2]

        centre = shapely.geometry.Point([lat, lon])
        angles = linspace(0, 360, 5) + 45.0
        polygon = geog.propagate(centre, angles, (size**2/2.0)**0.5)

        return shapely.geometry.Polygon(polygon).wkt

    def latlon2pix(self, product, lat, lon):
        """
        Return pixel indices of point in product given lat, lon

        :type product: *snappy.Product*
        :param product: data product

        :type lat: float
        :param lat: latitude of point

        :type lon: float
        :param lon: longitude of point

        :return:
            :x: *int*

            x index of point

            :y: *int*

            y index of point
        """

        geo_pos = snappy.GeoPos()
        geo_pos.lon = lon
        geo_pos.lat = lat
        pix_pos = snappy.PixelPos()
        geo_code = product.getBand(list(product.getBandNames())[0]).getGeoCoding()
        geo_code.getPixelPos(geo_pos, pix_pos)

        x = pix_pos.getX()
        y = pix_pos.getY()

        return x, y

    def pix2latlon(self, product, x, y):
        """
        Return lat lon of point in product given by pixel indices

        :type product: *snappy.Product*
        :param product: data product

        :type x: int
        :param x: x index of point

        :type y: float
        :param y: y index of point

        :return:
            :lat: *float*

            latitude of point

            :lon: *int*

            longitude of point
        """

        pix_pos = snappy.PixelPos()
        pix_pos.x = x
        pix_pos.y = y

        geo_pos = snappy.GeoPos()
        geo_code = product.getBand(list(product.getBandNames())[0]).getGeoCoding()
        geo_code.getGeoPos(pix_pos, geo_pos)

        lat = geo_pos.lat
        lon = geo_pos.lon

        return lat, lon

    def return_spatial_sampling(self, product, x_i, y_i):
        """
        Return pixel sampling around pixel at given index

        :type product: *snappy.Product*
        :param product: data product

        :type x_i: int
        :param x_i: x pixel index

        :type y_i: int
        :param y_i: y pixel index

        :return:
            :x_sampling: *float*

            spatial sampling in x direction in metres

            :y_sampling: *float*

            spatial sampling in y direction in metres
        """

        point = self.pix2latlon(product, x_i, y_i)
        point_xoffset = self.pix2latlon(product, x_i + 1, y_i)
        point_yoffset = self.pix2latlon(product, x_i, y_i + 1)

        x_sampling = geodesic(point, point_xoffset).m
        y_sampling = geodesic(point, point_yoffset).m

        return x_sampling, y_sampling


if __name__ == "__main__":
    pass
 

