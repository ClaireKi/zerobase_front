# Section04-1
# 데이터 타입
v_str1 = "Niceman"
v_bool = True
v_str2 = "Goodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 타입 출력 type()
print(type(v_tuple))
print(type(v_set))
print(type(v_float))

print('--------------------------------------------------------------------------------')

# 계산시 형변환
i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5
f4 = 10.

print(i1 * i2, type(i1 * i2))
print(big_int1 * big_int2, type(big_int1 * big_int2))
print(f1 ** f2, type(f1 ** f2))
print(f3 + i2, type(f3 + i2))

result = f3 + i2
print(result, type(result))

print('--------------------------------------------------------------------------------')

# 형변환
# int, float, complex(복소수)
a = 5.
b = 4

print(type(a), type(b))
result2 = a + b

print(result2, type(result2))
print(int(result2))             # float -> int
print(float(b))                 # int -> float
print(complex(3))               # int -> complex
print(int(True))                # boolean -> int
print(int(False))               # boolean -> int
print(int('3'))                 # string -> int     // 파이썬에는 char가 없음
print(complex(False))           # boolean -> complex
print('--------------------------------------------------------------------------------')

# 단항 연산자

y = 100
y += 100
print(y)

print('--------------------------------------------------------------------------------')

# 수치 연산 함수
print(abs(-7))
n, m = divmod(100, 8)           # n = 몫 / m = 나머지
print(n, m)

import math

print(math.ceil(5.1))           # 5.1 바로 위에 있는 정수
print(math.floor(3.874))        # 3.874 바로 밑에 있는 정수
