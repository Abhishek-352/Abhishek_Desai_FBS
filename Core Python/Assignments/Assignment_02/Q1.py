# Convert the time entered in hh,min and sec into seconds. 

h=int(input("Hours: "))
m=int(input("Minutes: "))
s=int(input("Seconds: "))

sec1=h*3600
print('\n'"Total seconds in Hours: ",sec1)

sec2=m*60
print("Total seconds in Minutes: ",sec2)

sec3=s
print("Total Seconds: ",sec3)

total=sec1+sec2+sec3
print('\n'"Total Seconds from given Hours, Minutes, secconds: ",total)