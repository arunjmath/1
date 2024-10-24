from typing import List
#Question 1: Reverse List by N Elements
def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
    result = []
    for i in range(0, len(lst), n):
        group = lst[i:i + n]  
        reversed_group = []
        for j in range(len(group) - 1, -1, -1):
            reversed_group.append(group[j])
       
        result.extend(reversed_group)
    
    return result

print(reverse_by_n_elements([1, 2, 3, 4, 5, 6, 7, 8], 3))  # Output: [3, 2, 1, 6, 5, 4, 8, 7]
print(reverse_by_n_elements([1, 2, 3, 4, 5], 2))          # Output: [2, 1, 4, 3, 5]
print(reverse_by_n_elements([10, 20, 30, 40, 50, 60, 70], 4))  # Output: [40, 30, 20, 10, 70, 60, 50]
#Question 2: Lists & Dictionaries
from typing import List, Dict


def group_by_length(lst: List[str]) -> Dict[int, List[str]]:
    result = {}
    
    for word in lst:
        length = len(word)
        if length not in result:
            result[length] = []
        result[length].append(word)
    
    return dict(sorted(result.items()))

# Example usage:
print(group_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))
print(group_by_length(["one", "two", "three", "four"]))

#Question 3: Flatten a Nested Dictionary
from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    def _flatten(current_dict: Any, parent_key: str = '') -> Dict[str, Any]:
        items = {}
        for key, value in current_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.update(_flatten(value, new_key))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    list_key = f"{new_key}[{i}]"
                    if isinstance(item, dict):
                        items.update(_flatten(item, list_key))
                    else:
                        items[list_key] = item
            else:
                items[new_key] = value
        return items

    return _flatten(nested_dict)

# Example usage:
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
#from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    def _flatten(current_dict: Any, parent_key: str = '') -> Dict[str, Any]:
        items = {}
        for key, value in current_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.update(_flatten(value, new_key))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    list_key = f"{new_key}[{i}]"
                    if isinstance(item, dict):
                        items.update(_flatten(item, list_key))
                    else:
                        items[list_key] = item
            else:
                items[new_key] = value
        return items

    return _flatten(nested_dict)

# Example usage:
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
#from typing import Dict, Any

def flatten_dict(nested_dict: Dict[str, Any], sep: str = '.') -> Dict[str, Any]:
    def _flatten(current_dict: Any, parent_key: str = '') -> Dict[str, Any]:
        items = {}
        for key, value in current_dict.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            if isinstance(value, dict):
                items.update(_flatten(value, new_key))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    list_key = f"{new_key}[{i}]"
                    if isinstance(item, dict):
                        items.update(_flatten(item, list_key))
                    else:
                        items[list_key] = item
            else:
                items[new_key] = value
        return items

    return _flatten(nested_dict)

# Example usage:
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
#Question 4: Generate Unique Permutations
from typing import List
from itertools import permutations

def unique_permutations(nums: List[int]) -> List[List[int]]:
    all_perms = permutations(nums)
    unique_perms = set(all_perms)
    return [list(p) for p in unique_perms]

# Example usage
nums = [1, 1, 2]
result = unique_permutations(nums)
print(result)
#Question 5: Find All Dates in a Text
import re
from typing import List

def find_all_dates(text: str) -> List[str]:
    # Define the regular expressions for different date formats
    date_pattern = r'\b\d{2}-\d{2}-\d{4}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{4}\.\d{2}\.\d{2}\b'
    
    # Find all matching dates in the text
    valid_dates = re.findall(date_pattern, text)
    
    return valid_dates

# Example usage
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
result = find_all_dates(text)
print(result)
#Question 6: Decode Polyline, Convert to DataFrame with Distances
import polyline
import pandas as pd
from math import radians, sin, cos, sqrt, atan2

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371000
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def polyline_to_dataframe(polyline_str: str) -> pd.DataFrame:
    coordinates = polyline.decode(polyline_str)
    df = pd.DataFrame(coordinates, columns=['latitude', 'longitude'])
    distances = [0]
    for i in range(1, len(df)):
        lat1, lon1 = df.loc[i-1, 'latitude'], df.loc[i-1, 'longitude']
        lat2, lon2 = df.loc[i, 'latitude'], df.loc[i, 'longitude']
        distance = haversine_distance(lat1, lon1, lat2, lon2)
        distances.append(distance)
    df['distance'] = distances
    return df

polyline_str = '_p~iF~ps|U_ulLnnqC_mqNvxq`@'
df = polyline_to_dataframe(polyline_str)
print(df)
#Question 7: Matrix Rotation and Transformation
from typing import List

def rotate_and_transform(matrix: List[List[int]]) -> List[List[int]]:
    n = len(matrix)
    rotated_matrix = [[matrix[n - j - 1][i] for j in range(n)] for i in range(n)]
    transformed_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            row_sum = sum(rotated_matrix[i])
            col_sum = sum(rotated_matrix[k][j] for k in range(n))
            transformed_matrix[i][j] = row_sum + col_sum - 2 * rotated_matrix[i][j]

    return transformed_matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
final_matrix = rotate_and_transform(matrix)
print(final_matrix)
#Question 8: Time CheckS
import pandas as pd

def time_check(df: pd.DataFrame) -> pd.Series:
    df['timestamp'] = pd.to_datetime(df['startDay'] + ' ' + df['startTime'])
    df['end_timestamp'] = pd.to_datetime(df['endDay'] + ' ' + df['endTime'])
    
    grouped = df.groupby(['id', 'id_2'])
    
    def check_timestamps(group):
        full_week = set(range(7))  # 0: Monday, 6: Sunday
        timestamps = group['timestamp']
        days_covered = {ts.dayofweek for ts in timestamps}
        if days_covered != full_week:
            return False
        
        daily_ranges = group['timestamp'].dt.date.unique()
        if len(daily_ranges) < 7:
            return False
        
        for day in daily_ranges:
            day_times = timestamps[timestamps.dt.date == day]
            if not (day_times.min() <= pd.Timestamp(day) + pd.Timedelta(hours=0) and
                    day_times.max() >= pd.Timestamp(day) + pd.Timedelta(hours=23, minutes=59, seconds=59)):
                return False
        
        return True

    result = grouped.apply(check_timestamps)
    return result
