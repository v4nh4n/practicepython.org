import json
from collections import Counter #didnt use it

with open("info.json","r+") as f:
    info = json.load(f)
res = {
    "JANUARY":0,
    "FEBRUARY":0,
    "MARCH":0,
    "APRIL":0,
    "MAY":0,
    "JUNE":0,
    "JULY":0,
    "AUGUST":0,
    "SEPTEMBER":0,
    "OCTOBER":0,
    "NOVEMBER":0,
    "DECEMBER":0
    }
for i in info:
    month = info[i][:2]
    if month=="01":
        res["JANUARY"]+=1
    elif month=="02":
        res['FEBRUARY']+=1
    elif month=="03":
        res['MARCH']+=1
    elif month=="04":
        res['APRIL']+=1
    elif month=="05":
    	res['MAY']+=1
    elif month=="06":
    	res['JUNE']+=1
    elif month=="07":
    	res['JULY']+=1
    elif month=="08":
    	res['AUGUST']+=1
    elif month=="09":
    	res['SEPTEMBER']+=1
    elif month=="10":
    	res['OCTOBER']+=1
    elif month=="11":
    	res['NOVEMBER']+=1
    elif month=="12":
    	res['DECEMBER']+=1

print(res)


