import numpy as np
import pandas as pd

# Method 1
data = np.array([['1', '2'], ['3', '4']])
dataFrame = pd.DataFrame(data, columns=['col1', 'col2'])
print(dataFrame)  # print a normal dataframe

json = dataFrame.to_json()
print(json)  # {"col1":{"0":"1","1":"3"},"col2":{"0":"2","1":"4"}}

# Other methods to represent this data
json_split = dataFrame.to_json(orient='split')
print('json_split = ', json_split, "\n")

json_records = dataFrame.to_json(orient='records')
print('json_records = ', json_records, '\n')

json_index = dataFrame.to_json(orient='index')
print('json_index = ', json_index, '\n')

json_columns = dataFrame.to_json(orient='columns')
print('json_columns = ', json_columns, '\n')

json_values = dataFrame.to_json(orient='values')
print('json_values = ', json_values, '\n')

json_table = dataFrame.to_json(orient='table')
print('json_table = ', json_table, '\n')

# All outputs listed below.
'''
  col1 col2
0    1    2
1    3    4
{"col1":{"0":"1","1":"3"},"col2":{"0":"2","1":"4"}}
json_split =  {"columns":["col1","col2"],"index":[0,1],"data":[["1","2"],["3","4"]]} 
json_records =  [{"col1":"1","col2":"2"},{"col1":"3","col2":"4"}] 
json_index =  {"0":{"col1":"1","col2":"2"},"1":{"col1":"3","col2":"4"}} 
json_columns =  {"col1":{"0":"1","1":"3"},"col2":{"0":"2","1":"4"}} 
json_values =  [["1","2"],["3","4"]] 
json_table =  {"schema":{"fields":[{"name":"index","type":"integer"},{"name":"col1","type":"string"},{"name":"col2","type":"string"}],"primaryKey":["index"],"pandas_version":"0.20.0"},"data":[{"index":0,"col1":"1","col2":"2"},{"index":1,"col1":"3","col2":"4"}]} 
'''
