import pandas as pd

# 1차원데이터 - Series 
# temp = pd.Series([-20,-10,0,10,20], index=['1월','2월','3월','4월','5월'])
# print(temp)
# print(['1월'])
# print([['1월','2월']]) # 2개 데이터 검색시 [[]]

#2차원데이터 - DataFrame : 딕셔너리 타입의 리스트 형태로 되어짐. 

data = {
    '이름':['강나래','강태원','강호림','김수찬','김재욱','박동현','박혜정','승근열'],
    '학교':['신림고','신림고','신림고','신림고','신림고','디지털고','디지털고','디지털고'],
    '키':[197,184,168,187,188,202,188,190],
    '국어' : [90, 40, 80, 40, 15, 80, 55, 100],
    '영어' : [85, 35, 75, 60, 20, 100, 65, 85],
    '수학' : [100, 50, 70, 70, 10, 95, 45, 90],
    '과학' : [95, 55, 80, 75, 35, 85, 40, 95],
    '사회' : [85, 25, 75, 80, 10, 80, 35, 95],
    'SW특기' : ['Python', 'Java', 'Javascript', '', '', 'C', 'PYTHON', 'C#']
}

# DataFrame 변환 
df = pd.DataFrame(data)
print(df)

# index 추가 
# 사용 이유 : 판다스로 변환하면 파이썬 리스트타입 보다 계산이 더 용이함 
df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번']) # index 추가하여 사용
print(df)

# DataFrame 생성후 index를 지정 
df = pd.DataFrame(data) 
df.set_index('이름') # 이름이라는 컬럼 (인덱스) 지정 
print(df)

# index를 지정하고 index 컬럼 이름을 지정할 수 있음 
df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번']) 
df.index.name = '지원번호' 
print(df)

# index 지정 해제방법 : drop=True:index를 삭제하지만 반영은 안됨 / inplace=True: 삭제시킨 후 완전히 반영시켜저장 
df = pd.DataFrame(data, index=['1번','2번','3번','4번','5번','6번','7번','8번']) 
df.index.name = '지원번호'
df.reset_index(inplace=True) 
print(df.reset_index(drop=True)) # 지원번호 컬럼부분을 삭제
print(df)

df = pd.DataFrame(data) 
print(df.set_index('이름', inplace=True)) # 이름컬럼을 index로 지정되었던 코드가 inplace=True가 있으면서 이름이 제일 앞에 출력됨
print(df)

# sort_index : index 정렬 inplace=True:완전지정되어 저장
df = pd.DataFrame(data) 
df.set_index('이름', inplace=True)
df.sort_index(inplace=True)
print(df)

# ascending=True : 순차정렬 ascending=False : 역순정렬 
df = pd.DataFrame(data) 
df.set_index('이름', inplace=True)
df.sort_index(inplace=True, ascending=False) 
print(df)



