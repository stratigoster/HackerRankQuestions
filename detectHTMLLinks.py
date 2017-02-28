import re
n = int(raw_input())
for i in range(0,n):
    input1 = raw_input()
    input = re.split("(<a href.*?</a>)", input1)
    for i in input:
        searchObj = re.search( r'<a href="(.*?)".*?>\s{0,1}(.*?)</a>.*?', i, re.M|re.I)
        if searchObj:
            if searchObj.group(2).startswith("<b>"):
                string = searchObj.group(2)
                whoCares = string[3:8]
                print searchObj.group(1) + ',' + whoCares
            elif searchObj.group(2).startswith("<"):
                print searchObj.group(1) + ','
            else:
                print searchObj.group(1) + ',' + searchObj.group(2)