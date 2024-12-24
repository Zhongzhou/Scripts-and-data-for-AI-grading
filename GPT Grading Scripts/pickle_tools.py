### This tool allows the user to save a list of variables using dill, and load them into the new session
### This tool is useful for llms because dill doesn't work well with connection objects.

import os
import dill as pickle

### The globalVars parameter is used to allow the function to access the global variables of the environment that it is imported into. 

def save_as_pickle(variables : list, folderName : str, globalVars, path = './pickle_objects'):
    """
    Takes a list of variables and pickles each variable into a file named "{variable_name}.pkl" in the specified path,
    and returns a list containing the names of the variables as strings.
    """
    variable_names = []
    folder_path = os.path.join(path, folderName)
    #checks if the folder exists under pickle_objects main folder
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for variable in variables:
        var_name = [name for name, val in globalVars.items() if id(val) == id(variable) and not name.startswith('_')]
        if var_name:
            var_name = var_name[0]
            file_path = os.path.join(folder_path, f"{var_name}.pkl")
            with open(file_path, 'wb') as f:
                pickle.dump(variable, f)
            variable_names.append(var_name)
        else:
            raise IndexError(f"Variable '{variable}' does not exist in the global scope.")
    globalVars['pickled_varNames'] = variable_names #This is convenient for debugging purposes, shows which variables are actually being pickled
    # Pickle the variable names itself
    with open(os.path.join(folder_path, '__varNames.pkl'), 'wb') as f:
        pickle.dump(variable_names, f)
    

def load_variables(variable_names, globalVars, folderName, path='./pickle_objects'):
    """
    Takes a list of variable names as strings, and loads from the specified path all of the "{variable_name}.pkl"
    files into the corresponding variable names.
    """
    #checks if the folder exists under pickle_objects main folder
    folder_path = os.path.join(path, folderName)
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Cannot find the folder {folderName} under {path}") 

    for var_name in variable_names:
        file_path = os.path.join(folder_path, f"{var_name}.pkl")
        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                globalVars[var_name] = pickle.load(f)
        else:
            print(f"File '{file_path}' does not exist.")

def load_from_pickle(folderName, globalVars, path = "./pickle_objects"):
    folder_path = os.path.join(path, folderName)
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"Cannot find the folder {folderName} under {path}") 
    varName_file_path = os.path.join(folder_path, "__varNames.pkl")
    with open(varName_file_path, 'rb') as f:
        pickle_varNames = pickle.load(f) #doing it this way has the added benefit of being able to hide the pickl_varNames variable from the global environment.
    load_variables(pickle_varNames, globalVars, folderName, path)

