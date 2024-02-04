import numpy as np
from scipy import stats
from scipy.stats import chi2_contingency,mode, skew, kurtosis,norm, expon, uniform, binom, poisson
import matplotlib.pyplot as plt
import os
import pandas as pd


# Function to calculate mean
def calculate_mean(data, column_name):
    mean_value = data.mean()
    print(f"Mean for '{column_name}': {mean_value}")
    return mean_value

# Function to calculate mode
def calculate_mode(data, column_name):
    mode_value = data.mode().iloc[0]
    print(f"Mode for '{column_name}': {mode_value}")
    return mode_value

# Function to calculate median
def calculate_median(data, column_name):
    median_value = data.median()
    print(f"Median for '{column_name}': {median_value}")
    return median_value

# Function to calculate minimum
def calculate_minimum(data, column_name):
    min_value = data.min()
    print(f"Minimum for '{column_name}': {min_value}")
    return min_value

# Function to calculate maximum
def calculate_maximum(data, column_name):
    max_value = data.max()
    print(f"Maximum for '{column_name}': {max_value}")
    return max_value

# Function to calculate quartiles
def calculate_quartiles(data, column_name):
    try:
        column_data = pd.to_numeric(data, errors='coerce').dropna()
        q1 = np.percentile(column_data, 25, method='midpoint')
        q3 = np.percentile(column_data, 75, method='midpoint')
        print(f"Q1 for '{column_name}': {q1}")
        print(f"Q3 for '{column_name}': {q3}")
        return q1, q3
    except ValueError:
        print(f"Unable to calculate quartiles for '{column_name}'. Contains non-numeric values.")
        return None, None

# Function to calculate sum of squared errors
def calculate_sse(data, column_name):
    mean_value = calculate_mean(data, column_name)
    sse_value = np.sum((data - mean_value) ** 2)
    print(f"Sum of Squared Errors for '{column_name}': {sse_value}")
    return sse_value

# Function to calculate skewness
def calculate_skewness(data, column_name):
    skewness_value = data.skew()
    print(f"Skewness for '{column_name}': {skewness_value}")
    return skewness_value

# Function to calculate kurtosis
def calculate_kurtosis(data, column_name):
    kurtosis_value = data.kurtosis()
    print(f"Kurtosis for '{column_name}': {kurtosis_value}")
    return kurtosis_value

# Function to calculate population standard deviation
def calculate_population_std_dev(data, column_name):
    std_dev_value = data.std()
    print(f"Population Standard Deviation for '{column_name}': {std_dev_value}")
    return std_dev_value

# Function to calculate population variance
def calculate_population_variance(data, column_name):
    variance_value = data.var()
    print(f"Population Variance for '{column_name}': {variance_value}")
    return variance_value


# Function to print statistics for a column
def print_column_statistics(df, column_name):
    try:
        print(f"--------------------FOR THE COLUMN '{column_name}'--------------------\n\n")
        column_data = df[column_name].astype(float)
        calculate_mean(column_data, column_name)
        calculate_mode(column_data, column_name)
        calculate_median(column_data, column_name)
        calculate_minimum(column_data, column_name)
        calculate_maximum(column_data, column_name)
        calculate_quartiles(column_data, column_name)
        calculate_sse(column_data, column_name)
        calculate_skewness(column_data, column_name)
        calculate_kurtosis(column_data, column_name)
        calculate_population_std_dev(column_data, column_name)
        calculate_population_variance(column_data, column_name)

        print(f"\n\n")
        

    except ValueError:
        print(f"Unable to calculate statistics for '{column_name}'. Contains non-numeric values.\n\n")

# Main function
def main():
    directory_path = './uploads'

    # Checks for any CSV file in the directory
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # Check if exactly one CSV file is found
    if len(csv_files) != 0:
        csv_file = csv_files[0]
        csv_file_path = os.path.join(directory_path, csv_file)

        if os.path.isfile(csv_file_path):
            df = pd.read_csv(csv_file_path)

    #-----------------------------------------iterates though every column in the dataset------------------------
            for column_name in df.columns:
                print_column_statistics(df, column_name)
                #print(f"Processing column '{column}' in file '{csv_file}'")
        else:
            print(f"Invalid file format. File '{csv_file}' is not a CSV file.")
    else:
        return

main()