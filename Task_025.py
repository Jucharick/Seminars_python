# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

path = r'C:/Users/Юлия Чарикова/Desktop/GeekBrains/I четверть - блок 2/Знакомство с языком Python/Seminars/file_for_task025.txt'
with open(path, 'r') as data:
    text = data.read().split()

print (text)
text = list(map(int, text))
print (text)

text = [text[x]-1 for x in range(1, len(text)) if text[x] - 1 != text [x-1]]
print (text) 