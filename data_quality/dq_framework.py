def null_check(data, column):
    return data[column].isnull().sum()

def duplicate_check(data, column):
    return data[column].duplicated().sum()

def range_check(data, column, min_val, max_val):
    return ((data[column] < min_val) | (data[column] > max_val)).sum()
