#1. 구구단
# w : write(덮어쓰기), a : append(이어쓰기), r : read(읽기)


with open("gugudan.txt", "w") as file:

    for i in range(2,10):
        for j in range(2,10):
            line = f"{i}*{j}={i*j}\n"
            file.write(line)


with open("ssafy.txt", "w") as file:
    z = ["안녕","하세요","저는","노승만","입니다","만나서","반갑습니다"]
    for soga in z:
        file.write(f"{soga}\n")


with open("ssafy.txt", "r") as file:
    word = file.readlines()

rword = reversed(word)

with open("result.txt", "w") as file:
    for line in rword:
        file.write(line)