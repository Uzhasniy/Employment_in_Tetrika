# Ввод массива и проверка условий
def inputter():
    array = ''
    array = input('Введите массив чисел: \n(по умолчанию: 111111111111111111111111100000000)').strip()
    if array == '':
        array = '111111111111111111111111100000000'
        task(array)
    else: 
        if '0' in array:
            task(array)
        else: print('Нет нулей')

# Поиск "0" и вывод индекса последней 1
def task(array):
    zero = array.find('0')
    print(f'Индекс последней единицы: {zero}')

if __name__ == "__main__":
    inputter()
