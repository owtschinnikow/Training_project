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

#coding: utf8
#Сжатие и распаковка по Хаффману

#Secondary functions
#Element to work: a - (quantity, symbol)

#comparison of two elements to quantity
def fn_cmp(a, b):
    if a[0] > b[0]: return 1
    if a[0] < b[0]: return -1
    return 0


# create tree of Haffman from text
def make_tree(text):
    #build sorted list (frequancy, symbol)
    se = set(text)
    ls = [(text.count(ch), ch) for ch in se]
    ls.sort(fn_cmp)

    #build binary tree by this list
    while len(ls) >= 2:
        d = (ls[0][0] + ls[1][0],(ls[0][1], ls[1][1]))
        #print d
        if ls[-1][0]<d[0]:
            ls.append(d)
        else:
            for num in range(2, len(ls)):
                if ls[num][0] >= d[0]:
                    break
            ls.insert(num, d)
        ls.pop(0)
        ls.pop(0)
    return ls[0][1]


# recursively create the element's sheet binary
def fn_cod(st, el):
    global ls_haf
    if type(el) == str:
        ls_haf.append( (el, st) )
        return
    fn_cod(st+'0', el[0])
    fn_cod(st+'1', el[1])
    return


# create Haffman's dictionary from text
def make_dict(text):
    global ls_haf
    ls = make_tree(text)
    ls_haf = []
    fn_cod('',ls)
    dc_haf = dict(ls_haf)
    return dc_haf

# compress over Haffman
def compress(text, dc_haf):
    st_res = ''
    for ch in text:
        st_res = st_res + dc_haf(ch)
    return st_res


# decompress
def decompress(text, dc_haf):
    dc_decod = { dc_haf[key]:key for key in dc_haf }
    st_res = ''
    while len(text) > 0:
        num = 1
        while text[:num] not in dc_decod:
            num += 1
        st_res += dc_decod[text[:num]]
        text = text[num:]
    return st_res


# Program

text = 'preved medved'



dc_haf = make_dict(text)
compressed_text = compress(text, dc_haf)
decompress_text = decompress(compressed_text, dc_haf)

print ('text', text)
print ('dc_haf', dc_haf)
print ('compressed_text', compressed_text)
print ('decompress_text', decompress_text)




"""
def main():
    d = {}
    sentens = 'abacabad' #list(input())
    print(sentens)
    leters = list(set(sentens))
    for leter in leters:
        n = sentens.count(leter)
        d[leter] = n
        print(leter, n)
    
    
        
    print(sentens, leters, d)

if __name__ == "__main__":
    main()
"""
