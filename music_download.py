import json
import requests

# JSON 파일 읽기
with open('music.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 다운로드 함수
def download_mp3(track):
    track_id = track['id']
    title = track['title']
    album_title = track['album']['title']
    audio_url = track['audioFile']['url']

    # 파일 이름 생성 (예: Castles In The Air - The Piano Works 4.mp3)
    filename = f"{title} - {album_title}.mp3"
    
    # 파일 다운로드
    response = requests.get(audio_url)
    
    if response.status_code == 200:
        # 파일 저장
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {title}")

# 모든 트랙 다운로드
tracks = data['props']['pageProps']['tracks']
for track in tracks:
    download_mp3(track)