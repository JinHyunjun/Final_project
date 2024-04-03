import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rc('font', family="Malgun Gothic")

# 데이터 준비
data = {
    '자치구': ['계', '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'],
    '이용량': [16723496, 525055, 717521, 260627, 1859572, 414884, 820720, 658422, 286036, 1011936, 346221, 599641, 343460, 841789, 340868, 501267, 679376, 410362, 1579209, 938128, 1356173, 343033, 419072, 586812, 403478, 479814]
}

df = pd.DataFrame(data)

# '계' 열은 제외하고 시각화하기
df = df[df['자치구'] != '계']

plt.figure(figsize=(14, 8)) # 그래프 크기 설정
plt.bar(df['자치구'], df['이용량'], color='skyblue') # 막대그래프 그리기
plt.xlabel('자치구', fontsize=14) # x축 라벨
plt.ylabel('이용량', fontsize=14) # y축 라벨
plt.title('2023년 1~5월 자치구별 따릉이 이용량', fontsize=16) # 제목
plt.xticks(rotation=45) # x축 눈금 라벨 회전
plt.tight_layout() # 레이아웃 조정
plt.show()
