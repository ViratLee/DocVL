import subprocess
results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = results.decode("ascii") # needed in python 3
#print(results)
results = results.replace("\r","")
print(results)
# ls = results.split("\n")
# ls = ls[4:]
# ssids = []
# x = 0
# while x < len(ls):
#     if x % 5 == 0:
#         ssids.append(ls[x])
#     x += 1
# print(ssids)