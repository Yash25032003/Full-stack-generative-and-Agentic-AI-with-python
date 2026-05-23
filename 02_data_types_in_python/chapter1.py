sugar_amount = 2 
print(f"The initial sugar is : {sugar_amount}")

sugar_amount = 12
print(f"The second sugar is : {sugar_amount}")
# above example me hum reference change kar rahe hai na ki value because numbers are immutable
# proof ? by checking the id

print(f"Id of 2 is : {id(2)}")
print(f"id of 12 is : {id(12)}")


# both id are different not same matlab they are immutable
