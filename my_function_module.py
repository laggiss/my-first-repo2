import arcpy


def get_number_fields(inFC):
    return (len(arcpy.ListFields(inFC)))
