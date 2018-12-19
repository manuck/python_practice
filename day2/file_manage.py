# file = open("new.txt", "w")
# file.write("글써짐?")
# file.close()

# 1. 파일 쓰기
with open("new1.txt", "w") as file:
    '''
    파이썬에서 with는 컨택스트 매니저라고 부른다.
    with 블록내에서 파일을 조작하고,
    블록이 끝나게 되면 파일이 닫힌다.
    '''
    file.write("글 또 쓰자")

# 2. 파일 읽기
with open("new.txt", "r") as file:
    line = file.read()
    print(line)


# 3. 파일 여러줄 쓰기 new2.txt
with open("new2.txt", "w") as file:
    for line in range(50):
        file.write(f"{line}번째 줄입니다.\n")

# 4. 파일 여러줄 읽기
with open("new2.txt", "r") as file:
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)
    # line = file.readline()
    # print(line)


    # while True:
    #     line = file.readline()
    #     if line =='':
    #         break
    #     print(line)
    lines = file.readlines()
    #print(lines)
    
    for i in lines:
        print(i.strip('\n'))