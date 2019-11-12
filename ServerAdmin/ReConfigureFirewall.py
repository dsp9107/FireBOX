import sys
import os

if sys.platform == "linux" :
    os.system("sudo ufw --force disable")
    os.system("sudo ufw --force reset")
    os.system("sudo ufw default reject incoming")
    os.system("sudo ufw default allow outgoing")
    os.system("sudo ufw default reject routed")
    os.system("sudo ufw limit ssh")
    os.system("sudo ufw allow dns")
    os.system("sudo ufw allow 67")
    os.system("sudo ufw allow 9107")
    os.system("sudo ufw --force enable")

print("Firewall Configured")
