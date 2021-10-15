def main():
    reader = (number for number in range(3)) # Генератор для стандатрого ввода, разбивает сроку на куски и приводит каждый кусок к целому куску
    for i in range(4):
        print('i', i)
        print('readeri',reader)
        print('next(reader)',next(reader, '_____stopiteration____'))


 


if __name__ == "__main__":
    main()
