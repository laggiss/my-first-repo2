import arcpy
from arcpy import env
import my_function_module
env.workspace=r"(C:\Users\msawada\Downloads\Lecture7_Data\Module7_Data\OTTAWA.gdb\OTTAWADATA)"
featureclass_list=arcpy.ListFeatureClasses()
fieldnumbervector=[]
for fc in featureclass_list:
     fieldnumbervector.append(my_function_module.get_number_fields(fc))