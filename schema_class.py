from pyspark.sql.types import StructType, StructField
from pyspark.sql.types import DoubleType, IntegerType, StringType


class Schema:
    "This is a schema class to obtain standard schema"
    def __init__(self):
        self.schema = StructType([
        StructField("Name", StringType()),
        StructField("Region", StringType()),
        StructField("C", StringType()), 
        StructField("D", StringType()), 
        StructField("to import", IntegerType()),
        StructField("to export", IntegerType())
        ])


    def get_schema(self):
        return self.schema