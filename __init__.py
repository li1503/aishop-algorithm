# initialize package used
from pyspark.sql import SparkSession
#from pyspark import SparkContext
from schema_class import Schema

# main starting point
if __name__ == '__main__':
    spark = SparkSession.builder.appName("AI-Shop-Algorithm").getOrCreate()
 #   sc = SparkContext("local", "")

    print("------------------------------------start from here------------------------------------------------")
    ini_schema = Schema()
    data_schema = ini_schema.get_schema()
    df = spark.read.csv('./src/fromdata.csv', header=True, mode="DROPMALFORMED", schema=data_schema)
    df.show()

    spark.stop()    