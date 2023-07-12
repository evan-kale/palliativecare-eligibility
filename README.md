# palliativecare-eligibility
Originally built as an eligibility checker for potential guests/referrers at The Bird House, an Iowa City palliative care center

Testing Instructions for Local Hosting

1. Create a new folder on desktop
2. Download eligibility_logic.py and eligibility_template.html into the new folder
3. Create a new folder within the folder and name it “templates”
4. Place eligibility_template.html into “templates”
5. Create a new project at https://console.cloud.google.com
6. In the top left, select Navigation Menu and go to IAM & Admin
7. Click on Service Accounts and create one (make name what you want)
8. Click on the new service account email
9. Go to Keys, Add key, Create new key, JSON
10. Save JSON into the new folder you created
11. In the search bar at the top of the page, search “Google Drive API” and scroll to the exact result under the “marketplace” heading
12. Click enable and let it load
13. Search “Google Sheets API” and repeat steps 11 and 12
14. Modify the .py file so it contains the corresponding google sheet file name, sheet name, and .json file name. Also modify code as needed
15. Share the Google Sheet file with the service account email as an Editor
16. Open eligibility_logic.py and eligibility_template.html in your IDE
17. In FlaskApp.py type “pip install gspread google-auth” and then “pip install flask” into the console. It should take a few seconds to install each package
18. Run script, console should display locally hosted URL named https://127.0.0.1:8123
19. Copy link and paste into a browser while script is running


Instructions for Live Application

1. Deploy Python Flask App on Pythonanywhere.com
Great resource: https://www.youtube.com/watch?v=6p7GBfHgJq8&t=308s

