# Usage

AKiPS set up

* Should access admin account
1. Admin >> API >> Web API Settings

  1. Site Script Functions (On)
  2. Unused Interfaces (On)
  
2. Admin >> API >> Site scripting

  1. Paste perl code(siteScript.pl) into left panel and save
  
3. Set the file path of report properly in your environment in AKiPS_report.py file

with open(r'P:\Script\AKiPS_Report\Unused_Interface.csv', 'w', newline='') as csvFile:
