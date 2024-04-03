import sys
input = sys.stdin.readline

n = int(input()) # 조각의 수
songs = []
max_waiting_time = 0 # 최대 대기 시간
current_length = 0 # 현재 다운로드되어 있는 노래 조각의 길이

for _ in range(n):
    d, v = map(int, input().split()) # 노래의 길이, 다운로드 시간
    songs.append((d,v))

for song_length, download_time in songs:
    current_length -= download_time
    
    if current_length < 0:
        max_waiting_time -= current_length
        current_length = 0
    
    current_length += song_length

print(max_waiting_time)

