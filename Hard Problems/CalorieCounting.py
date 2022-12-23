# The data to be inserted into the list
str_data = [ """ {input} """ ]

# The list to hold the constructed data
constructed = []

# Iterate over the data strings
for i in str_data:
  # Remove the leading and trailing whitespace from the string
  i = i.strip()

  # Add the items from the string to the constructed list
  constructed.extend(i.split("\n"))

int_construcked = []

for j in constructed:
    if j.isdigit():
        int_construcked.append(int(j))
    else:
        int_construcked.append(j)

# split into different arrays
output = []
counter = 0
start = 0
for item in int_construcked:
    if item == "":
        output.append(int_construcked[start:counter])
        start = counter + 1
    if counter == len(int_construcked) - 1:
        output.append(int_construcked[start:counter + 1])
    counter += 1

elfs_sums = []
for k in range(len(output)):
    elfs_sums.append(sum(output[k]))
elfs_sums.sort()
print(elfs_sums[-3] + elfs_sums[-1] + elfs_sums[-2])

