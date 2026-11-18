first_name = input("Enter your given name: ")
last_name = input("Enter your last name: ")
section_ = input("Section: ")
fav_sub = input("Favorite subject: ")

full_name = first_name + "" + last_name

print("Student Name:", first_name.capitalize(), last_name.capitalize())
print("Student Code:", first_name.upper(), last_name.upper())
print("Section:", section_.upper())
print("Student's Favorite Subject:", fav_sub.title())
print("Character Count:", len(full_name))
