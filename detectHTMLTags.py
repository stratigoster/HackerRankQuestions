# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
a = set()
output=""
n = int(raw_input())
for i in range(0,n):
    line = raw_input()
    input = re.split("(<\w.*?>)", line)
    for x in input:
        m = re.search("<([^/].*?)[\s>]", x)
        if m:
            a.add(str(m.group(1)))
output = sorted(a)
empty = ""
for i in output:
    empty += i + ";"
    
size = len(empty)
print(empty[0:size-1])