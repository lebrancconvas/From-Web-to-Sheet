from oauth2client.service_account import ServiceAccountCredentials
import gspread


def get_sheet_data():
	scope = ['https://www.googleapis.com/auth/spreadsheets'] 

	credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
	gc = gspread.authorize(credentials)

	sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/15eJoqC8c6k1BkMXMU2epuuIE9dt4JblwRX96KgfNF0A/edit?usp=sharing")

	worksheet = sheet.get_worksheet(0)

	print(worksheet.get_all_values()) 
 
def get_text_data():
  with open('../automation/data/output.txt') as f:
    contents = f.read()
    return contents


def data_management():
  text_data = get_text_data()
  print(text_data)

data_management()