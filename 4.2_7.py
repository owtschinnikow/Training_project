"""
Sample Input:

6
Insert 200
Insert 10
ExtractMax
Insert 5
Insert 500
ExtractMax
Sample Output:

200
500

"""


def main():
    #n = input()
    number_0 = 0
    n = 6
    n = int(n)
    for i in range(n):
        sentens = input()
        if sentens == 'ExtractMax':
            print(number)
        elif sentens != 'ExtractMax':
            text = sentens.split()
            number = int(text[1])
            if number >= number_0:
                number_0= number
            elif number < number_0:
                number = number_0
            #print('text', number)
            #list.reverse()    Разворачивает список
            
    
    
    
if __name__ == "__main__":
    main()
