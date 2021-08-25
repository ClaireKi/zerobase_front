# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 기본출력
print('Hello Python!')
print("Hello Python!")
print("""Hello Python!""")
print('''Hello Python!''')

print()


# Separator 옵션 사용하기 : sep 값을 각 문자열 중간에 넣어 문자열 연결
print('T', 'E', 'S', 'T')
print('T', 'E', 'S', 'T', sep='') 
print('2019', '02', '19', sep='-') 
print('niceman','google.com', sep='@') # 이메일 주소 받을 때 유용 = 회원가입 개인정보 수집에 이용될 수 있을 듯

print()


# end 옵션 사용하기 : end 값을 문자열 끝에 넣고 문장 줄바꿈 없이 그 자리에서 끝냄
print('Welcome To', end=' ')
print('the black paradise', end=' ')
print('piano notes')
print('testline') # end 옵션이 없으므로 문장 줄바꿈 됨

print()


# format 사용하기
print('{} and {}'.format('You', 'Me'))
print("{0} and {1} and {0}".format('You', 'Me')) # format은 mapping이 가능하다
print("{a} and {bravo}".format(a='You', bravo='Me')) # mapping시에 변수 활용 가능
print("%s's favorite number is %d" %('SY', 8)) # %s , %d, %f

print()

print("Test1: %5d, Test2: %-5d, Price: %4.2f" %(1234.1234, 1234.1234, 6534.123)) # %5d 는 기본 5자리 표시 숫자가 5자리보다 더 되면 정수만 떼어서 전체 표시 / - 붙이면 왼쪽정렬
print("Test1: {0: 5d}, Price: {1: 4.2f}".format(776, 6534.123)) # 중괄호 묶을 시 % 필요 없음
print("Test1: {a: 5d}, Price: {b: 4.2f}".format(a=776, b=6534.123))

print()


# escape문 사용하기
print("'you'")
print('\'you\'')
print('"you"')
print("""'you'""")
print('\\you\\\n')
print('\ttest')