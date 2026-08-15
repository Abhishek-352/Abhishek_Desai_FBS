# Convert distant given in feet and inches into meter and centimeter. 

feet=int(input("Enter your distance in feet: "))
inch=int(input("Enter your distance in inches: "))

meter=int(feet*0.3048)
centimeter=int(inch*2.54)

print('\n'"Your distance in meter is: ",meter,'m')
print("Your distance in centimeter is: ",centimeter,'cm')