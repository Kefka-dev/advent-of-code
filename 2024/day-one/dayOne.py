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


def partTwo(left, right):
  #just the left needs to be sorted
  left = np.sort(left)

  similarity = 0
  sum = 0
  for i in range(0, len(left)):
    wanted_number = left[i]
    count = np.count_nonzero(right == wanted_number)
    similarity = left[i] * count
    sum += similarity
  return sum

print("sum is: ", partOne(left, right))
print("similarity is: ", partTwo(left, right))

