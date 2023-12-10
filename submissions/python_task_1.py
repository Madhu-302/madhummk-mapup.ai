import pandas as pd

def generate_car_matrix(dataset):
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    df = pd.read_csv(dataset)
    
    car_matrix = df.pivot(columns = "id_2",index = "id_1",values = "car")

    car_matrix = car_matrix.fillna(0)

    for i in range(min(car_matrix.shape[0],car_matrix.shape[1])):
        car_matrix.iloc[i,i] = 0
    return car_matrix
  
dataset = "dataset-1.csv"
matrix_dataframe = generate_car_matrix(dataset)
print(matrix_dataframe)
print()



def get_type_count(dataset):

    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    
    df = pd.read_csv(dataset)
    
    df["car_type"] = pd.cut(
                            df["car"],
                            bins = [float("-inf"),15,25,float("inf")],
                            labels = ["low","medium","high"],
                            include_lowest = True
    
    )
    
    type_count = df["car_type"].value_counts().to_dict()
    
    sorted_type_count = dict(sorted(type_count.items()))
    
    return sorted_type_count 
  
dataset = "dataset-1.csv"
car_type_dict = get_type_count(dataset)
print(car_type_dict)
print() 





def get_bus_indexes(dataset):

    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """

    df = pd.read_csv(dataset)
    
    bus_mean = df["bus"].mean()
    
    con = df["bus"] > 2*bus_mean
    
    bus_indices = df[con].index.to_list()
    
    sorted_bus_indices = sorted(bus_indices)
    
    return sorted_bus_indices
    
dataset = "dataset-1.csv"

bus_indices_list = get_bus_indexes(dataset)
print(bus_indices_list)
print()





def filter_routes(dataset):

    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    
    df = pd.read_csv(dataset)
    
    grouped = df.groupby(by = ["route"])["truck"]
    
    filtered = grouped.mean().reset_index()
    
    filtered_df = filtered[filtered["truck"]>7]
    
    sorted_res = sorted(filtered_df["route"].to_list())
   
    return sorted_res
  
dataset = "dataset-1.csv"
route_list = filter_routes(dataset)
print(route_list)
print()





def multiply_matrix(input_df):

    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    
    modified_df = input_df.copy()
    
    modified_df = modified_df.applymap(lambda x:x*0.75 if x>20 else x*1.75)
    
    modified_df = modified_df.round(1)
    
    return modified_df

input_df = pd.read_csv("dataset-1.csv")
modified_matrix = multiply_matrix(input_df)
print(modified_matrix) 





def time_check(df):
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame): Input DataFrame containing columns id, id_2, startDay, startTime, endDay, endTime.

    Returns:
        pd.Series: Boolean series indicating if each (`id`, `id_2`) pair has incorrect timestamps.
    """
    
    df['start_timestamp'] = pd.to_datetime(df['startTime'])

    df['end_timestamp'] = pd.to_datetime(df['endTime'])

    df['duration'] = df['end_timestamp'] - df['start_timestamp']

    mask = (df['duration'] == pd.Timedelta(days=1)) & (df['start_timestamp'].dt.dayofweek == 0) & (df['end_timestamp'].dt.dayofweek == 6)

    result_series = df.groupby(['id', 'id_2'])['duration'].agg(lambda x: x.mask(mask).any()).fillna(False)

    return result_series

df = pd.read_csv("dataset-2.csv")
time_series = time_check(df)
print(time_series)



