import pandas as pd
import numpy as np

def read_csv_file(file_path):
    """
    Reads a CSV file using pandas and returns a pandas DataFrame object.
    """
    df = pd.read_csv(file_path, index_col=False)
    return df


def get_column_names(df):
    """
    Returns a list of column names of the given DataFrame.
    """
    return list(df.columns)



#Calculate all of the ratios for each index within 2 different dataframes
def calculate_ratios(df1, df2):
    rat_press, rat_temp, rat_den = [], [], []
    for i in range(len(df1)):
        rat_press.append(df1['Pressure'][i]/df2['Pressure'][i])
        rat_temp.append(df1['Temperature'][i]/df2['Temperature'][i])
        rat_den.append(df1['Density'][i]/df2['Density'][i])
    return rat_press

#Genereate a new dataframe with the ratios
def generate_ratio_df(df1, df2):
    calculate_ratios(df1, df2)
    """ Generates a new dataframe with the ratios of the 2 dataframes """
    df_new = df2.copy()
    for i in range(df1):
        df_new['Pressure'][i] = (df2['Density'][i]/rat_den[i])
        df_new['Temperature'][i] = (df2['Temperature'][i]/rat_temp[i])
        df_new['Density'][i] = (df2['Pressure'][i]/rat_press[i])

    return df_new

def finite_diff(M_old, M_current):
    """ Calculates the finite difference between the old and current Mach numbers"""
    MachOld = np.matrix([M_old])
    M_current = M_current

    S = M_old - M_current

    c = min(np.size(S), 4)
    cVec = np.transpose(np.matrix(range(c)))
    A = np.matrix(np.array(S) ** np.array(cVec))
    b = 1.0 * (cVec == 0)

    x = np.linalg.solve(A, b)
    x = np.linalg.pinv(A) * b

