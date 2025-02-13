import requests

def get_github_user_info(username):
    """
    GitHub 사용자 정보를 가져오는 함수.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"사용자를 찾을 수 없습니다. 상태 코드: {response.status_code}"}

def get_github_repo_info(username, repo_name):
    """
    GitHub 레포지토리 정보를 가져오는 함수.
    """
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"레포지토리를 찾을 수 없습니다. 상태 코드: {response.status_code}"}

def main():
    username = input("GitHub 계정명을 입력하세요: ")  
    user_info = get_github_user_info(username)

    if "error" in user_info:
        print(user_info["error"])
        return  # 사용자 정보가 없으면 종료

    # 사용자 정보 출력
    print(f"\nGitHub 사용자 정보 ({username}):")
    print(f"로그인 이름: {user_info['login']}")
    print(f"이름: {user_info.get('name', '없음')}")
    print(f"블로그: {user_info.get('blog', '없음')}")
    print(f"팔로워 수: {user_info['followers']}")
    print(f"팔로잉 수: {user_info['following']}")
    print(f"계정 생성일: {user_info['created_at']}")

    repo_name = input("\n조회할 레포지토리 이름을 입력하세요: ")
    repo_info = get_github_repo_info(username, repo_name)

    if "error" in repo_info:
        print(repo_info["error"])
        return  # 레포지토리 정보가 없으면 종료

    # 레포지토리 정보 출력
    print(f"\nGitHub 레포지토리 정보 ({repo_name}):")
    print(f"설명: {repo_info.get('description', '없음')}")
    print(f"언어: {repo_info.get('language', '없음')}")
    print(f"스타 개수: {repo_info['stargazers_count']}")
    print(f"포크 개수: {repo_info['forks_count']}")
    print(f"레포지토리 생성일: {repo_info['created_at']}")

if __name__ == "__main__":
    main()