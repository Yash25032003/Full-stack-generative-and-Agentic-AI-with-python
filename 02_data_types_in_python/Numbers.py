#INTEGERS

black_tea_grams = 17
ginger_grams = 4

total = black_tea_grams + ginger_grams

print(f"the total grams of black andginger is {total}")

remaining = black_tea_grams - ginger_grams
print(f"remaining black tea is {remaining} grams")

milk_liters = 7
serving = 4

serving_per = milk_liters / serving
print(f"serving per individual is {serving_per}")

total_tea_bags = 7
pots = 4

bags_per_bot = total_tea_bags // pots # to avoid decimal places in division

print(f"bags per pot is {bags_per_bot}")

# Remainder
remaining_bags = total_tea_bags % pots
print(f"remaining bags in remainder form is {remaining_bags}")

#exponential
base = 2
power = 3

new_number = base ** power
print(f"the new number from exponential is {new_number}")

#ways to write million or billion in python
million = 1_000_000
billion = 1_000_000_000

print(f"million is {million} and billion is {billion}")