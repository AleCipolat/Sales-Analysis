import pandas as pd
import numpy as np

# Execute query
def sql_query(user_data:dict, data_base:str, table_name:str, query_lang:str) -> pd.DataFrame:
    """connects with mysql and retrieves the data as a DataFrame
    ## Inputs:
    * user_data: (dict) a dictionary containing the data for login in mysql. {"user":"user", "password":"password"} 
    * data_base: (str) The data base name in MySQL
    * table_name: (str) The Table we want to make the query.
    * query_lang: (str) the desired SQL syntax
    """

    # Import the required libraries for this function.
    import numpy as np
    import pandas as pd
    import mysql.connector as msql
    from mysql.connector import Error

    # Reading the user data from the dictionary.
    user = user_data["user"]
    password = user_data["password"]

    # Make the connection with My_SQL.
    try:
        conn = msql.connect(host='localhost', user=user,  
                            password=password)
        
        # Connect and cursor.
        if conn.is_connected():
            cursor = conn.cursor()

            # Input the query    
            sql = query_lang
            cursor.execute(sql)
            result = cursor.fetchall()         

            # Getting the table columns
            sql_get_columns = "SHOW COLUMNS FROM" + " "+data_base+"."+table_name
            cursor.execute(sql_get_columns)
            columns_names = cursor.fetchall()
            columns_names = [columns_names[each][0] for each in range(len(columns_names))]
            
            # Create a DataFrame
            df = pd.DataFrame(result, columns=columns_names)

        return df
    
    # Exception with the error displayed in screen.
    except Error as e:
        print("Error while connecting to MySQL", e)




