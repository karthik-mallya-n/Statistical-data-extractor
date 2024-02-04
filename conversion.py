import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

#*********csv conversion**************
# Read CSV
df = pd.read_csv('your_file.csv')

# Convert to Parquet
df.to_parquet('output_file.parquet')

# Convert to Arrow
table = pa.Table.from_pandas(df)
pa.parquet.write_table(table, 'output_file.arrow')

# Convert to JSON
df.to_json('output_file.json', orient='records', lines=True)

# Convert to TSV
df.to_csv('output_file.tsv', sep='\t', index=False)

# Convert to Excel
df.to_excel('output_file.xlsx', index=False, engine='openpyxl')
#**********parquet**************************

# Read Parquet
table = pq.read_table('your_file.parquet')
df = table.to_pandas()

# Convert to CSV
df.to_csv('output_file.csv', index=False)

# Convert to Arrow
table = pa.Table.from_pandas(df)
pa.parquet.write_table(table, 'output_file.arrow')

# Convert to JSON
df.to_json('output_file.json', orient='records', lines=True)

# Convert to TSV
df.to_csv('output_file.tsv', sep='\t', index=False)

# Convert to Excel
df.to_excel('output_file.xlsx', index=False, engine='openpyxl')
#*****************arrow*********


# Read Arrow
table = pq.read_table('your_file.arrow')
df = table.to_pandas()

# Convert to CSV
df.to_csv('output_file.csv', index=False)

# Convert to JSON
df.to_json('output_file.json', orient='records', lines=True)

# Convert to TSV
df.to_csv('output_file.tsv', sep='\t', index=False)

# Convert to Excel
df.to_excel('output_file.xlsx', index=False, engine='openpyxl')
#*************json********************


# Read JSON
df = pd.read_json('your_file.json', lines=True)

# Convert to CSV
df.to_csv('output_file.csv', index=False)

# Convert to Parquet
df.to_parquet('output_file.parquet')

# Convert to Arrow

table = pa.Table.from_pandas(df)
pa.parquet.write_table(table, 'output_file.arrow')

# Convert to TSV
df.to_csv('output_file.tsv', sep='\t', index=False)

# Convert to Excel
df.to_excel('output_file.xlsx', index=False, engine='openpyxl')

#************************tsv******************************

# Read TSV
df = pd.read_csv('your_file.tsv', sep='\t')

# Convert to CSV
df.to_csv('output_file.csv', index=False)

# Convert to Parquet
df.to_parquet('output_file.parquet')

# Convert to Arrow

table = pa.Table.from_pandas(df)
pa.parquet.write_table(table, 'output_file.arrow')

# Convert to JSON
df.to_json('output_file.json', orient='records', lines=True)

# Convert to Excel
df.to_excel('output_file.xlsx', index=False, engine='openpyxl')
