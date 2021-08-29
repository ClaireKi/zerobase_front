# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리 (Dictionary) : 순서 x, 중복 x , 수정ㅇ, 삭제ㅇ
# Key, Value 형식
# Json 형식이랑 비슷함 -> mongoDB등

# 선언
a = {'name': 'Kim', 'Phone': '010-1234-1234', 'birth': 980831}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]}    # value 부분에는 어떤 자료형이든 올 수 있음 = 매우 유연하게 사용 가능

print(type(a))
print('--------------------------------------------------------------------------------')

# 출력 - key로 조회
print(a['name'])
#print(a['name1'])              # 에러 = name1이라는 키가 없기 때문에
print(a.get('name'))            # .get('key') : key로 value 가져옴
print(a.get('address'))         # .get('key') 메소드 같은 경우에는 key가 없는 값이여도 에러가 뜨지 않으므로(none출력) 안전한 코딩법임
print(c['arr'][1:3])            # arr이라는 키의 value값을 인덱스 1부터 2까지 출력

print('--------------------------------------------------------------------------------')

# 딕셔너리 추가
a['address'] = 'Seoul'          # 딕셔너리명['key명'] = value
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2, 3)
print(a)

print('--------------------------------------------------------------------------------')

# keys, values, items(쌍)
print(a.keys())                 # 딕셔너리명.keys() : 키만 리스트 형태로 가져옴
# print(a.keys()[0])            # 에러 O
print(list(a.keys())[0])        # 에러 X

print(a.values())               # 딕셔너리명.values() : 밸류만 리스트 형태로 가져옴
print(list(a.values())[0])

print(a.items())                # 딕셔너리명.items() : 쌍을 리스트 형태로 가져옴
print(list(a.items())[0])       
print(type(list(a.items())[0])) # 리스트 안에 튜플이 들어간 형태로 반환

print('--------------------------------------------------------------------------------')


# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])

print(type(a))
print(c)                        # 6 중복 제거 후 출력

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(s1.intersection(s2))      # 교집합 출력 1
print(s1 & s2)                  # 교집합 출력 2

print(s1.union(s2))             # 합집합 출력 1
print(s1 | s2)                  # 합집합 출력 2

print(s1.difference(s2))        # 차집합 출력 1
print(s1-s2)                    # 차집합 출력 2

# 집합 추가 & 제거
s3 = set([7, 8, 10, 15])
s3.add(18)
print(s3)
s3.remove(7)
print(s3)