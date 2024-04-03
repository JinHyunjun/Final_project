import requests
import json
import folium

# API로부터 XML 응답 받기
response = requests.get('http://openapi.seoul.go.kr:8088/4e795179456a696e35395663765278/json/bikeListHist/1/100/20231024810')
# JSON 형식으로 응답 파싱
data = response.json()

# 서울 중심부를 기준으로 한 지도 생성
m = folium.Map(location=[37.5665, 126.9780], zoom_start=11)

# data에서 대여소 정보 추출 및 마커 생성
for station in data['getStationListHist']['row']:
    lat = float(station['stationLatitude'])
    lon = float(station['stationLongitude'])
    name = station['stationName']
    shared = int(station['shared']) / 100

    # shared 값에 따라 마커 색상 구분
    if shared > 1:
        color = 'red'  # 자전거 쏠림 현상이 있는 경우
    else:
        color = 'blue'  # 일반 경우

    # 마커 생성
    folium.Marker([lat, lon], popup=name, icon=folium.Icon(color=color)).add_to(m)

# 지도 저장(혹은 직접 출력)
m.save('seoul_bike_stations.html')