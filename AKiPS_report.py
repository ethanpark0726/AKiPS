import requests
import openpyxl

# Getting unused Interface section
# First, make a hash table of devices
response = requests.get('server-name/api-script?password=yourpassword;function=web_export_device_list;', verify=False)
deviceHash = {}

for elem in response.text.splitlines():
    device, ipv4 = elem.split(',')

    if device.startswith('P') == False:
        deviceHash[device] = ipv4

print('--- Hash table has been created!')

# Second, create a report combining with hashtable above
response = requests.get('server-name/api-unused-interfaces?password=yourpassword;', verify=False)

with open(r'P:\Script\AKiPS_Report\Unused_Interface.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(['Device', 'IPv4 Address', 'Interface', 'State', 'Description'])

    for elem in response.text.splitlines():
        line = elem.split(',')
            
        if line[4].startswith('up') or line[0].startswith('P') != False:
            continue
        else:
            writer.writerow([line[0], deviceHash.get(line[0]), line[1], line[4], line[6]])
