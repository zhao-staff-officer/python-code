def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have{cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("we can just give the function numbers directly:")
cheese_and_crackers(20,30)

print("Or, we can use variables form our script:")
amout_of_cheese = 10
amout_of_crackers = 50

cheese_and_crackers(amout_of_cheese,amout_of_crackers)

print("wen can even do math inside too:")
cheese_and_crackers(10+20,5+6)

print("And we can combine the two,variables and math")
cheese_and_crackers(amout_of_cheese+100,amout_of_crackers+10000)
