# Its loads from a dictionary to multiple csv files in the path we choose.
import os
import pickle

def create_csv_s(dict_dataframe: dict, folder_path: str):
    """It generates mutiple csv files with the dataframes contained in a dictionary.
    
    ## Parameters:
    * dict_dataframe:(dict) a dictionary which contains the name of the file, or dataset as a Key and the Dataframe as value.
    * folder_path: (str) the folder path in which it will create the csv files.
    ## Output:
    Multiple .csv files generated in the indicated path.
    """
    import os

    os.makedirs(folder_path, exist_ok=True)
    for dataset_name, dataset in dict_dataframe.items():
        file_path = os.path.join(folder_path, f"{dataset_name}.csv")
        dataset.to_csv(file_path)
        print(f"The file for the: {dataset_name} has been created in the following route: {file_path}\n")




# Load the python object in the desired path in pickle format
def create_pickle_file(object:any , folder_path:str, file_name:str) -> pickle:
    """It generates a pickle file to store the python object in the desired path.
    
    ## Parameters:
    * object:(any) any python object
    * folder_path: (str) the folder path in which it will create the pickle file.
    * file_name: (str) the pickle object file name
    
    ## Output:
    A pickle file containing the generated object in the indicated path with the indicated name.

    ## Example:
    my_new_list = [1,2,3]

    folder_path = "C:\\Users\\user\\project"

    create_pickle_file(object=df_dict, folder_path= folder_path, file_name="my_new_list" )

    """
    import os
    import pickle

    #os.makedirs(folder_path, exist_ok=True)
    try:
        os.chdir(folder_path)
        #file_path = os.path.join(folder_path, f"{dataset_name}.csv")
        file = open(file_name, "wb")
        pickle.dump(df_dict, file)
        file.close()

        print(f"The file has been created in the following path: {folder_path}\{file_name}")
    
    except:
        print(f"The file: {file_name} couldn't be created in the following path: {folder_path}\n")



# Import some python object from flash to python while using pickle
# A function to load a python object from disk to the virtual enviroment.
def load_pickle_file(file_path:str) -> any:
    """Load a pickle file to the enviroment.
    """
    import pickle
    import os

    try:
        #os.chdir(file_path)
        pickle_file = open(file_path, "rb")
        python_object = pickle.load(pickle_file)
        pickle_file.close()

        print(f"The file has been readed from the following path: {file_path}")
        
        return python_object
    
    except:
        print(f"The file: couldn't be readed in the following path: {file_path}\n")
