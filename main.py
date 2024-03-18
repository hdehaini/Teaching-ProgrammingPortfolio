myList = [-10, 4, 9, -3, 0, 2, 1]

# Variable from the script
num = 5

# Loop through each item and apply the conditions from the script
for item in myList:
    if item % 2 == 0:  # If the item is even
        print(item)
        if item > num:  # If the item is greater than num
            num = item  # Set num to item

print("Final num = ", num)