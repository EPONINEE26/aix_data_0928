import pandas as pd

# 1차원 : Series, 2차원 : DataFrame 
# pandas : [] 리스트 구조, 데이터분석에 용이하게 만든 라이브러리 
# sum 작성하지 않아도 알아서 적용

# Series 변환 
temp = pd.Series([-20,-10,10,20])
print(temp)
print(temp[0])
# print(type(temp))
# print(type(1))
# print(type([1,2,3,4,5]))

# index 추가
temp = pd.Series([-20,-10,10,20], index=['Jan','Feb','Mar','Apr']) 
print(temp)
# # print(temp[0]) # index가 주어졌을 때는 0주소를 찾을 수 없음 
print(temp['Jan'])


