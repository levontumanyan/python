import re

logs = []

with open('sample_log.txt', 'r') as log_file:
	#print(logs)
	for line in log_file:
   #match = re.search(r"^(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) ([A-Z]+) ([\w\s]+)", line)
		match = re.search(r"^([A-Z][a-z]{2})  (\d) (\d{2}:\d{2}:\d{2}) (.*)", line)
		if match:
			log = {
				"date": { "month": match.group(1), "day": match.group(2) },
				"time": match.group(3),
				"message": match.group(4)
			}
			logs.append(log)


#print(logs)
#print(len(logs))
print(logs)




#with open('file.txt', 'r') as file:
#    for line in file:
#        print(line)