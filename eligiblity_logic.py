from flask import Flask, render_template, request
import gspread
from google.oauth2.service_account import Credentials

#Creating app
app = Flask(__name__)

#Calling spreadsheets
spreadsheet_name = "file_name"
sheet_name = "sheet_name"

#API Credentials
credentials = Credentials.from_service_account_file('name.json')
scoped_credentials = credentials.with_scopes(['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
client = gspread.Client(auth=scoped_credentials)

#Opening sheet
spreadsheet = client.open(spreadsheet_name)

#Naming sheets
eligibility_sheet = spreadsheet.worksheet(sheet_name)

@app.route('/', methods=['GET', 'POST'])
def eligibility_check():
    if request.method == 'POST':
        #Save data from eligibility_check
        client_first_name = request.form['client_first_name']
        client_last_name = request.form['client_last_name']
        birthday = request.form['birthday']
        life_expectancy = request.form['life_expectancy']
        enrolled_agency = request.form['enrolled_agency']
        covid_status = request.form['covid_status']
        weight = request.form['weight']
        dnr_status = request.form['dnr_status']
        attorney_status = request.form['attorney_status']
        hospice_plan = request.form['hospice_plan']
        agreement = request.form['agreement']
        phone = request.form['phone']
        email = request.form['email']

        #Logic for reason of ineligibility
        reason = ""
        #If reason exists, save reason and provide explanation to user
        if int(life_expectancy) > 6:
            reason = "Guests are required to have a life expectancy of 6 months or less."
        elif enrolled_agency.lower() == "n/a":
            reason = "Guests are required to be enrolled with one of the listed agencies."
        elif covid_status.lower() != "yes":
            reason = "Guests must be COVID negative at the time of admission."
        elif int(weight) > 300:
            reason = "Guest weight is required to be below 300lbs."
        elif dnr_status.lower() != "yes":
            reason = "Guests are required to have a 'Do Not Resuscitate'."
        elif attorney_status.lower() != "yes":
            reason = "Guests are required to have a Durable Power of Attorney'."
        elif hospice_plan.lower() != "yes":
            reason = "Guests are required to have a hospice plan in case of discharge."
        elif agreement.lower() != "yes":
            reason = "Guests and their family/friends are required to agree on the purpose of admission, hospice care plan, and projected length of stay."

        if reason:
            #Append ineligible users to Eligible sheet
            eligibility_sheet.append_row([client_first_name, client_last_name, "Ineligible", enrolled_agency, birthday, reason, weight+"lbs", phone, email])
            #Ineligible message
            return "The guest is ineligible for the Care Center but may be reconsidered. \nPlease contact (xxx) xxx-xxxx or xxxx@xxx.xxx if you want additional information."

        #Appending eligible users to Eligible sheet
        eligibility_sheet.append_row([client_first_name, client_last_name, "Eligible", enrolled_agency, birthday, " ", weight+"lbs", phone, email])

        #Eligible message to user
        return "Congratulations! The guest is eligible to stay at Care Center.\nLook for a call from (xxx) xxx-xxxx or an email from xxx@xxx.xxx soon!"

    #Returning info to eligibility_template.html
    return render_template('eligibility_template.html')


#Running application locally
if __name__ == '__main__':
    app.debug = True
    app.run(port=8123, use_reloader=False)
