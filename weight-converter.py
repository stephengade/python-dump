
# weight converter

user_weight = input("what is your weight? ")
weight_unit = input("is the weight in Kg (K) or pounds (L)? ")

if weight_unit.upper() == "L":
    weight_result = int(user_weight) * 0.454
    result_unit = "kilogrammes"
else:
    weight_result = int(user_weight) * 2.205
    result_unit = "pounds"
print(f'You weight is {weight_result} in {result_unit}')