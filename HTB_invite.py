import re
import colored
import subprocess
import base64

red=colored.fg("red")
yellow=colored.fg("yellow")
purple=colored.fg("magenta")
reset=colored.attr("reset")

subprocess.call(["clear"])
print('''
Hi Friend
This Script For Automating HTB_invite Code using python ''')
print(yellow + "Scripted By: ")
print(purple + "             Script Kiddie Tamil"+reset)

curl=subprocess.check_output("curl -XPOST https://www.hackthebox.eu/api/invite/generate",shell=True)

basemsg=re.findall(r"\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w\w=",str(curl))
base64_string=basemsg[0]
print("\n")


base64_bytes = base64_string.encode("ascii")

sample_string_bytes = base64.b64decode(base64_bytes)
sample_string = red+sample_string_bytes.decode("ascii")

print(f"Your HTB Code : {sample_string}"+reset)