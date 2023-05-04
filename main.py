import json
from file_reader import read_file

# Load the config file
with open('config.json', 'r') as f:
    config = json.load(f)

# Read the content of the source file
source_file = config['source_file']
content = read_file(source_file)

# Create the destination file
destination_file = config['destination_file']
with open(destination_file, 'w') as f:
    # Write the keys of the dictionary to the first line of the file
    f.write(','.join(content.keys()) + '\n')
    
    # Write the values of the dictionary to the second line of the file
    f.write(','.join(content.values()) + '\n')

