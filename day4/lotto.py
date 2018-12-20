import requests
import random
# 1. https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837
# 위의 주소로 요청을 보낸다.
url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
response = requests.get(url).json()

# 2. 응답된 결과를 json으로 바꿔서 dictionary처럼 활용한다.
lotto_number = []
for i in range(1,7):
    lotto_number.append(response[f"drwtNo{i}"])
bonus = response["bnusNo"]

# 2-1. 당첨번호와 보너스 번호 출력
print(lotto_number)
print(bonus)

# 3. 랜덤으로 로또 번호 하나를 추출한다.
# my_numbers = random.sample(range(1,46),6)
# my_numbers = [int(i) for i in my_numbers]

# 4. 몇 등인지 알아본다.
# 1등 : 6개, 2등 : 5개+보너스번호
# 3등 : 5개, 4등 : 4개, 5등 : 3개





'''
a = 0
b = 0
while(1) : 
    my_numbers = random.sample(range(1,46), 6)
    for k in range(1, 7):
        if my_numbers[k] in lotto_number:
            b += 1
    if b == 2:
        print('5등')
        break
    elif b == 3:
        print('4등')    
        break
        
        
    
    else:
        a += 1
        print(a)

'''        


# 5. 등수를 출력한다.



'''
파이썬에는 set이라는 자료형이 있다.
list를 set으로 형변환을 할 수 있다.
혹은 a = {1, 2, 5} 직접 만들 수도 있다.
set은 중복된 값을 제거한다.
예) a = [1, 2, 2]
set(a)
=>{1,2}

교집합(&), 차집합(-), 합집합(|)을 할 수 있다.
'''

lucky = [0, 0, 0, 0, 0, 0]
for i in range(10000000):
    my_numbers = random.sample(range(1,46), 6)
    count = len(set(lotto_number) & set(my_numbers))

    if count ==6 :
        print("1등")
        lucky[0] += 1
        print(i)
        print(3100000000*lucky[0] + 66000000*lucky[1] + 1500000*lucky[2] + 50000*lucky[3] + 5000*lucky[4])
        break 
    elif count == 5 and bonus in my_numbers:
        lucky[1] += 1
    elif count == 5:
        lucky[2] += 1
    elif count == 4:
        lucky[3] += 1
    elif count == 3:
        lucky[4] += 1
    print(lucky, i, end="\r")
