from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("YourAppName").getOrCreate()
data1 = [(1, "Alice","Purnia","12/06/2003","23/09/2050",-1),(2, "Bob","Jaipur","12/06/2033","23/09/2055",0),(3, "Charlie","Delhi","12/06/2053","23/09/2055",1)]    
columns1 = ["id", "name","Address","dob","dob1","status"]

df = spark.createDataFrame(data1, columns1)

expected_df = [Row(id=1, name='Alice', Address='Purnia', dob='12/06/2003', dob1='23/09/2050', status=-1, city=None), 
 Row(id=2, name='Bob', Address='Jaipur', dob='12/06/2033', dob1='23/09/2055', status=0, city=None), 
 Row(id=3, name='Charlie', Address='Delhi', dob='12/06/2053', dob1='23/09/2055', status=1, city=None)]
#df.collect() # it should be in the form of df.collect() for compare.

columns_to_add = ['city']

columns_to_drop = ['city']

column_to_capitalize = ['Address']




