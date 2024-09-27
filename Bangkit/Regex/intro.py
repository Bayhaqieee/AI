import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])


log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

result1 = re.search(r"aza", "plaza")
print(result1)

result2 = re.search(r"aza", "bazaar")
print(result2)

result3 = re.search(r"aza", "maze")
print(result3)

print(re.search(r"^x", "xenon"))