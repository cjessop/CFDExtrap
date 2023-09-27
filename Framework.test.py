import pandas as pd
import numpy as np
import os
from Framework import CFD_Extrapolation

# create test dataframes
df1 = pd.DataFrame({'Pressure': [1, 2, 3], 'Temperature': [100, 200, 300], 'Density': [10, 20, 30]})
df2 = pd.DataFrame({'Pressure': [4, 5, 6], 'Temperature': [400, 500, 600], 'Density': [40, 50, 60]})

# create CFD_Extrapolation object
cfd = CFD_Extrapolation(df1, df2)

# test read_csv_file method
assert isinstance(cfd.read_csv_file(), pd.DataFrame)

# test get_column_names method
assert cfd.get_column_names(df1) == ['Pressure', 'Temperature', 'Density']

# test calculate_ratios method
assert np.allclose(cfd.calculate_ratios(df1, df2), [0.25, 0.4, 0.5])

# test generate_ratio_df method
df_new = cfd.generate_ratio_df(df1, df2)
assert np.allclose(df_new['Pressure'], [4.0, 5.0, 6.0])
assert np.allclose(df_new['Temperature'], [400.0, 500.0, 600.0])
assert np.allclose(df_new['Density'], [40.0, 50.0, 60.0])

# test extrapolate method
df_extrapolated = cfd.extrapolate(df1, df2)
assert np.allclose(df_extrapolated['Pressure'], [4.8, 6.0, 7.2])
assert np.allclose(df_extrapolated['Temperature'], [480.0, 600.0, 720.0])
assert np.allclose(df_extrapolated['Density'], [48.0, 60.0, 72.0])

# test check_csv_file method
assert cfd.check_csv_file() == False

# test parse_dict method
dict_name = {'key1': 'value1', 'key2': 'value2'}
file_name = 'test.txt'
with open(file_name, 'w') as f:
    f.write('key1: {{key1}}, key2: {{key2}}')
cfd.parse_dict(file_name, dict_name)
with open(file_name, 'r') as f:
    assert f.read() == 'key1: value1, key2: value2'

# test finite_diff method
M_old = [1, 2, 3]
M_current = [4, 5, 6]
assert np.allclose(cfd.finite_diff(M_old, M_current), [-3.0, 3.0, 0.0])