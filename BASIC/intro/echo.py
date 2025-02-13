# 무한 루프로 사용자 입력을 계속 받는 Python 3 프로그램
while True:
    user_input = input("문장을 입력하세요 (종료하려면 'exit' 입력): ")
    
    if user_input.lower() == "exit":  # 'exit' 입력 시 종료
        print("프로그램을 종료합니다.")
        break
    
    print("입력한 문장:", user_input)