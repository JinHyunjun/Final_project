import pandas as pd
import matplotlib.pyplot as plt

# 데이터 로드
data = pd.read_csv("C:\\multi_final\\data\\2022년_latest.csv")

# 'datetime' 컬럼을 datetime 객체로 변환
data['datetime'] = pd.to_datetime(data['datetime'])

# 월 단위로 datetime 변환
data['month'] = data['datetime'].dt.to_period('M')

# 필요한 컬럼만 선택
data = data[['datetime', 'ID', 'y', 'month']]

# ID와 월별로 그룹화하여 y의 평균 계산
monthly_data = data.groupby(['ID', 'month'])['y'].mean().reset_index()

# 선택한 10개의 정류소 ID, 예시로 1부터 10까지의 ID를 가정
selected_ids = range(1, 11)

# 그래프 설정
plt.figure(figsize=(15, 10))
plt.rc('font', family="Malgun Gothic")

# 각 정류소별로 반복하여 그래프 그리기
for id in selected_ids:
    # 현재 정류소의 월별 평균 데이터 선택
    temp_data = monthly_data[monthly_data['ID'] == id]
    # 그래프 그리기
    plt.plot(temp_data['month'].astype(str), temp_data['y'], label=f'ID {id}')

# 범례 표시
plt.legend()
# x축 레이블
plt.xlabel('월')
# y축 레이블
plt.ylabel('평균 자전거 거치대 수')
# 그래프 제목
plt.title('정류소별 월 평균 자전거 거치대 수')
# x축 눈금 레이블 회전
plt.xticks(rotation=45)
# 그래프 표시
plt.show()
