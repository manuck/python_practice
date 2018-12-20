import requests


key = "c191b82500178c3be4ea332e68b2bb81"
url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json"

response = requests.get(url).json
targetDt = "20181220"
url = f"{url}?key={key}&"

# 1. 요청
print(url.response["movieListResult"])

