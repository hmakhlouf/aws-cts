# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc, avg, count

spark = SparkSession.builder.appName("Top10Movies-PySpark").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

moviesFile = "s3n://iquiz.datasets/movielens/movies.csv"
ratingsFile = "s3n://iquiz.datasets/movielens/ratings.csv"

movieDF = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(moviesFile)
            
ratingsDF = spark.read \
            .option("header", "true") \
            .option("inferSchema", "true") \
            .csv(ratingsFile)
                        
movieDF.show()
ratingsDF.show()

ratingsSummaryDf = ratingsDF.groupBy("movieId") \
                    .agg( count("rating").alias("totalRatings"),
                          avg("rating").alias("averageRating") 
                        ) \
                    .where("totalRatings >= 25") \
                    .orderBy(desc("averageRating")) \
                    .limit(20)

ratingsSummaryDf.show(20)

joinCol = ratingsSummaryDf["movieId"] == movieDF["movieId"]

output = ratingsSummaryDf.join(movieDF, joinCol) \
            .drop(movieDF["movieId"]) \
            .select("movieId", "title", "totalRatings", "averageRating") \
            .orderBy(desc("averageRating")) \
            .coalesce(1)

output.show()