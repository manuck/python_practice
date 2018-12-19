print('hello world')

# 1부터 100까지 숫자를
a = range(1,101)
# even list 를 만들어서 짝수만 저장
even = []
# odd list 를 만들어서 홀수만 저장
odd = []

for i in a:
    #짝
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)