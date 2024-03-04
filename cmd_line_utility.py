# Command Line Utility:
# This is a builtin module 
import argparse
import requests
# Now we download a file using request: 
def dowload_file(url, local_file_name):
    # local_file_name = url.split('/')[-1]
    # Note the stream= True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_file_name, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                #
                #
                f.write(chunk) 
    return local_file_name

# parser Instance = module_name with this class
parser = argparse.ArgumentParser()

# Add Command Line Utility
parser.add_argument("url", help="description of argument 1")
# parser.add_argument("output", help="by which name do you want to save your file: ")
parser.add_argument("-o", "--output", help="description of optional arguments", default=None)

# parse the argument:
args = parser.parse_args()

# Use the argument in your code
print(args.url)
print(args.output)
dowload_file(args.url, args.output)