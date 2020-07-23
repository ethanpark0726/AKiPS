# Creating a customized AKiPS report

  - Used AKiPS' site scripting (Perl script) & Web API
  - Created a report by Python
  - Report example

|Device|IPv4 Address|Interface|State|Description|
|:------:|:-----------:|:---------:|:-----:|:-----------:|
|Switch1|10.1.1.1|Gi2/17|down|UPLINK Switch2|
|Switch2|10.1.3.1|Gi1/1|up|UPLINK Switch3|


## Preset

  * AKiPS setting
    - Admin >> API >> Web API Settings
      - Site Script Functions & Unused Interfaces turn on
    - Admin >> API >> Site scripting
      - Paste perl code (siteScript.pl) into left panel and save
  * Python code setting (AKiPS_report.py)
    - Set the file path of report in your environment
```sh
with open(r'P:\Script\AKiPS_Report\Unused_Interface.csv', 'w', newline='') as csvFile:
```
