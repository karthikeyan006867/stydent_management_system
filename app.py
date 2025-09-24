from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__, template_folder='../templates', static_folder='../static')

# Google Sheets setup
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client = gspread.authorize(creds)
sheet = client.open("StudentSheet").sheet1  # Replace with your sheet name

@app.route("/", methods=['GET'])
def home():
    students = sheet.get_all_records()
    return render_template('index.html', students=students)

@app.route("/add_student", methods=['POST'])
def add_student():
    name = request.form['name']
    roll = request.form['roll']
    clas = request.form['class']
    sheet.append_row([name, roll, clas])
    return redirect("/")

def handler(request):
    return app(request)