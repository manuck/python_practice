phonebook = {
    #key    :   value
    "중국집": "02843",
    "초밥집": "031",
    "한식집": "043"
    } 

phonebook2 = dict(중국집=1, 초밥집=2)

# print(phonebook)
# print(phonebook2)

# phonebook["분식집"] = "042123"
# print(phonebook["분식집"])

#1. 좋아하는 그룹 : key - 이름 , value - 나이
twice = {
    "모모": 23,
    "사나": 23,
    "나연": 24
}

#1-2. idol이라는 dictionary
# idol : key - 그룹명, value - dictionary
idol = {
    "twice":{
        "모모":23,
        "사나":23,
        "나연":24
    },
    "rv":{
        "슬기":23,
        "웬디":24
    }
}
a = idol["twice"]["모모"]
print(a)
# dictionary 반복문
for key in phonebook:
    print(key, end=' ')
    print(phonebook[key])
#   위와 아래 같은 출력(key, value)
for key, value in phonebook.items():
    # for key, value
    print(key, value)

# value만 출력
for value in phonebook.values():
    print(value)

# key만 출력
for key in phonebook.keys():
    print(key)

# https://zzu.li/dj_dict1