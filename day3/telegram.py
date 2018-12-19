import requests
import os
#!!!!!!!!!!!! 토큰은 비밀번호와 같다!!!!!!!!!!!!!!
token = os.getenv("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/getUpdates"
# 1. 요청을 보낸 결과를 response 저장을 한다.
response = requests.get(url)


# 2. json 형식으로 바꾼다. 
# 지금은 dictionary와 list가 섞여 있는 것과 같다고 생각하면 된다.
updates = response.json() 
#print(updates)

# 3. user의 id를 찾는다.
user_id = updates["result"][0]["message"]["from"]["id"]
print(user_id)

# 4. 메시지를 설정한다.
msg  = "안녕안녕?"
url = f"https://api.telegram.org/bot{token}/sendMessage?text={msg}&chat_id={user_id}"

# 5. 메시지를 보낸다.
requests.get(url)