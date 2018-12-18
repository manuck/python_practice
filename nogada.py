import os

# SSAFY_지원자 폴더로 들어가고
os.chdir(r'SSAFY_지원자')
# SSAFY지원자 폴더로 들어가고
os.chdir(r'SSAFY지원자')
# 모두 출력
files = os.listdir()
print(files)
for file in files:
    os.rename(file, file.replace("SAMSUNG", "SSAFY"))