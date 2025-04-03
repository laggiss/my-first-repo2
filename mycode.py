import arcpy
from arcpy import env
env.workspace=r"(C:\Users\msawada\Downloads\Lecture7_Data\Module7_Data\OTTAWA.gdb\OTTAWADATA)"
featureclass_list=arcpy.ListFeatureClasses()