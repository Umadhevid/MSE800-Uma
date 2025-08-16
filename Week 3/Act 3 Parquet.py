# Develop a Python project using an object-oriented (OO) approach to convert large datasets into Parquet format. 
# Then, compute the maximum, minimum, average, and absolute values for each column in the dataset.

import pandas as pd
from ucimlrepo import fetch_ucirepo 
class parquet_handling:
    def display_parquet(self,text):
        self.text=text
    def convert_parquet(self,text):
        panda_df=pd.read_csv(text)
        panda_df.to_parquet("hospitaldata.parquet", engine='pyarrow', index=False)
        panda_df = pd.read_parquet("large_dataset.parquet", engine='pyarrow')
        print(panda_df.head())
    def mainfun(self):
        hospitaldata = fetch_ucirepo(id=296) 

if __name__=='__main__':
    parquet_handling.mainfun()

  
# # fetch dataset 
# hospitaldata = fetch_ucirepo(id=296) 
  
# # data (as pandas dataframes) 
# X = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
# y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets 
  
# # metadata 
# print(diabetes_130_us_hospitals_for_years_1999_2008.metadata) 
  
# # variable information 
# print(diabetes_130_us_hospitals_for_years_1999_2008.variables)  

# df = pd.read_parquet("large_dataset.parquet", engine='pyarrow')
# print(df.head())
# df = pd.read_csv("large_dataset.csv")

# # Convert to Parquet
# df.to_parquet("large_dataset.parquet", engine='pyarrow', index=False)


df = pd.concat([hospitaldata.data.features, hospitaldata.data.targets], axis=1)
df.to_parquet("hospital_data.parquet", engine="pyarrow", index=False)
df_parquet = pd.read_parquet("hospital_data.parquet", engine="pyarrow")
print(df_parquet.head())
