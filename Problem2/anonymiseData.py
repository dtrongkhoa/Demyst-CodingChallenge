from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

def anonymize_data(input_path, output_path):
    spark = SparkSession.builder.appName("Anonymize Data").getOrCreate()

    # Read the CSV file
    df = spark.read.csv(input_path, header=True)

    # Anonymize the data
    anonymized_df = df.withColumn("first_name", lit("ANONYMIZED")) \
                      .withColumn("last_name", lit("ANONYMIZED")) \
                      .withColumn("address", lit("ANONYMIZED"))

    # Write the anonymized data back to a new CSV file
    anonymized_df.write.csv(output_path, header=True)

    spark.stop()

if __name__ == "__main__":
    anonymize_data('data.csv', 'anonymized_data.csv')
