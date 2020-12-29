# initialize package used
from pyspark.sql import SparkSession

# main starting point
if __name__ == '__main__':
    spark = SparkSession.builder.appName("AI-Shop-Algorithm").getOrCreate()
    print("start from here")