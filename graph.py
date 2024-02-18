import matplotlib.pyplot as plt
import os
import pandas as pd
import sys
import seaborn as sns

# Function to generate scatter plot and save as PNG
def scatter_plot(data, column_x, column_y, save_location, graph):
    try:
        # Convert columns to numeric, handling non-numeric values
        data[column_x] = pd.to_numeric(data[column_x], errors='coerce')
        data[column_y] = pd.to_numeric(data[column_y], errors='coerce')

        # Drop NaN values
        data = data.dropna(subset=[column_x, column_y])

        plt.scatter(data[column_x], data[column_y])
        plt.title(f"Scatter Plot for '{column_x}' vs '{column_y}'")
        plt.xlabel(column_x)
        plt.ylabel(column_y)

        path = f"{save_location}/{column_x}_vs_{column_y}{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  
    except ValueError as e:
        print(f"Error: {e}")

# Function to generate line plot and save as PNG
def line_graph(data, column_x, column_y, save_location, graph):
    try:
        # Convert columns to numeric, handling non-numeric values
        data[column_x] = pd.to_numeric(data[column_x], errors='coerce')
        data[column_y] = pd.to_numeric(data[column_y], errors='coerce')

        # Drop NaN values
        data = data.dropna(subset=[column_x, column_y])

        plt.plot(data[column_x], data[column_y])
        plt.title(f"Line Plot for '{column_x}' vs '{column_y}'")
        plt.xlabel(column_x)
        plt.ylabel(column_y)

        path = f"{save_location}/{column_x}_vs_{column_y}{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  
    except ValueError as e:
        print(f"Error: {e}")

    

# Function to generate bar plot and save as PNG
def bar_graph(data, column_x, column_y, save_location, graph):
    try:
        # If the x-axis column contains non-numeric values, use range(len(data)) for the bar positions
        if not pd.api.types.is_numeric_dtype(data[column_x]):
            x_values = range(len(data))
            x_labels = data[column_x]
        else:
            x_values = data[column_x]
            x_labels = None

        plt.bar(x_values, data[column_y])
        plt.title(f"Bar Plot for '{column_x}' vs '{column_y}'")
        plt.xlabel(column_x)
        plt.ylabel(column_y)

        if x_labels is not None:
            plt.xticks(x_values, x_labels, rotation=45, ha='right')  

        path = f"{save_location}/{column_x}_vs_{column_y}{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  
    except ValueError as e:
        print(f"Error: {e}")
        
        
# Function to generate box plot and save as PNG
def box_plot(data, column_x, save_location, graph):
    try:
        # Convert the column_x to numeric, handling non-numeric values
        data[column_x] = pd.to_numeric(data[column_x], errors='coerce')

        # Create a box plot for the specified column_x
        plt.figure(figsize=(10, 6))  
        sns.boxplot(y=column_x, data=data)
        plt.title(f"Box Plot for '{column_x}'")
        plt.xlabel("Data")
        plt.ylabel(column_x)

        path = f"{save_location}/{column_x}_{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  
    except ValueError as e:
        print(f"Error: {e}")

# Function to generate histogram and save as PNG
def histogram(data, column_name, save_location, graph):
    try:
        # Convert the column_name to numeric, handling non-numeric values
        data[column_name] = pd.to_numeric(data[column_name], errors='coerce')
        data[column_name].dropna(inplace=True)  # Drop NaN values

        plt.hist(data[column_name], bins=20, edgecolor='black')
        plt.title(f"Histogram for '{column_name}'")
        plt.xlabel("Value")
        plt.ylabel("Frequency")        
        path = f"{save_location}/{column_name}_{graph}.png"
        print(path)
        plt.savefig(path)
    except ValueError as e:
        print(f"Error: {e}")
    
#Piechart
def pie_chart(data, column_name, save_location, graph):
    counts = data[column_name].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
    plt.title(f"Pie Chart for '{column_name}'")    
    path = f"{save_location}/{column_name}_{graph}.png"
    print(path)
    plt.savefig(path)


# Function to generate contour plot and save as PNG
def contour_plot(data, column_x, column_y, save_location, graph):
    try:
        # Convert columns to numeric, handling non-numeric values
        data[column_x] = pd.to_numeric(data[column_x], errors='coerce')
        data[column_y] = pd.to_numeric(data[column_y], errors='coerce')

        # Drop NaN values
        data = data.dropna(subset=[column_x, column_y])

        sns.kdeplot(data=data, x=column_x, y=column_y, fill=True, cmap='viridis')
        plt.title(f"Contour Plot for '{column_x}' vs '{column_y}'")
        plt.xlabel(column_x)
        plt.ylabel(column_y)

        path = f"{save_location}/{column_x}_vs_{column_y}_contour_{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  # Close the figure to prevent overlapping plots
    except ValueError as e:
        print(f"Error: {e}")


# Function to generate heatmap and save as PNG
def heatmap(data, save_location, graph):
    try:
        # Convert the data to numeric, handling non-numeric values
        data = data.apply(pd.to_numeric, errors='coerce')

        # Drop NaN values
        data = data.dropna()

        sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
        plt.title("Heatmap of Correlation Matrix")
        
        path = f"{save_location}/heatmap_{graph}.png"
        print(path)
        plt.savefig(path)
        plt.close()  # Close the figure to prevent overlapping plots
    except ValueError as e:
        print(f"Error: {e}")




def main():
    directory_path = './uploads'
    graph = sys.argv[1]
        
    save_location = "graphs"
    # Checks for any CSV file in the directory
    csv_files = [file for file in os.listdir(directory_path) if file.endswith('.csv')]

    # Check if exactly one CSV file is found
    if len(csv_files) != 1:
        print("Error: Exactly one CSV file should be present in the 'uploads' directory.")
        sys.exit(1)

    csv_file = csv_files[0]
    csv_file_path = os.path.join(directory_path, csv_file)

    #checking if file exists
    if not os.path.isfile(csv_file_path):
        print(f"Error: CSV file '{csv_file}' not found.")
        sys.exit(1)
    
    #reading
    try:
        df = pd.read_csv(csv_file_path)
    except pd.errors.EmptyDataError:
        print("Error: CSV file is empty.")
        sys.exit(1)
    except pd.errors.ParserError:
        print("Error: Unable to parse CSV file.")
        sys.exit(1)
    
    #generating graphs
    if graph == "Scatter Plot":
        x_column = sys.argv[2]
        y_column = sys.argv[3]
        scatter_plot(df, x_column, y_column, save_location, graph)
    elif graph == "Line Graph":
        x_column = sys.argv[2]
        y_column = sys.argv[3]
        line_graph(df, x_column, y_column, save_location, graph)
    elif graph == "Bar Graph":
        x_column = sys.argv[2]
        y_column = sys.argv[3]
        bar_graph(df, x_column, y_column, save_location, graph)
    elif graph == "Box Plot":
        x_column = sys.argv[2]
        box_plot(df,x_column, save_location, graph)
    elif graph == "Histogram":
        x_column = sys.argv[2]
        histogram(df, x_column, save_location, graph)
    elif graph == "Pie Chart":
        x_column = sys.argv[2]
        pie_chart(df, x_column, save_location, graph)
    elif graph == "Contour Plot":
        x_column = sys.argv[2]
        y_column = sys.argv[3]
        contour_plot(df, x_column, y_column, save_location, graph)
    elif graph == "Heat Map":
        heatmap(df, save_location, graph)

main()

