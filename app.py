import os

# Define shared mount path
shared_path = '/mount/storage/notshare'
shared_path2 = '/mount/storage/notshare/container2'
input_file = os.path.join(shared_path, 'input.txt')
output_file = os.path.join(shared_path, 'output.txt')

try:
    # Read from input file
    with open(input_file, 'r') as f:
        content = f.read()
        print(f"Read from {input_file}: {content}")

    # Write to output file
    with open(output_file, 'w') as f:
        f.write(f"Processed content: {content}")
        print(f"Wrote to {output_file}")

except Exception as e:
    print(f"Error: {e}")
