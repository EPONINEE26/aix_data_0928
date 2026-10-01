import pandas as pd
df = pd.read_excel('file/score.xlsx',index_col='지원번호')

# 컬럼선택 : df[컬럼] , 2개이상 []리스트로 추가
df[['이름','키','학교']]
df.columns # 컬럼전체출력
df.columns[0]
df.columns[1]
df.columns[-1]     # 마지막 컬럼명 출력
df['SW특기']       # 마지막 컬럼 출력
df[df.columns[-1]] # 마지막 컬럼 출력
df[['이름','학교']]

df['이름']  #df[컬럼명만 들어갈수 있음]

# 컬럼 슬라이싱
df[ df.columns[[0,3,-1]] ] # 컬럼 슬라이싱
df[df.columns[1:4]]        # 컬럼 슬라이싱
df.columns[1:4]   # 컬럼명