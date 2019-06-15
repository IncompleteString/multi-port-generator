starting_port = int(input("Enter your starting port number:"))
monitors = int(input("Enter your number of monitors:"))
https = int(input("If you use HTTPS enter 1:"))


##Leave everything below this line alone, unless you know what you are doing

P1 = starting_port+1
P2 = starting_port+1
M1 = monitors 
M2 = monitors 


PM = P1 + M1
PM2 = P2 + M2
space = " "



print (space)
print (space)
##Zoneminder Apache2 Virtual Host file port generator##
if https ==	1:
	print("Paste the following into your /etc/apache2/sites-available/000-default-le-ssl.conf OR default-ssl.conf at the line that begins with <VirtualHost *:443")
else:
	print("Paste the following into your /etc/apache2/sites-available/000-default.conf at the line that begins with <VirtualHost *:80")
print (space)
print (space)
while P1 < PM: 
	print ("*:",P1,space,sep='',end = '')
	P1 = P1+1

	
##line break#
print (space)
print (space)
	
	
##Zoneminder Apache2 ports.conf port generator##
if https ==	1:
	print("Paste the following into your /etc/apache2/ports.conf file at the line starting with listen 443")
else:	
	print("Paste the following into your /etc/apache2/ports.conf file at the line starting with listen 80")
	
print (space)
print (space)

while P2 < PM2:
	if https ==	1:
		print ("Listen",P2,"https")
	else:
		print ("Listen",P2)
	P2 = P2+1
	
	