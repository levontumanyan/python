import requests
import threading
import time

# List of urls to download from
urls = ['https://www.cnn.com/us', 'https://www.cnn.com/world', 'https://www.cnn.com/world/americas', 'https://www.cnn.com/world/asia', 
		'https://www.cnn.com/world/australia', 'https://www.cnn.com/world/china', 'https://www.cnn.com/world/india',
		'https://www.cnn.com/world/europe']

# File path
file_path = 'example.txt'

def download_and_process(url):

	thread_id = threading.get_ident()
	print(f"Thread {thread_id} for {url} started.")
	start_time = time.time()
	# Download the data
	print(f"{thread_id}: Downloading data from {url}...")
	response = requests.get(url)
	data = response.text

	print(f"{thread_id}: Processing data from {url}...")
	# processing of the data
	processed_data = data.lower()

	end_time = time.time()
	print(f"{thread_id}: Data from {url} processed. Time taken: {end_time - start_time} seconds.")
	# Open the file in append mode
	with open(file_path, 'a') as file:
		# Append content to the file
		file.write(processed_data + "\n")

if __name__ == "__main__":
	threads = []
	for url in urls:
		download_thread = threading.Thread(target=download_and_process, args=(url,))
		threads.append(download_thread)
		download_thread.start()
	
	for thread in threads:
		thread.join()

print('All downloads completed')