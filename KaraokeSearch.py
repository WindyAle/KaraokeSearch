import requests
from bs4 import BeautifulSoup
import re

# TJ노래방 곡 검색 페이지 URL
url = "http://www.tjmedia.co.kr/tjsong/song_search_list.asp"

# 모든 곡 정보를 담고 있는 리스트
songs = []

# 모든 곡 정보를 크롤링하여 리스트에 추가합니다.
for page in range(1, 21):
    params = {"strType": "2", "strText": "", "strCond": "", "strSize": "20", "strPage": page}
    response = requests.post(url, data=params)
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.select("tr[onmouseover]")

    for row in rows:
        cols = row.select("td")
        song_id = cols[1].text.strip()
        title = cols[2].text.strip()
        artist = cols[3].text.strip()
        songs.append((song_id, title, artist))

# 곡 번호를 입력하면 곡 정보를 출력하는 함수
def search_by_id(song_id):
    for song in songs:
        if song[0] == song_id:
            print(f"{song[1]} - {song[2]}")
            return
    print("해당하는 곡이 없습니다.")

# 곡 제목을 입력하면 곡 번호를 출력하는 함수
def search_by_title(title):
    for song in songs:
        if song[1] == title:
            print(f"{song[0]}")
            return
    print("해당하는 곡이 없습니다.")

# 가수 이름을 입력하면 해당 가수의 모든 곡 정보를 출력하는 함수
def search_by_artist(artist):
    for song in songs:
        if song[2] == artist:
            print(f"{song[0]} - {song[1]}")
    if not any(song[2] == artist for song in songs):
        print("해당하는 가수의 곡이 없습니다.")

# 사용자 입력을 받아서 각 함수를 호출하는 루프
while True:
    search_type = input("곡 번호, 곡 제목, 가수 중 어떤 것으로 검색하시겠습니까? ")
    if search_type == "곡 번호":
        song_id = input("곡 번호를 입력하세요: ")
        search_by_id(song_id)
    elif search_type == "곡 제목":
        title = input("곡 제목을 입력하세요: ")
        search_by_title(title)
    elif search_type == "가수":
        artist = input("가수 이름을 입력하세요: ")
        search_by_artist(artist)
    else:
        print("올바른 검색 유형을 입력하세요.")