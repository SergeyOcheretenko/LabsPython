array = list(map(float, input('Enter your array:\n').split()))
print('Your array:\n', array)

array.sort()
print('Sorted array:\n', array)

count = 0
average = 0.0
for i in range(0, len(array)):
  if i % 2 == 0:
    average += array[i]
    count += 1
average = round(average / count, 5)
print('Your average:\n', average)

for i in range(0, len(array)):
  if array[i] % 1 == 0:
    array[i] = average
print('Updated array:\n', array)
