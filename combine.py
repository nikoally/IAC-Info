import os

# The path to the directory where the .md files are stored
module_dir = 'modules'

# The path to the new master .md file
output_file_path = 'master.md'

# Get the list of all markdown files in the directory
markdown_files = [f for f in os.listdir(module_dir) if f.endswith('.md')]

# Open the output file
with open(output_file_path, 'w') as master_file:
    # Iterate over all markdown files
    for markdown_file in markdown_files:
        # Open each markdown file
        with open(os.path.join(module_dir, markdown_file), 'r') as input_file:
            # Write the content of the input file to the output file
            master_file.write(input_file.read())
            # Write a page break (two newlines) to the output file
            master_file.write('\n\n')

print("Master markdown file has been created at:", output_file_path)
