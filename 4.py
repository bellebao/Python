year = int(input('year:'))
month = int(input('month:'))
day = int(input('day:'))

day1 = [31,28,31,30,31,30,31,31,30,31,30,31]
day2 = [31,29,31,30,31,30,31,31,30,31,30,31]
i=0
datnum=0
if year%4==0:
	for i in range (0, month-1):
	    datnum +=day2[i]
else:
	for i in range (0, month-1):
	    datnum +=day1[i]

datnum = datnum + day
print (datnum)
