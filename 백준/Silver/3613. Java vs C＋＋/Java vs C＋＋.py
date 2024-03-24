# C++ → Java 함수
def cpp_to_java(variable):
    error = "Error!"
    converted_strings = []

    # 에러 발생 경우
    # 1. 변수명에 “__”가 존재하는 경우
    if "__" in variable:
        return error
    # 2. 변수명의 첫번째 글자 또는 마지막 글자가 “_”인 경우
    if variable[0] == "_" or variable[-1] == "_":
        return error
    # 3. 변수에 대문자가 포함되어 있는 경우
    if variable.islower() == False: # islower(): 모두 소문자인지 확인
        return error
    
    # 구분자(”_”)로 나눠진 단어를 꺼내 변환히기
    for word in variable.split("_"):
        # 첫번째로 꺼낸 단어는 그대로 리스트에 저장
        if len(converted_strings) == 0:
            converted_strings.append(word)
        # 그 이후 단어부터는 첫번째 글자를 대문자로 바꿔서 넣음
        else:
            converted_strings.append(word.capitalize())

    return "".join(converted_strings) # 변환된 문자열을 합쳐서 리턴


# Java → C++ 함수
def javaToCpp(variable):
    error = "Error!"
    converted_strings = []

    # 한 글자씩 꺼내서 처리함
    for i in range(len(variable)):
        # 대문자인 경우
        if variable[i].isupper():
            # 변수명의 첫번째 문자가 대문자인 경우 에러 발생
            if i == 0:
                return error
            else: # f-string으로 "_소문자"를 리스트에 저장
                converted_strings.append(f"_{variable[i].lower()}")
        # 소문자면 리스트에 그대로 넣는다.
        else:
            converted_strings.append(variable[i])
    
    return "".join(converted_strings) # 변환된 문자열을 합쳐서 리턴


variable = input() # 변수명 입력받음

# 먼저 입력된 변수명에 밑줄이 있는지 확인함
if "_" in variable:
    print(cpp_to_java(variable))
else:
    print(javaToCpp(variable))
