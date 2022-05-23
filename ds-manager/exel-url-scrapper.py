import pandas as pd
import urllib.request


excel_file_path = 'csv-files/exterior.csv'

df = pd.read_csv(excel_file_path)
print(df.head())
# # print('Beginning file download with urllib...')
# url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
# urllib.request.urlretrieve(url, '/Users/scott/Downloads/cat.jpg')