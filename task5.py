# В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.

from string import punctuation

st = '''a b c d de f g a a a g r s t y a df hfg hdj
hxfdzgfdg fhj xhdjcfjmh cgf d d
d?<<>dsjhnlkJ d l l l l l l i a a i ihdb de eh dsu we i f f f l k s'''.lower()
ls = ''
count = {}

for i in st:
    if i not in punctuation:
        ls += i
ls = ls.replace("\n", " ")

for i in ls.split(' '):
    count[i] = count.get(i, 0) + 1
    # if i not in count:
    #     count[i] = 1
    # else:
    #     count[i] += 1
ls_count = sorted(list(count.items()), key=lambda x: x[-1], reverse=True)
print(ls_count[:10])
