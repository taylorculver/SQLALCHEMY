'''1) Setup the Engine and MetaData'''
# Import create_engine, MetaData
from sqlalchemy import create_engine, MetaData

# Define an engine to connect to chapter5.sqlite: engine
engine = create_engine('sqlite:///chapter5.sqlite')

# Initialize MetaData: metadata
metadata = MetaData(engine)


'''2) Create the Table to the Database'''
# Import Table, Column, String, and Integer
from sqlalchemy import Table, Column, String, Integer

# Build a census table: census
census = Table('census', metadata,
               Column('state', String(30)),
               Column('sex', String(1)),
               Column('age', Integer()),
               Column('pop2000', Integer()),
               Column('pop2008', Integer()),)

# Create the table in the database
metadata.create_all(engine)


'''3) Reading the Data from the CSV'''
import csv

with open('census.csv', newline='') as file:
    csv_reader = csv.reader(file, delimiter=',', quotechar='"')

    # Create an empty list: values_list
    values_list = []

    # Iterate over the rows
    for row in csv_reader:
        # Create a dictionary with the values
        data = {'state': row[0], 'sex': row[1], 'age': row[2], 'pop2000': row[3], 'pop2008': row[4]}
        # Append the dictionary to the values list
        values_list.append(data)


'''4) Load Data from a list into the Table'''
# Import insert
from sqlalchemy import insert

# Build insert statement: stmt
stmt = insert(census)

# Use values_list to insert data: results
connection = engine.connect()
results = connection.execute(stmt, values_list)

# Print rowcount
print(results.rowcount)




