#A program to find out if a year is a leap year or not.

year = int(input("Which year do you want to check? "))

# Method 1:
# if (year % 4 == 0) and (year % 100 != 0):
#   print(f"Leap year.")
# elif (year % 100 == 0) and (year % 400 == 0):
#   print(f"Leap year.")
# else:
#   print(f"Not leap year.")

# Method 2
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"Leap year")
    else:
      print(f"Not leap year")
  else:
    print("Leap year.")
else:
  print(f"Not leap year")