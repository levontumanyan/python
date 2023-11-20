import datetime
import os
import pandas as pd
import re

#how it should run:

# each month i will create an invoice for the previous month for myself
# this app will take a template file and create a new file monthly invoice based on the template
# the file name created will be of this form: Levon_Tumanyan_January_2021.csv
# the invoice will be a csv file with the following columns:
# how to find a particular cell and change the value of a cell below that cell
# how to find a cell based on regex and change the value of a cell below that cell


# Read the Excel file


# create the main python file structure here like if __name__ == "__main__": and then call the functions from there
def validate_year(year):
    # regex that matches a year format
    if not year:
        return False
    
    pattern = r"^(19|20)\d{2}$"
    if re.match(pattern, year):
        return True
    else:
        return False
    
def validate_month(month):
    # regex that matches a month format
    if not month:
        return False
    pattern = r"^(0[1-9]|1[012])$"
    if re.match(pattern, month):
        return True
    else:
        return False
    
def get_month_year():
    """This function will ask the user to enter the month and year for the invoice they want to create and then return the month and year"""

    print("Enter the month and year for the invoice you want to create, for example: 04 2021")
    month = input("Enter the month - (For example: 04) --- ")
    year = input("Enter the year - (For example: 2021) --- ")
    
    return month, year

def update_invoice_number(df):
    """This function will update the invoice number in the template file"""
    # both in the template and in the new excel file to be created
    # we will grab the current invoice number from the template file and then update it in the new file
    # grab the value of a cell in column INVOICE for Hanen Early Language Program and row 5
    # can possibly create a function that updates a cells value based on the column name and row number
    old_invoice_number = df.loc[2, 0]
    # strip spaces from the string
    old_invoice_number = old_invoice_number.strip()
    # convert the string to an integer
    old_invoice_number = int(old_invoice_number)
    # increment the integer by 1
    new_invoice_number = old_invoice_number + 1
    # convert the integer back to a string
    new_invoice_number = str(new_invoice_number)
    # update the value of the cell in column INVOICE for Hanen Early Language Program and row 5
    df.loc[2, 0] = new_invoice_number

    print("The new invoice number is: " + new_invoice_number)
    
    #df.loc[1, 'INVOICE for Hanen Early Language Program'] = ''
    #locate the cell in column INVOICE for Hanen Early Language Program and row 2 and then update the value of that cell
    #df.loc[2, 'INVOICE for Hanen Early Language Program'] = ''

def update_date_of_issue(df):
    """This function will update the date of issue in the template file"""
    # both in the template and in the new excel file to be created
    # create a date time object for the current date in the format of 2023-02-05 00:00:00
    current_date = datetime.datetime.now().date()
    current_datetime = datetime.datetime.combine(current_date, datetime.time.min)

    df.loc[2, 1] = current_datetime
    
    #df.loc[3, 'INVOICE for Hanen Early Language Program'] = new_date_of_issue

def generate_filename(month, year):
    return f'Levon_Tumanyan_{month}_{year}.xlsx'

def save_dataframe_to_excel_file(df, excel_file):
    """This function will save the dataframe to an excel file"""

    # with open(excel_file, 'wb') as f:
    #     # write the dataframe to the file as excel after decoding it from utf-8
    #     df.to_excel(f, index=False, encoding='utf-8')
    # Set the output directory
    # Get the current working directory
    cwd = os.getcwd()
    excel_file_path = os.path.join(cwd, "invoices")

    # Create the output directory if it doesn't exist
    if not os.path.exists(excel_file_path):
        os.makedirs(excel_file_path)

    # Define the output file path
    excel_file = os.path.join(excel_file_path, excel_file)

    # Save the DataFrame to an Excel file in the output directory
    df.to_excel(excel_file, index=False, header=False)

def main():
    # Load the template file
    df = pd.read_excel('Levon_Tumanyan_Template_Invoice.xlsx')
    print(df)

    df.columns = range(len(df.columns))


    # create a workshop loop here that will ask the user for the month and year and then create the invoice for that month and year
    # it will then continuesly ask to user to enter a new task in that invoice with the time spent on that task
    # Workshop Date, workshop start time, End time, Total Hours, Description, Program Id, Amount
    # it will then ask the user if they want to add another task to the invoice
    # if the user says yes then it will ask for the task details and then add it to the invoice
    # if the user says no then it will save the invoice and then ask the user if they want to exit the program or create another invoice
    # if the user says exit then it will exit the program
    # if the user says create another invoice then it will ask the user for the month and year and then create the invoice for that month and year
    # it will then continuesly ask to user to enter a new task in that invoice with the time details...


    # Main program loop
    while True:
        #now that we have the month and year we can create the invoice by updating the template file
        #we will use the month and year to update the INVOICE NUMBER, DATE OF ISSUE
        
        month, year = get_month_year()

        if not month or not year:
            continue

        if not validate_month(month):
            print("The month you entered is not valid, please enter a valid month")
            continue

        if not validate_year(year):
            print("The year you entered is not valid, please enter a valid year")
            continue
        
        # update the invoice number
        update_invoice_number(df)

        # update the date of issue
        update_date_of_issue(df)


        # if the program gets to this point then we can save the dataframe to an excel file
        excel_file = generate_filename(month, year)

        #save
        save_dataframe_to_excel_file(df, excel_file)



        date_of_issue = df.loc[2, 1]
        print(type(date_of_issue))
        print(df.loc[2, 1])

        # for debugging print the date cells value under the column Unnamed: 1

if __name__ == "__main__":
    #load_template()
    #create_invoice()
    main()
