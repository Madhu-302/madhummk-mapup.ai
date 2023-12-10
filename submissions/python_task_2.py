import pandas as pd

def calculate_distance_matrix(df):

    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    
    distance_matrix = df.pivot_table(index='id_start', columns='id_end', values='distance', aggfunc='sum', fill_value=0)

    distance_matrix = distance_matrix + distance_matrix.T

    distance_matrix.values[[range(len(distance_matrix))]*2] = 0

    return distance_matrix


df = pd.read_csv('dataset-3.csv')

matrix_df = calculate_distance_matrix(df)
print(matrix_df)
print()




def unroll_distance_matrix(df):

    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    
    unrolled_df = pd.DataFrame(columns=['id_start', 'id_end', 'distance'])

    for index, row in df.iterrows():
        id_start = row['id_start']
        id_end = row['id_end']
        distance = row['distance']

        if id_start != id_end:
            unrolled_df = unrolled_df._append({'id_start': id_start, 'id_end': id_end, 'distance': distance}, ignore_index=True)

    return unrolled_df

df = pd.read_csv("dataset-3.csv")

unrolled_df_matrix = unroll_distance_matrix(df)
print(unrolled_df_matrix)
print()






def find_ids_within_ten_percentage_threshold(df, reference_value):

    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    

    reference_df = df[df['id_start'] == reference_value]

    avg_distance = reference_df['distance'].mean()

    lower_bound = avg_distance - (0.1 * avg_distance)
    upper_bound = avg_distance + (0.1 * avg_distance)

    filtered_df = df[(df['distance'] >= lower_bound) & (df['distance'] <= upper_bound)]

    result_ids = sorted(filtered_df['id_start'].unique())

    return result_ids


df = unrolled_df_matrix
reference_value = 123  

dataframe_ids = find_ids_within_ten_percentage_threshold(df, reference_value)
print(dataframe_ids)
print()






def calculate_toll_rate(dataframe):

    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    
    df = pd.read_csv("dataset-3.csv")
    
    dataframe['moto'] = 0.8 * dataframe['distance']
    dataframe['car'] = 1.2 * dataframe['distance']
    dataframe['rv'] = 1.5 * dataframe['distance']
    dataframe['bus'] = 2.2 * dataframe['distance']
    dataframe['truck'] = 3.6 * dataframe['distance']

    return dataframe

df_with_toll_rates = calculate_toll_rate(df)
df_with_toll_rates = df_with_toll_rates.drop(["distance"],axis = 1)
print(df_with_toll_rates)
print()
























