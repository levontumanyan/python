import threading

def worker():
	print('this code is running in a thread')

# create a thread
worker_thread = threading.Thread(target=worker)
worker_thread.start()
