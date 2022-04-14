# import boto3
# import pandas
# import xlsxwriter
# import csv

# client = boto3.client('ec2')
# # regions = [region['RegionName'] 
# for region in client.describe_regions()['Regions']:
#     print(region['RegionName'])

#  # Write to csv file.
# header = ['RegionName']
# with open('regions-details.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=header)
#     writer.writeheader()
#     writer.writerows()

# # # list all the availability regions
# # import boto3

# # ec2 = boto3.client('ec2')

# # # Retrieves all regions/endpoints that work with EC2
# # response = ec2.describe_regions()
# # print('Regions:', response['Regions'])



# # # Retrieves availability zones only for region of the ec2 object
# # response = ec2.describe_availability_zones()
# # print('Availability Zones:', response['AvailabilityZones'])

from ensurepip import bootstrap
import boto3


l1=[]
session = boto3.Session()
services = session.get_available_regions(service_name='ec2')
for i in services:
    l1.append(i)
    print(i)
availZones = []
for kl in range(len(l1)):
    client=boto3.client('ec2',region_name=l1[kl])
    for zone in client.describe_availability_zones()['AvailabilityZones']:
        if zone['State'] == 'available':
            # availZones.append(zone['ZoneName'])
            print(zone['ZoneName'])
print(availZones)