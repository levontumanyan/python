import threading
import time

# Global variable to store the result
result = None

# Function for the calculation thread
def calculate():
    global result
    print("Calculating...")
    # Simulate a time-consuming calculation
    time.sleep(3)
    result = 42  # Store the result in the global variable
    print("Calculation complete")

# Function for the task thread
def perform_tasks():
    while result is None:
        print("Performing tasks while waiting for calculation...")
        time.sleep(1)
    print(f"Result from calculation: {result}")
    # Continue with other tasks using the result

# Create threads
calculation_thread = threading.Thread(target=calculate)
tasks_thread = threading.Thread(target=perform_tasks)

# Start threads
calculation_thread.start()
tasks_thread.start()

# Wait for both threads to finish
calculation_thread.join()
tasks_thread.join()

print("All threads are done.")
