# Program which converts miles to KM
# Author: Mike Audam 
# CSD-325

#Prompting user for number of miles driven
num_miles = float(input("Enter number of miles: "))

# Function which converts miles to KM (~ 1.6 km == 1 mile)
def convert_distance(num_miles):
	km = num_miles * 1.6  
	return km
distance_km = 0

# Convert miles to kilometers referencing convert_distance()
distance_km = convert_distanse(num_miles)

# Calculate the total distance in miles and kilometers
print("The total distance in miles is " + str(num_miles))
print("The total distance in kilometers is " + str(distance_km))