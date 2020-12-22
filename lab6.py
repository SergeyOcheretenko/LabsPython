change = int(input('Выберите способ ввода (1 - ввести строку в консоль, 2 - ввести строку с файла):\n'))
if change == 1:
  string = input('Введите вашу строку:\n').strip()
  print(f'Ваша строка:\n{string}')
  array = string.split(' ')
  for i in range(len(array)):
    array[i] = str(ord(array[i][0].lower()) - 96) + array[i][1:]
  print(f"Обновленная строка:\n{' '.join(array)}")
elif change == 2:
  name = input('Введите названия файла в виде name.txt:\n')
  handle = open(name)
  string = handle.readline().strip()
  print(f'Ваша строка:\n{string}')
  array = string.split(' ')
  for i in range(len(array)):
    array[i] = str(ord(array[i][0].lower()) - 96) + array[i][1:]
  print(f"Обновленная строка:\n{' '.join(array)}")
  handle.close()
else:
  print('Ошибка ввода')
