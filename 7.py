class IntTypeErr(Exception):
    def __init__(self, msg='Вы ввели не число!'):
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = int(real_part)
        self.imaginary_part = int(imaginary_part)

    def __str__(self):
        if self.real_part == 0:
            return f'{self.imaginary_part}i'
        else:
            if self.imaginary_part > 0:
                if self.imaginary_part == 1:
                    return f'{self.real_part}+i'
                return f'{self.real_part}+{self.imaginary_part}i'
            elif self.imaginary_part < 0:
                if self.imaginary_part == -1:
                    return f'{self.real_part}-i'
                return f'{self.real_part}{self.imaginary_part}i'
            else:
                return f'{self.real_part}'

    def __add__(self, other):
        new_real = self.real_part+other.real_part
        new_imaginary = self.imaginary_part+other.imaginary_part
        return ComplexNumber(new_real, new_imaginary)

    def __mul__(self, other):
        new_real = self.real_part*other.real_part-self.imaginary_part*other.imaginary_part
        new_imaginary = self.real_part*other.imaginary_part+self.imaginary_part*other.real_part
        return ComplexNumber(new_real, new_imaginary)


try:
    print('Введите действительную часть первого комплексного числа: ')
    real1 = input()
    print('Введите мнимую часть первого комплексного числа: ')
    imaginary1 = input()
    complex_num1 = ComplexNumber(real1, imaginary1)
    print(f'Первое комплексное число: {complex_num1}')

    print('Введите действительную часть второго комплексного числа: ')
    real2 = input()
    print('Введите мнимую часть второго комплексного числа: ')
    imaginary2 = input()
    complex_num2 = ComplexNumber(real2, imaginary2)
    print(f'Второе комплексное число: {complex_num2}')

    complex_num3 = complex_num1 + complex_num2
    print(f'Результат сложения: {complex_num3}')
    complex_num4 = complex_num1 * complex_num2
    print(f'Результат умножения: {complex_num4}')
except ValueError:
    print(IntTypeErr())