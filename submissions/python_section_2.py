#Question 9: Distance Matrix Calculation
import pandas as pd
import numpy as np

def calculate_distance_matrix() -> pd.DataFrame:
   
    ids = [1001400, 1001402, 1001404, 1001406, 1001408, 1001410, 1001412]
    distances = [
        [0.0, 9.7, 29.9, 45.9, 67.6, 78.7, 94.3],
        [9.7, 0.0, 20.2, 36.2, 57.9, 69.0, 84.6],
        [29.9, 20.2, 0.0, 16.0, 37.7, 48.8, 64.4],
        [45.9, 36.2, 16.0, 0.0, 21.7, 32.8, 48.4],
        [67.6, 57.9, 37.7, 21.7, 0.0, 11.1, 26.7],
        [78.7, 69.0, 48.8, 32.8, 11.1, 0.0, 15.6],
        [94.3, 84.6, 64.4, 48.4, 26.7, 15.6, 0.0]
    ]
    
    distance_matrix = pd.DataFrame(distances, index=ids, columns=ids)

    distance_matrix = (distance_matrix + distance_matrix.T) / 2

    return distance_matrix

distance_df = calculate_distance_matrix()
print(distance_df)


#Question 10: Unroll Distance Matrix
import pandas as pd

def unroll_distance_matrix(df: pd.DataFrame) -> pd.DataFrame:
    results = []
    
    for index, row in df.iterrows():
        id_start = row['id_start']
        for id_end in df['id_end'].unique():
            if id_start != id_end:
                results.append({'id_start': id_start, 'id_end': id_end, 'distance': row['distance']})
    
    unrolled_df = pd.DataFrame(results)
    
    return unrolled_df

data = {
    'id_start': [1001400] * 9,
    'id_end': [1001402, 1001404, 1001406, 1001408, 1001410, 1001412, 1001414, 1001416, 1001418],
    'distance': [9.7, 29.9, 45.9, 67.6, 78.7, 94.3, 112.5, 125.7, 139.3]
}
df = pd.DataFrame(data)

unrolled_df = unroll_distance_matrix(df)
print(unrolled_df)


#Question 11: Finding IDs within Percentage Threshold


import pandas as pd

def find_ids_within_ten_percentage_threshold(df: pd.DataFrame, reference_id: int) -> pd.DataFrame:
   
    reference_distances = df[df['id_start'] == reference_id]['distance']
    
    if reference_distances.empty:
        print(f"No distances found for reference ID: {reference_id}")
        return pd.DataFrame(columns=['id_start', 'average_distance'])

    average_distance = reference_distances.mean()
    
    lower_bound = average_distance * 0.90  # 10% less
    upper_bound = average_distance * 1.10  # 10% more

    average_distances_df = df.groupby('id_start', as_index=False)['distance'].mean()
    
    filtered_df = average_distances_df[
        (average_distances_df['distance'] >= lower_bound) & 
        (average_distances_df['distance'] <= upper_bound)
    ]
    
    filtered_df = filtered_df.sort_values(by='id_start')

    return filtered_df

data = {
    'id_start': [1001400, 1001400, 1001400, 1001401, 1001401, 1001402, 1001402, 1001403, 1001403],
    'id_end': [1001402, 1001404, 1001406, 1001400, 1001401, 1001400, 1001402, 1001403, 1001404],
    'distance': [10.5, 15.5, 20.0, 9.0, 11.5, 12.0, 13.5, 14.0, 15.0]
}

df = pd.DataFrame(data)

result_df = find_ids_within_ten_percentage_threshold(df, 1001400)

print("Filtered DataFrame:")
print(result_df)



#Question 12: Calculate Toll Rate


import pandas as pd

