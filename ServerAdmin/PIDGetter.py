import psutil

pname = 'a.py'

processes = psutil.process_iter(attrs=['pid', 'name'])

process = [p.info for p in processes if pname in p.info['name']]

print(process)
