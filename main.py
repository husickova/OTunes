import os

# Run the add_ga.py script
result = os.system('python add_ga.py')
if result != 0:
    print("Error occurred while running add_ga.py")
    exit(1)

# Run the Streamlit app
result = os.system('streamlit run app.py')
if result != 0:
    print("Error occurred while running the Streamlit app")
    exit(1)
