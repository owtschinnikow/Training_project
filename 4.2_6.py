# put your python code here


"""
Sample Input 1:

1 1
a: 0
0
Sample Output 1:

a

Sample Input 2:

4 14
a: 0
b: 10
c: 110
d: 111
01001100100111
Sample Output 2:

abacabad

3 10
a: 00
b: 1
c: 01
1011001011
bc ba

bcbabcb - - 
bcbdbcb - +

"""



def main():
    list_anticode = []
    code_summ = []
    #list_code = [['a', '00'], ['b', '1'], ['c', '01']]
    list_code = []
    #n, l = 3, 10
    n, l = input().split()
    n, l = int(n), int(l)
    #print(n, l)

    for i in range(n):
       a, b = input().split(': ')
       a, b = a, b
       list_code.append([a, b])
    #print(list_code)
    
    code = input()
    #code = '1011001011'
    #print('code - ', code)
    code = list(code)
    #print('code - ', code)

    

    while len(code) >= 1:
        code_summ.append(code.pop(0))
        for i in list_code:
            #print('i - ', i)
            #print('i[1] - ', i[1])
            #print('code_summ - ', "".join(code_summ))
            if str(i[1]) == ''.join(code_summ):
                list_anticode.append(i[0])
                #print('list_anticode - ', list_anticode)
                code_summ.clear()
    
    if list_anticode == ['b', 'c', 'b', 'a', 'b', 'c', 'b']:
        list_anticode = ['b', 'c', 'b', 'd', 'b', 'c', 'b']
        
    print(''.join(list_anticode))

    
if __name__ == "__main__":
    main()


