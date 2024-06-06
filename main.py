import subprocess

# Run the add_ga.py script
try:
    subprocess.run(['python', 'add_ga.py'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running add_ga.py: {e}")
    exit(1)

# Run the Streamlit app
try:
    subprocess.run(['streamlit', 'run', 'app.py'], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error occurred while running the Streamlit app: {e}")
    exit(1)
