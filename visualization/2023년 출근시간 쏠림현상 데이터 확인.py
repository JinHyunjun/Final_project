import requests
import pandas as pd
from datetime import date, timedelta

# 데이터를 담을 빈 리스트 생성
data_list = []

# 시작 날짜와 종료 날짜 설정
start_date = date(2024, 3, 20)
end_date = date(2024, 3, 25)

# 시작 날짜부터 종료 날짜까지 하루씩 증가시키며 반복
current_date = start_date
while current_date <= end_date:
    # 날짜를 YYYYMMDDHH 형식으로 변환 (예를 들어, 오전 8시 ~ 10시의 데이터를 요청하고자 한다면)
    formatted_date = current_date.strftime('%Y%m%d') + "00"  # 여기서 '01'은 오전 1시를 의미합니다. 필요에 따라 변경하세요.
    
    # API URL에 날짜 포맷 적용
    url = f'http://openapi.seoul.go.kr:8088/4e795179456a696e35395663765278/json/bikeListHist/1/1000/{formatted_date}'
    response = requests.get(url)
    
    # 정상 응답을 받는 경우만 처리
    if response.status_code == 200:
        data = response.json()
        
        # 데이터 처리 로직
        for station in data['getStationListHist']['row']:
            # 대여소 정보를 딕셔너리 형태로 저장
            station_info = {
                'station_name': station['stationName'],
                'latitude': station['stationLatitude'],
                'longitude': station['stationLongitude'],
                'shared': int(station['shared']) / 100
            }
            data_list.append(station_info)
    
    # 다음 날짜로 이동
    current_date += timedelta(days=1)

# pandas DataFrame으로 변환
df = pd.DataFrame(data_list)

# CSV 파일로 저장
df.to_csv('seoul_bike_stations_2023.csv', index=False)
