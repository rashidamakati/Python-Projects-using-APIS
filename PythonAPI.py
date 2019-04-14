# Write a python program that takes input from a file and outputs to another file. The input file consists of n lines. Each line will be comma separated values. The first work will be an IP address followed by various key attributes.
# The output will be a file which has n lines in a comma separated values. The first word will be the ip address followed by values of the key attributes from the input file for that ip address.
# Use this api to get information for that IP.
# https://ipapi.co/api/#introduction
#
# Input file and output file name will be give via command line parameters. You must write your own function to validate the IP address. Your code must use object oriented classes and objects as much as possible.
#
# If IP is not valid, output line must say INVALID IP
# If any key attribute is not valid for any input IP, output must say INVALID KEY for that key value.
# If key attributes values are comma separated, you must replace comma with :
#
# Eg.
# $ ip_info.py input.txt output.txt
#
# input.txt-
# 8.8.8.8,city,region,country,postal
# 123.10.100.50,asn,org,in_eu,region_code
# 600.40.12.100,timezone,utc_offset,asn,org
# 5.225.26.154,postal,languages,public
#
# output.txt-
# 8.8.8.8,Mountain View,California,United States,94035
# 123.10.100.50,AS4837,CHINA UNICOM China169 Backbone,false,null
# INVALID IP
# 5.225.26.154,15572,es-ES:ca:gl:eu:oc,INVALID KEY

from requests import get
import json
import socket
collective_data = []
def main():
    with open("input.txt") as file:
        for lines in file:
            line_data = lines[:-1]
            split_data = line_data.split(',')
            ipaddress = split_data[0]
            ipvalid = validateIP(ipaddress)
            collect_data = [ipaddress]
            if ipvalid:
                for j in range(1,len(split_data),1):
                    valueip = get('https://ipapi.co/'+str(ipaddress)+'/'+str(split_data[j])+'/').text
                    if 'Not Found' in valueip or valueip == 'Undefined':
                        valueip = 'INVALID KEY'
                    if ',' in valueip:
                        split_data1 = valueip.split(',')
                        valueip = ':'.join(split_data1)
                    collect_data.append(valueip)
                collective_data.append(collect_data)
            else:
                collective_data.append(['INVALID IP'])

    file.close()
    with open('output.txt', 'w') as f:
        for item in collective_data:
            item = ','.join(item)
            f.write("%s\n" % item)

def validateIP(ipdata):
    try:
        socket.inet_aton(ipdata)
        return True
    # legal
    except socket.error:
        return False
    # Not legal

if __name__ == "__main__":
    main()
