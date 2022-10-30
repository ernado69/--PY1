def get_count_char(str_):
        # TODO посчитать количество каждой буквы в строке в аргументе str_
    str_ = ''.join(str_.lower().split())
    dict = {}
    DEFAULT_COUNT = 0

    for symbol in str_:
        if symbol.isalpha():
            dict[symbol] = dict.get(symbol, DEFAULT_COUNT) + 1
    return dict

main_str = """
        Данное предложение будет разбиваться на отдельные слова. 
        В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
        Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
    """

def get_percent_char(enum_):
    enumeration = sum(enum_.values())
    for symbol in enum_:
        enum_[symbol] = enum_[symbol] / enumeration * 100
    return enum_

print(get_count_char(main_str))
