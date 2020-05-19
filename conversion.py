import pandas as pd
import html 

file_path = "Resources/cities.csv"
file_df = pd.read_csv(file_path)
print(file_df)

file_html = file_df.to_html('data1.html')