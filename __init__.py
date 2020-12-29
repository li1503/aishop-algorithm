# initialize package used
from pyspark.sql import SparkSession
from pyspark import SparkContext

# main starting point
if __name__ == '__main__':
#    spark = SparkSession.builder.appName("AI-Shop-Algorithm").getOrCreate()
    sc = SparkContext("local", "")
    print("start from here")