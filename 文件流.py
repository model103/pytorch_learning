a = {}
b = [1,2,3]
c= [11,22,33]
a['111'] = dict(zip(b,c))  #可通过a[]形式直接给字典添加内容 #zip(a,b)将list a和b压缩成元组,查看该元组还需转成lsit，dict再转成字典,
#print(a)
#print(list(zip(b,c)))
a['a'] = 'b'
a['c'] = 'c'
#print(a)
#print(a.items()) #items()转成元组
#print(tuple(a)) #tuple只将key转成元组
if 'a' in a and 'b' == a['a']:
    print('true')

di = {'a':3,'b':2,'c':1}
di['a'] = 4
after_sorted = sorted(di.items(), key = lambda item: item[1]) #对i.items()元组进行排序，排序依据key为lamba匿名函数的返回值，即item[1]，也即字典的vlaue
print(after_sorted[:2])


b = ['a','a','a','b','b']

def frequence(b:list):
    fre = {}
    for i in b:
        if i not in fre:
            fre[i] = 1
        else:
            fre[i] += 1
    return fre
print(frequence(b))
#[()for v in sorted(dict.values())]

def aa(*path):
    return path

print(aa('111','222','333'))