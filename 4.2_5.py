"""

По данной непустой строке ss длины не более 10^4, состоящей из строчных
букв латинского алфавита, постройте оптимальный беспрефиксный код.
В первой строке выведите количество различных букв kk, встречающихся в строке, и размер
получившейся закодированной строки. В следующих kk строках запишите коды букв в формате
"letter: code". В последней строке выведите закодированную строку.

Sample Input 1:
a

Sample Output 1:
1 1
a: 0
0

Sample Input 2:
abacabad

Sample Output 2:
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111

"""


"""
4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
"""



def main():
    lst = []
    lst1 = []
    lst2 = {}
    sentens = 'abcd' #list(input())
    #sentens = 'abacabad' #list(input())
    #print(sentens)
    leters = list(set(sentens))
    for leter in leters:
        n = sentens.count(leter)
        lst.append([n, leter])
        lst.sort()
        
    if len(lst) == 1:
        lst2[leter] = str(0)

    while len(lst) > 1:
        
        min1 = lst.pop(0)
        lst1.append([min1[1], 0])
        #print('first_pop', min1, lst1)
        
        min2 = lst.pop(0)
        lst1.append([min2[1], 1])
        #print('second_pop', min2, lst1)
        
        
        item_sum = [(min1[0] + min2[0]), (min1[1] + min2[1])]
        lst.append(item_sum )
        lst.sort()
        
            
        #print('lst', lst, )
        
    for i in leters:
        #print('i - ', i)
        for j in lst1:
            #print('j - ', j)
            if i in j[0]:
                #print('i - ', i, 'j - ', j)
                if i not in lst2:
                    lst2[i] = str(j[1])
                    #print('lst2-1 - ', lst2)
                else:
                    lst2[i] = (str(j[1]) + str(lst2[i]))
                    #print('lst2-2 - ', lst2[i])
    #print('third - ', lst2)
    
    encoded_str = ''.join([lst2[char] for char in sentens])
    print(len(leters), len(encoded_str))
    for key, value in sorted(lst2.items()):
        print('{}: {}'.format(key, value))
    
    print(encoded_str)

if __name__ == "__main__":
    main()
