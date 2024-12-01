import numpy as np
input_file = "input.txt"
left = np.empty(0, dtype=int)
right = np.empty(0, dtype=int)
#get two arrays left and right
with open(input_file, "r") as file:
  for line in file:
    line_numbers = line.split()
    left = np.append(left,int(line_numbers[0]))
    right = np.append(right,int(line_numbers[1]))

def partOne(left, right):

  #sort the array
  left = np.sort(left)
  right = np.sort(right)


  sum = 0
  for i in range(0, len(left)):
    distance = abs(left[i] - right[i])
    sum+=distance
  return sum


print("sum is: ", partOne(left, right))

