'''
Программа должна считывать одну строку со стандартного ввода и выводить для каждого уникального слова в этой строке число 
его повторений (без учёта регистра) в формате "слово количество" (см. пример вывода). 
Порядок вывода слов может быть произвольным, каждое уникальное слово должно выводиться только один раз.
'''

def wordFrequency(words):
    d = {}
    for key in words:
        if(d.get(key)!=None):
            d[key] += 1;
        else:
            d[key] = 1;
    return d
s = input()
s = s.lower()
words = s.split(' ')
d = wordFrequency(words)
for key, value in d.items():
    print(key, value); 
