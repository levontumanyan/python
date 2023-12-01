import time
import threading
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

def square_numbers(numbers):
    results = []
    for num in numbers:
        results.append(num * num)
    return results

def run_single_thread(numbers):
    start_time = time.time()
    square_numbers(numbers)
    end_time = time.time()
    print(f"Single-threaded execution time: {end_time - start_time:.4f} seconds")
    
def run_threaded(numbers):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(square_numbers, [((1, numbers//2)), ((numbers//2, numbers))])
    end_time = time.time()
    print(f"Threaded execution time: {end_time - start_time:.4f} seconds")

def run_multi_thread(numbers):
    start_time = time.time()
    
    # Create two threads
    thread1 = threading.Thread(target=square_numbers, args=(numbers[:len(numbers)//2],))
    thread2 = threading.Thread(target=square_numbers, args=(numbers[len(numbers)//2:],))

    # Start both threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Multi-threaded execution time: {end_time - start_time:.4f} seconds")

def run_multi_process(numbers):
    start_time = time.time()

    # Create two processes
    process1 = multiprocessing.Process(target=square_numbers, args=(numbers[:len(numbers)//3],))
    process2 = multiprocessing.Process(target=square_numbers, args=(numbers[len(numbers)//3:],))
    process3 = multiprocessing.Process(target=square_numbers, args=(numbers[len(numbers)//3:],))

    # Start both processes
    process1.start()
    process2.start()
    process3.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()
    process3.join()

    end_time = time.time()
    print(f"Multi-process execution time: {end_time - start_time:.4f} seconds")

def run_multiprocess_better(numbers):
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=8) as executor:
        executor.map(square_numbers, [(1, numbers//2), (numbers//2, numbers)])
    end_time = time.time()
    print(f"Multiprocess execution time: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    # Create a large dataset
    #numbers = list(range(1, 100000001))
    numbers = 100000000000001

    # Run each method and measure the execution time
    # run_single_thread(numbers)
    # run_multi_thread(numbers)
    # run_multi_process(numbers)
    run_threaded(numbers)
    run_multiprocess_better(numbers)
    
