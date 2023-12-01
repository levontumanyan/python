import threading
import time

def long_running_task():
    # Simulate a long-running task
    time.sleep(5)
    print("Task finished")

# Start the long-running task in a separate thread
thread = threading.Thread(target=long_running_task)
thread.start()

# Meanwhile, the main thread can continue executing other code
print("Main thread continues to execute")

