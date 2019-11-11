import sys
import argparse

parser = argparse.ArgumentParser(description='Print Name')
parser.add_argument('-a', '--allow', help = 'Allow An IP', action='store_true')
parser.add_argument('-d', '--deny', help = 'Deny An IP', action='store_true')
parser.add_argument('-i', '--ip', type = str, help = 'IP Address', required=True)

args = parser.parse_args()

if args.allow == args.deny :
    parser.error('Specify One Option')

elif args.allow :
    if sys.platform == 'linux' :
        os.system(f"sudo ufw allow out from any to {args.ip} port 443")
    print(f"{ip} Is Allowed To Access Internet Securely")

elif args.deny :
    if sys.platform == 'linux' :
        os.system(f"sudo ufw deny out from any to {args.ip} port 443")
    print(f"{ip} Is Not Allowed To Access Internet")
