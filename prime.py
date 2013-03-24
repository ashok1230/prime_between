class prime:
   def __init__(self):
	count=0
	low_limit=int(raw_input('enter lower limit'))
	up_limit=int(raw_input('enter upper limit'))
	print 'prime numbers are:'
	if low_limit<up_limit:
	    for i in range(low_limit,up_limit):
		for j in range(2,i/2+1):
		    if i%j==0:
		        break
	        else:
		    print i,
		    count+=1
	    print '\nprime numbers between ',low_limit,' and ',up_limit,' are ',count
	else:
	   print 'numbers you enter are wrong and lower limit must less than upper limit'

a=prime()
