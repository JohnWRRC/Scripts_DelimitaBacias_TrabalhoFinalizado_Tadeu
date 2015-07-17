import arcpy
from arcpy import env
#c4 var ambientais
list_c1_varamb=[]
env.workspace=r'E:\data_2015\___john\Tadeu_finlandia\sadas_grass'
rt=arcpy.ListRasters()
env.workspace=r'E:\data_2015\___john\Tadeu_finlandia\sadas_grass\vects'
#arcpy.env.extent = "569030.488466 6692716.757393 733549.645342042 6937845.5011629"
for i in rt:
    if "30m" in i:
        out=i.replace('.tif','_shp')
        print out

env.workspace=r'E:\data_2015\___john\Tadeu_finlandia\sadas_grass\vects\Basins'
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_10000_30m.tif","Mosaic_Topodata_30m_extract_tif_10000_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_5000_30m.tif","Mosaic_Topodata_30m_extract_tif_5000_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_2000_30m.tif","Mosaic_Topodata_30m_extract_tif_2000_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_1000_30m.tif","Mosaic_Topodata_30m_extract_tif_1000_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_3000_30m.tif","Mosaic_Topodata_30m_extract_tif_3000_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_0500_30m.tif","Mosaic_Topodata_30m_extract_tif_0500_30m_vect","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolygon("Mosaic_Topodata_30m_extract_tif_0250_30m.tif","Mosaic_Topodata_30m_extract_tif_0250_30m_vect","NO_SIMPLIFY","Value")

#streams
env.workspace=r'E:\data_2015\___john\Tadeu_finlandia\sadas_grass\vects\streams'
arcpy.conversion.RasterToPolyline("streams_thr_250.tif.tif","streams_thr_250_vect","NODATA","","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolyline("streams_thr_500.tif.tif","streams_thr_500_vect","NODATA","","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolyline("streams_thr_5000.tif.tif","streams_thr_5000_vect","NODATA","","NO_SIMPLIFY","Value")
arcpy.conversion.RasterToPolyline("streams_thr_10000.tif.tif","streams_thr_10000_vect","NODATA","","NO_SIMPLIFY","Value")
