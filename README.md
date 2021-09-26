# Contorion
Test
UI_Automation
Automation suite for UI functional testing.
Basically the project contains Automation scripts for Contorion website which runs on local system which basically consists of login and search operations.

Pre-requisites
In order to run the automation script Python3 and pip should be pre-installed and below libraries should be installed. pip install pytest-html pip install selenium pip install pytest pip install logging  pip install openpyxl
Web Browsers & Web Drivers: Web Browsers: Safari, Chrome, Firefox, IE, Opera, Download webdrivers for the above browsers & put them in the Path variables.
IDE: PyCharm & Command Prompt(Windows)

Steps to run the Automation Script
1.	Cloning the repo from GitHub
https://github.com/rajeevpatil24/UI_Automation.git
2.	Go to the path where above repo has been cloned, open the repo in an IDE Open terminal in IDE and run below command
pytest -v -s --html=Report\reports.html TestCases/test_loginSearch.py
pytest -v -s --html=Report\loginNegative.html TestCases/test_login_Negative.py
test_loginSearch.html file which you one can open in a browser of their choice, log file is also hosted here and screen shots also.
https://github.com/suryapriyankach/Contorion.git
