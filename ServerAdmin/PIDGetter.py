import psutil
import argparse

parser = argparse.ArgumentParser(description='Find Process')
parser.add_argument('-n', '--name', help = 'Name of File', action='store')
args = parser.parse_args()

processes = psutil.process_iter(attrs=['pid', 'name'])

process = [p.info for p in processes if args.name in p.info['name']]

print(process)
