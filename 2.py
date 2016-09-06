i = int (input('profit:'))
arr = [100,60,40,20,10,0]
rat =[0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idex in range(0,6):
	 if i > arr[idex]:
		 r+=(i-arr[idex])*(rat[idex])
		 i=arr[idex]
print (r)
