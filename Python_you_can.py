# Step 1: Write a few lines into the file
with open("learning_python.txt", "w") as file:
    file.write("In Python you can automate repetitive tasks.\n")
    file.write("In Python you can make Robots \n")
    file.write("In Python you can make a shiny rock filled with lightning do magical things\n")

# Step 2a: Read and print the entire file content at once
print("=== learning_python.txt ===")
with open("learning_python.txt") as file:
    contents = file.read()
    print(contents)

# Step 2b: Read and print the file line by line using a loop
print("=== loop ===")
with open("learning_python.txt") as file:
    for line in file:
        print(line.strip())

# Step 2c: Store lines in a list and print them outside the with block
print("=== list of line ===")
with open("learning_python.txt") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())

# Step 3: Replace 'Python' with 'PHP' and print modified lines
print("=== Replacing easy with awful ===")
for line in lines:
    print(line.replace("Python", "C++").strip())
