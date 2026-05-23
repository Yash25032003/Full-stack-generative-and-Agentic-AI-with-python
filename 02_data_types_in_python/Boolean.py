is_logged_in = True
count = 5

#upcasting
total_action = count + is_logged_in

print(f"total action is: {total_action}")

milk_present = 0 
# converts it into boolean
print(f"is milk present : {bool(milk_present)}")

# true represents 1 , false represents 0

# BOOLEAN OPERATORS which are and, or , not

#and
water_hot = True
tea_added = False
can_serve_chai = water_hot and tea_added
print(f"can serve chai ? {can_serve_chai} ")

#or
is_logged_in = True
user_has_password = False
can_enter = is_logged_in or user_has_password
print(f"can enter ? {can_enter} ")




