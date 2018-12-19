"""
파이썬 dictionary 활용 기초!
"""

# 1. 평균을 구하세요.
iu_score = {
    "수학": 80,
    "국어": 90,
    "음악": 100
}
a=0
# 답변 코드는 아래에 작성해주세요.
for score in iu_score.values():
    a = a + score
b = len(iu_score)
a = a / b
print(a)


# 2. 반 평균을 구하세요.
score = {
    "iu": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    },
    "ui": {
        "수학": 80,
        "국어": 90,
        "음악": 100
    }
}
# 답변 코드는 아래에 작성해주세요.
print("=====Q2=====")
z = 0
x = 0
for iusum in score["iu"].values():
    z = z + iusum
for uisum in score["ui"].values():
    x = x + uisum
c = z + x
num = len(score["iu"]) + len(score["ui"])
avr = c / num
print(avr)

# 기본 풀이법

# total_score = 0
# for person_score in score.values():
#     #length += len(person_score)
#     for individual_score in person_score():
#         total_score += individual_score
#         length += 1
# average_score = total_score / len(length)

# 3. 도시별 최근 3일의 온도 평균은?
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
# 3-1. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

# 답변 코드는 아래에 작성해주세요.
print("=====Q3=====")

tem1 = [sum(city["서울"]), sum(city["대전"]), sum(city["광주"]), sum(city["부산"])]
seo = len(city["서울"])
# for stem in city.values():

for ci, tem in city.items():
    # for key, value
    a = sum(tem)/len(tem)
    print(f"{ci} :  {a}")







# 답변 코드는 아래에 작성해주세요.
print("=====Q3-1=====")
city = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9]
}

cold = 0
hot = 0
count = 0
hot_city = ""
cold_city = ""
for name, temp in city.items():
    # 첫 번째 시행 때,
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
        hot = max(temp)
        cold = min(temp)
        hot_city = name
        cold_city = name
    else :
        #최저온도가 cold보다 더 추우면, cold에 넣고
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        #최고온도가 hot보다 더 더우면, hot에 넣고 
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1
print(f"가장 더운 도시 : {hot_city}")
print(f"가장 추운 도시 : {cold_city}")


# 4. 위에서 서울은 영상 2도였던 적이 있나요?
# 답변 코드는 아래에 작성해주세요.
print("=====Q4=====")
2 in city["서울"]


if 2 in city["서울"]:
    print("있어요")
else:
    print("없어요")