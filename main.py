import subprocess
import sys

def main(zip_filename):
    # Step 1: Unzip
    subprocess.call(['python', 'a04_unzip.py', zip_filename])

    # Step 2: Compile and Run
    subprocess.call(['python', 'complile_run.py'])

    # Step 3: Compare
    subprocess.call(['python', 'compare.py'])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python full_process.py <zip_file>")
    else:
        main(sys.argv[1])