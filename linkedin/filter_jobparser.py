import sys
import pandas as pd

def main(filename):
	print(f"Processing filename: {filename}")
	# Load the CSV file
	df = pd.read_csv(filename)

	# We will reindex and drop the following columns
	"""
	description
	site
	salary_source  
	interval  
	min_amount  
	max_amount  
	currency  
	listing_type  
	company_logo  
	company_addresses  
	company_num_employees  
	company_revenue  
	company_description
	"""

	# Only show the following columns in the following order
	columns = ['id', 'title', 'job_url', 'company', 'date_posted', 'job_level', 'job_type','emails', 'job_url_direct', 'is_remote', 'location', 'job_function', 'company_industry', 'company_url', 'company_url_direct']
	df = df.reindex(columns=columns)

	# Sort by date posted
	df = df.sort_values(by='date_posted', ascending=False)
	
	# Set 'id' column as the index
	df.set_index('id', inplace=True)
	df.to_csv(filename, index=False)

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print("Usage: python3 your_script.py <filename>")
		sys.exit(1)
	main(sys.argv[1])
