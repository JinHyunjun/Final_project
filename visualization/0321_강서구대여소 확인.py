import pandas as pd

# CSV 파일 로드
file_path = "C:\\Users\\hyeon\\Downloads\\서울시공공자전거이용정보(시간대별)(12월).csv"
df = pd.read_csv(file_path)

# 'RENT_NM' 칼럼에 '강서구'가 포함된 행만 필터링
filtered_df = df[df['RENT_NM'].str.contains('강서')]

# 결과 출력
print(filtered_df)


