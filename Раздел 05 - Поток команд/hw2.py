x = int(input(' Введите число, пожалуйста: '))
print(' Результат: ' + (
          'Плохо' if x % 2 != 0 else
          'Неплохо' if 1 < x < 6 else
          'Так себе' if 5 < x < 21 else
          'Отлично' if x > 20 else
          'Какое-то странное у вас число... не натуральное'))
