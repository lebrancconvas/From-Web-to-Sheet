from oauth2client.service_account import ServiceAccountCredentials
import gspread


scope = ['https://www.googleapis.com/auth/spreadsheets.readonly'] 

credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
gc = gspread.authorize(credentials)

sheet = gc.open_by_url("https://docs.google.com/spreadsheets/d/15eJoqC8c6k1BkMXMU2epuuIE9dt4JblwRX96KgfNF0A/edit?usp=sharing")

worksheet = sheet.get_worksheet(0)

print(worksheet.get_all_values()) 