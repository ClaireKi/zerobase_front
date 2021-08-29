# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요
# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1)
    v1 += 1

print('--------------------------------------------------------------------------------')

for v2 in range(10):
    print("v2 is :", v2)

print('--------------------------------------------------------------------------------')

for v3 in range(1, 11):
    print("v3 is :", v3)

print('--------------------------------------------------------------------------------')

# 1부터 100까지 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 += 1

print('1~100 : ', sum1)
print('1~100 : ', sum(range(1,101)))
print('1~100 : ', sum(range(1, 101, 2)))        # 2개 단위로 건너뛰면서 합산
print('--------------------------------------------------------------------------------')

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable : range, reversed, enumerate, filter, map, zip

names = ['Kim', 'Park', 'Cho']

for name in names:
    print("Your name : ", name)
print('--------------------------------------------------------------------------------')

word = "Dreams"

for s in word:
    print("Word : ", s)
print('--------------------------------------------------------------------------------')

my_info = {
    "name" : "Kim",
    "age" : 24,
    "city" : "Seoul"
}

# 기본은 key로 받아옴
for info in my_info:
    print("my_info : ", info)
print('--------------------------------------------------------------------------------')

# 값
for value in my_info.values():
    print("value : ", value)
print('--------------------------------------------------------------------------------')

# 키
for key in my_info.keys():
    print("key : ", key)
print('--------------------------------------------------------------------------------')

# 쌍 튜플로 받기
for item in my_info.items():
    print("item :", item)
print('--------------------------------------------------------------------------------')

# 쌍 따로 받기
for k, v in my_info.items():
    print("item : ", k, v)
print('--------------------------------------------------------------------------------')

# Q. 대문자는 소문자로 소문자는 대문자로
name = "KennRY"         # 문자열은 immutable이라서 자체는 안바뀜
temp = []               # 그래서 리스트로 하나씩 받은 다음에 이어줄거임

# 한글자씩 가져오기
for word in name:
    # 소문자 대문자 구분
    if word.isupper() == True:
        temp.append(word.lower())
    else:
        temp.append(word.upper())
print(temp)
print(''.join(temp))
print('--------------------------------------------------------------------------------')

# break
numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 36, 38]
lengthOfNumbers = len(numbers)
idx = 0
for number in numbers:
    if number == 38:
        print("리스트의 인덱스", idx, '에 존재합니다.')
        break
    if idx == lengthOfNumbers - 1:
        print("리스트에 존재하지 않습니다.")
    idx += 1
print('--------------------------------------------------------------------------------')

# for - else 구문(반복문이 정상적으로 수행된 경우 else블럭 수행)
for number in numbers:
    if number == 38:
        print("리스트에 존재합니다.")
        break
else:
    print("리스트에 존재하지 않습니다.")
print('--------------------------------------------------------------------------------')

# continue
lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float:
        continue                # 밑으로 안 내려가고 다음 반복문 실행
    print("타입: ", type(v))
print('--------------------------------------------------------------------------------')

name = "Niceman"
print(reversed(name))
print(list(reversed(name)))
print(name[::-1])