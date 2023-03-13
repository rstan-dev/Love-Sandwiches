import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')


def get_sales_data():
    """
    Get sales figures input from the user
    """
    print("Please enter sales data from the last market")
    print("Data should be 6 numbers, seperated by commas.")
    print("Example: 10,11,12,16,19,5\n")

    data_str = input("Enter your data here:")

    sales_data = data_str.split(",")
    validate_data(sales_data)

def validate_data(values):
    """
    inside the try / except statement -  converts all string values to integers, raises a ValueError if strings can't be converted to int or if there is not exactly 6 values
    """
    try:
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values are required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}. Please try again.\n")



    

get_sales_data()