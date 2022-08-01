class IntTypeErr(Exception):
    def __init__(self, in_str, msg='Вы ввели не число!'):
        self.in_str = in_str
        self.message = msg
        super().__init__(self.message)

    def __str__(self):
        return self.message


in_lst = []
while True:
    try:
        print('Введите число: ')
        inp = input()
        if inp == 'stop':
            break
        num = int(inp)
        in_lst.append(num)
    except ValueError:
        print(IntTypeErr(inp))
print(in_lst)