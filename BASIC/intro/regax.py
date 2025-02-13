import re

def validate_password(password):
    """
    비밀번호 검증 함수
    조건:
    - 최소 하나의 소문자 [a-z]
    - 최소 하나의 대문자 [A-Z]
    - 최소 하나의 숫자 [0-9]
    - 최소 하나의 특수문자 [!@#$%^&*(),.?":{}|<>]
    - 최소 8자 이상
    """
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*(),.?\":{}|<>]).{8,}$"
    
    if re.match(pattern, password):
        return "✅ 유효한 비밀번호입니다!"
    else:
        return "❌ 비밀번호는 최소 8자 이상이며, 대소문자/숫자/기호를 포함해야 합니다."

# 테스트 실행
if __name__ == "__main__":
    while True:
        user_password = input("비밀번호를 입력하세요 (종료하려면 'exit'): ")
        if user_password.lower() == "exit":
            print("프로그램을 종료합니다.")
            break
        print(validate_password(user_password))