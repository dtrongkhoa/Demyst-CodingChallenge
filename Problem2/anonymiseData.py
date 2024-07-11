from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

# A Spark Job to anonymise data 
def anonymize_data(input_path, output_path):
    # Generate a Spark Session name "Anonymize Data"
    spark = SparkSession.builder.appName("Anonymise Data").getOrCreate()

    # Read the CSV file
    df = spark.read.csv(input_path, header=True)

    # Anonymize the data
    anonymised_df = df.withColumn("first_name", lit("ANONYMISED")) \
                      .withColumn("last_name", lit("ANONYMISED")) \
                      .withColumn("address", lit("ANONYMISED"))

    # Write the anonymised data back to a new CSV file
    # Mode equals "overwrite" to overwite if files are existed
    anonymised_df.write.mode("overwrite").csv(output_path, header=True)

    spark.stop()

if __name__ == "__main__":
    # Call the spark job, passing 2 arguments
    # The first argument is the csv file we need to anonymise
    # The second argument is the csv file that we've anonymised the data
    anonymize_data('data.csv', 'anonymised_data.csv')
