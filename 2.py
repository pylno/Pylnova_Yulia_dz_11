class DivideByZero(Exception):
    def __init__(self, number, msg='Делить на ноль нельзя, введите другой делитель!'):
        self.number = number
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        return f'Второе число - {self.number} --> {self.message}'


class Number:
    def __init__(self, number):
        self.number = int(number)

    @staticmethod
    def divide_fail(number):
        if number == 0:
            print(DivideByZero(number))
            return True
        return False


def divide(n1, n2):
    return n1/n2


print('Введите делимое:')
num1 = Number(input())
print('Введите делитель:')
num2 = Number(input())
while Number.divide_fail(num2.number):
    num2 = Number(input())
print(f'Результат деления: {divide(num1.number, num2.number)}')