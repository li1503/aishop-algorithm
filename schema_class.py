from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType


class Schema:
    "This is a schema class to obtain standard schema"
    def __init__(self):
        self.schema = StructType([
        StructField("Name", StringType()),
        StructField("Region", StringType()),
        StructField("col3", StringType()), 
        StructField("col4", StringType()), 
        StructField("to_import", IntegerType()),
        StructField("to_export", IntegerType())
        ])


    def get_schema(self):
        return self.schema