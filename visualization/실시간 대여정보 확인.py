import requests
import folium

response_data = requests.get('http://openapi.seoul.go.kr:8088/50455477556a696e333748484d707a/json/bikeList/1/1000/')

bike = response_data.json()
bike_infos = bike['rentBikeStatus']['row']

# 서울의 중심에 해당하는 위도와 경도를 기준으로 초기 지도 생성
seoul_map = folium.Map(location=[37.5665, 126.9780], zoom_start=12)

# 대여소의 위치에 마커 추가
for bike_info in bike_infos:
    station_lat = bike_info['stationLatitude']  # 위도
    station_lon = bike_info['stationLongitude']  # 경도
    station_name = bike_info['stationName']  # 대여소 이름
    station_bike = bike_info['rackTotCnt']
    # 마커 생성
    folium.Marker([station_lat, station_lon], popup=[station_name, station_bike]).add_to(seoul_map)

# 지도를 html파일로 저장
seoul_map.save('seoul_bike_map.html')