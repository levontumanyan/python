import os
import multiprocessing

# Get the number of processors using os.cpu_count()
num_processors = os.cpu_count()

# Alternatively, you can use multiprocessing.cpu_count()
print('Number of processors: {}'.format(multiprocessing.cpu_count()))

print(f"Number of processors: {num_processors}")
