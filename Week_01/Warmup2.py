# Create class list
class_list = []

# Ask the name of all classes this semester
num_classes = int(input('Enter number of classes you are taking this semester. '))

# Save class names in a list
for i in range(num_classes):
    class_name = input(f'Enter the name of class {i+1}: ')
    class_list.insert(i, class_name)

# Print all classes in a list
print(class_list)