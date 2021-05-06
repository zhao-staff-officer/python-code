cars=100
space_in_a_car=4.0
drivers =30
passengers =90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capactity=cars_driven * space_in_a_car
average_passengers_per_car=passengers/cars_driven

print("There are",cars,"cars available")
print("there are only",drivers,"drivers availables")
print("there will be",cars_not_driven,"empty cars today.")
print("we can transport",carpool_capactity,"people today.")
print("wen have",passengers,"to carpool today.")
print("wen need to put about",average_passengers_per_car,"in each car.")
