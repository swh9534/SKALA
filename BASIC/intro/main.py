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

# 사용자가 입력한 문장을 그대로 출력하는 부분
def repeat_input():
    user_input = input("문장을 입력하세요: ")
    print("입력한 문장:", user_input)

if __name__ == "__main__":
    while True:
        # 사용자가 무엇을 할지 선택하도록 유도
        action = input("1. 문장 입력 (1)\n2. 비밀번호 검증 (2)\n3. 비밀번호 입력 및 검증 (3)\n종료하려면 'exit' 입력: ").lower()

        if action == 'exit':
            print("프로그램을 종료합니다.")
            break
        
        if action == '1':
            user_input = input("문장을 입력하세요: ")
            print("입력한 문장:", user_input)  # 문장을 그대로 출력
        elif action == '2':
            user_password = input("비밀번호를 입력하세요: ")
            print(validate_password(user_password))  # 비밀번호 검증
        elif action == '3':
            user_password = input("비밀번호를 입력하세요: ")
            print("입력한 비밀번호:", user_password)  # 입력한 비밀번호 출력
            print(validate_password(user_password))  # 비밀번호 검증
        else:
            print("올바른 선택을 해주세요.")