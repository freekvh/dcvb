#! /usr/bin/python3
import os
import yaml
import subprocess

# For now hardcode the destination, will fix this later
backup_destination = os.path.join(
    '/', 'data', '0', 'Backups', 'docker-compose-backups'
    )

# Load the docker-compose.yaml file
with open('docker-compose.yaml', 'r') as yf:
    dc = yaml.load(yf, Loader=yaml.FullLoader)

# create a services:volumes dictionary, only include services that have volumes
services = {
    service:dc['services'][service]['volumes'] for service in dc['services']
    if 'volumes' in dc['services'][service]
    }

# For every services rsync the all volumes to the destination
for service in services:
    print('For service', service)
    for volume in services[service]:
        volume = volume.split(':')[0]
        if volume.startswith('./'):
            abspath_volume = os.path.abspath(volume)
            destination = os.path.abspath(
                os.path.join(backup_destination, volume)
                )
            print('Backing up', abspath_volume, '->', destination)
            subprocess.check_call(' '.join([
                'mkdir -p', destination
                ]), shell=True)
            subprocess.check_call(' '.join([
                'rsync -ax --delete --relative', abspath_volume, destination
                ]), shell=True)
        else:
            print('skipping', volume)
    print('---')

print('Done.')