def calculate_toll_rate(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame): The input DataFrame with distance data.

    Returns:
        pandas.DataFrame: The modified DataFrame with calculated toll rates.
    """
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }

    for vehicle, coefficient in rate_coefficients.items():
        df[vehicle] = df[vehicle] * coefficient

    return df

data = {
    'id_start': [1001400]*10,
    'id_end': [1001402, 1001404, 1001406, 1001408, 1001410, 1001412, 1001414, 1001416, 1001418, 1001420],
    'moto': [7.76, 23.92, 36.72, 54.08, 62.96, 75.44, 90.00, 100.56, 111.44, 121.76],
    'car': [11.64, 35.88, 55.08, 81.12, 94.44, 113.16, 135.00, 150.84, 167.16, 182.64],
    'rv': [14.55, 44.85, 68.85, 101.40, 118.05, 141.45, 168.75, 188.55, 208.95, 228.30],
    'bus': [21.34, 65.78, 100.98, 148.72, 173.14, 207.46, 247.50, 276.54, 306.46, 334.84],
    'truck': [34.92, 107.64, 165.24, 243.36, 283.32, 339.48, 405.00, 452.52, 501.48, 547.92]
}

df = pd.DataFrame(data)

result_df = calculate_toll_rate(df)

print(result_df)
#Question 13: Calculate Time-Based Toll Rates
import pandas as pd
import datetime

def calculate_toll_rate(df) -> pd.DataFrame:
   
    return df

def calculate_time_based_toll_rates(df) -> pd.DataFrame:
    
  
    weekday_discount_factors = {
        (datetime.time(0, 0), datetime.time(10, 0)): 0.8,
        (datetime.time(10, 0), datetime.time(18, 0)): 1.2,
        (datetime.time(18, 0), datetime.time(23, 59, 59)): 0.8
    }
    
    weekend_discount_factor = 0.7

    toll_rates_df = df.copy()

    for index, row in toll_rates_df.iterrows():
        start_day = row['start_day']
        start_time = row['start_time']
        
       
        if start_day in ['Saturday', 'Sunday']:
           
            discount_factor = weekend_discount_factor
        else:
            
            discount_factor = 1.0 
            for time_range, factor in weekday_discount_factors.items():
                if time_range[0] <= start_time < time_range[1]:
                    discount_factor = factor
                    break
        
       
        toll_rates_df.at[index, 'moto'] *= discount_factor
        toll_rates_df.at[index, 'car'] *= discount_factor
        toll_rates_df.at[index, 'rv'] *= discount_factor
        toll_rates_df.at[index, 'bus'] *= discount_factor
        toll_rates_df.at[index, 'truck'] *= discount_factor

    return toll_rates_df


data = {
    'id_start': [1001400, 1001400, 1001400, 1001400, 1001408, 1001408, 1001408, 1001408],
    'id_end': [1001402, 1001402, 1001402, 1001402, 1001410, 1001410, 1001410, 1001410],
    'distance': [9.7, 9.7, 9.7, 9.7, 11.1, 11.1, 11.1, 11.1],
    'start_day': ['Monday', 'Tuesday', 'Wednesday', 'Saturday', 'Monday', 'Tuesday', 'Wednesday', 'Saturday'],
    'start_time': [datetime.time(0, 0), datetime.time(10, 0), datetime.time(18, 0), datetime.time(0, 0),
                   datetime.time(0, 0), datetime.time(10, 0), datetime.time(18, 0), datetime.time(0, 0)],
    'end_day': ['Friday', 'Saturday', 'Sunday', 'Sunday', 'Friday', 'Saturday', 'Sunday', 'Sunday'],
    'end_time': [datetime.time(10, 0), datetime.time(18, 0), datetime.time(23, 59, 59), datetime.time(23, 59, 59),
                 datetime.time(10, 0), datetime.time(18, 0), datetime.time(23, 59, 59), datetime.time(23, 59, 59)],
    'moto': [6.21, 9.31, 6.21, 5.43, 7.10, 10.66, 7.10, 6.22],
    'car': [9.31, 13.97, 9.31, 8.15, 10.66, 15.98, 10.66, 9.32],
    'rv': [11.64, 17.46, 11.64, 10.19, 13.32, 19.98, 13.32, 11.66],
    'bus': [17.07, 25.61, 17.07, 14.94, 19.54, 29.30, 19.54, 17.09],
    'truck': [27.94, 41.90, 27.94, 24.44, 31.97, 47.95, 31.97, 27.97]
}

df = pd.DataFrame(data)

result_df = calculate_time_based_toll_rates(df)

print(result_df)
