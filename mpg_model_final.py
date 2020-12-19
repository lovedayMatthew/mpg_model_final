#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
cost_per_gallon = float(input("Enter cost per gallon: \t"))
# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)
tgs = round(gallons_used * cost_per_gallon,1)
cpm = round (cost_per_gallon/mpg,1 )
            
# format and display the result
print()
print("Miles per gallon:\t\t" + str(mpg))
print ("Total gas cost:\t\t"+ str(tgs))
print ("Cost per mile:\t\t"+str(cpm))
print()
print("Bye")


