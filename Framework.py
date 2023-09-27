import numpy as np
import pandas as pd
import sys
import os


f_path = os.path.dirname(os.path.realpath(__file__))

class CFD_Extrapolation():
    def __init__(self, df1=None, df2=None, filepath=f_path):
        self.df1 = df1
        self.df2 = df2
        self.filepath = filepath
        print('CFD_Extrapolation object created')
        print('Filepath: {}'.format(self.filepath))
        print('df1: {}'.format(self.df1))
        print('df2: {}'.format(self.df2))
        print('-------------------------------------------------------------------')
        print("""
   ______    ______    ____            ______   _  __  ______    ____     ___     ____    ____     __     ___   ______    ____   ____     _   __
  / ____/   / ____/   / __ \          / ____/  | |/ / /_  __/   / __ \   /   |   / __ \  / __ \   / /    /   | /_  __/   /  _/  / __ \   / | / /
 / /       / /_      / / / /         / __/     |   /   / /     / /_/ /  / /| |  / /_/ / / / / /  / /    / /| |  / /      / /   / / / /  /  |/ / 
/ /___    / __/     / /_/ /         / /___    /   |   / /     / _, _/  / ___ | / ____/ / /_/ /  / /___ / ___ | / /     _/ /   / /_/ /  / /|  /  
\____/   /_/       /_____/         /_____/   /_/|_|  /_/     /_/ |_|  /_/  |_|/_/      \____/  /_____//_/  |_|/_/     /___/   \____/  /_/ |_/   
                                                                                                                                                
""")
        print('-------------------------------------------------------------------')


    def read_csv_file(self):
        """
        Reads a CSV file using pandas and returns a pandas DataFrame object.
        """
        df = pd.read_csv(self.filepath, index_col=False)
        return df
    
    def get_column_names(self, df):
        """
        Returns a list of column names of the given DataFrame.
        """
        return list(df.columns) 
    
    def calculate_ratios(self, df1, df2):
        """ Calculates all of the ratios for each index within 2 different dataframes """
        rat_press, rat_temp, rat_den = [], [], []
        for i in range(len(df1)):
            rat_press.append(df1['Pressure'][i]/df2['Pressure'][i])
            rat_temp.append(df1['Temperature'][i]/df2['Temperature'][i])
            rat_den.append(df1['Density'][i]/df2['Density'][i])
        return rat_press
    
    def generate_ratio_df(self, df1, df2):
        """ Generates a new dataframe with the ratios of the 2 dataframes """
        rat_press, rat_temp, rat_den = self.calculate_ratios(df1, df2)
        df_new = df2.copy()
        for i in range(len(df1)):
            df_new['Pressure'][i] = (df2['Density'][i]/rat_den[i])
            df_new['Temperature'][i] = (df2['Temperature'][i]/rat_temp[i])
            df_new['Density'][i] = (df2['Pressure'][i]/rat_press[i])
    
        return df_new
    
    def finite_diff(self, M_old, M_current):
        """ Calculates the finite difference between the old and current Mach numbers"""
        MachOld = np.matrix([M_old])
        M_current = M_current

        S = MachOld - M_current

        c = min(np.size(S), 4)
        cVec = np.transpose(np.matrix(range(c)))
        A = np.matrix(np.array(S) ** np.array(cVec))
        b = 1.0 * (cVec == 0)

        x = np.linalg.solve(A, b)
        x = np.linalg.pinv(A) * b

        return x
    
    def extrapolate(self, df1, df2):
        """ Extrapolates the data from 2 dataframes and returns a new dataframe with the extrapolated data """
        df_new = self.generate_ratio_df(df1, df2)
        df_new['Pressure'] = df_new['Pressure'].apply(lambda x: x * 1.2)
        df_new['Temperature'] = df_new['Temperature'].apply(lambda x: x * 1.2)
        df_new['Density'] = df_new['Density'].apply(lambda x: x * 1.2)
        return df_new

   
    def check_csv_file(self):
        """ Checks to see if the restart csv file is present in the current working directory """
        if os.path.isfile('restart.csv'):
            return True
        else:
            print('restart.csv not found in current working directory')
            return False
        
    def parse_dict(self, file_name, dict_name):
        """ Parses a dictionary from a file """
        with open(file_name, 'r') as f:
            f_data = f.read()

        for key in dict_name:
            f_data = f_data.replace(key, str(dict_name[key]))

        with open(file_name, 'w') as f:
            f.write(f_data)

    #to-do: add a function that checks the total number of iterations of a completed simulation and compares it with the previous simulation

    def check_iter(self, df1, df2):
        """ Checks the total number of iterations of a completed simulation and compares it with the previous simulation """
        
        pass
    
    #to-do: add a function that applies the rankine-hugoniot relations to the dataframes

    def rankine_hugoniot(self, df1, df2):
        """ Applies the Rankine-Hugoniot relations to the dataframes """
        pass
    
    
    # def check_csv_file(self):
    #     """ Checks to see if the restart csv file is present in the current working directory """
    #     try:
    #         open('restart.csv')
    #     except IOError:
    #         print('restart.csv not found in current working directory')
    #         sys.exit(1)