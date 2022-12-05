
import sys
import questionary
from pathlib import Path
from qualifier.utils.fileio import save_csv

def save_qualifying_loans(qualifying_loans):
    """Saves the qualifying loans to a CSV file.

    Args:
        qualifying_loans (list of lists): The qualifying bank loans.
    """
    # if there are no qualifying loans, print "No qualifying loans" and exit save qualifying loans 
    if len(qualifying_loans) == 0:
        print("No Qualifying loans available, App will exit. No file was saved. ")
        exit
    # if there are qualifying loans, ask if results need to be saved
    else:
        # Ask for saving file if there are qualifying results
        save_file = questionary.confirm("There are qualifying loans available, would you like to save the results YES/NO?").ask()

        # If user does not want to save files, exit
        if save_file != True:
            # print whatever input user has given (if not yes) and highlight that app exited due to that. If user wants to save rerun process and answer yes when prompted. 
            print(f"app will exit, no file was saved by app.\
                 \nPlease rerun application and type Y when prompted to save qualifying loan results if results need to be saved.")
            exit
        # If user wants to save files, prompt where they would like to save the files
        else:
            # Determine folder path for new file to be saved in
            csvpath = questionary.text("Please enter output file path for the to be saved file:").ask()
#            csvpath = "./" + csvpath + "/"
            csvpath = Path(csvpath)
            if not csvpath.exists():
                sys.exit(f"Oops! Can't find this path: {csvpath}")
            
            # Determine file name for qualifying loan list
            file_name = questionary.text("Please enter file name for qualifying loan list (No file extention necessary):").ask()
            file_name = file_name + ".csv"
            
            print(f"File will be available in folder: \{csvpath}\ with file name: {file_name}")

            # Save file if user wants to save files in determined location and with determined file name
            csvpath = Path(csvpath, file_name)
            return save_csv(csvpath, qualifying_loans)
