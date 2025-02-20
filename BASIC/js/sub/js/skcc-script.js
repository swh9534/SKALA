const users = [{ name: "신우현", password: "1234" }];

document.addEventListener("DOMContentLoaded", function () {
    const users = [{ name: "신우현", password: "1234" }];
    const loginButton = document.getElementById("loginButton");

    loginButton.addEventListener("click", function () {
        let username = document.getElementById("username").value.trim();
        let password = document.getElementById("password").value.trim();
        let errorMessage = document.getElementById("error-message");

        // 유효성 검사 - 이름 또는 비밀번호 미입력 시 alert 표시
        if (username === "" || password === "") {
            alert("이름과 비밀번호를 모두 입력해주세요!");
            errorMessage.style.display = "block";
            return;
        }

        // 비밀번호 숫자만 입력 가능 (정규식 활용)
        if (!/^\d+$/.test(password)) {
            alert("비밀번호는 숫자만 입력할 수 있습니다!");
            errorMessage.style.display = "block";
            return;
        }

        // 로그인 검증
        let isValidUser = users.some(
            (user) => user.name === username && user.password === password
        );

        if (isValidUser) {
            alert("로그인 성공!");
            window.location.href = "skmain.html"; // 로그인 성공 시 이동
        } else {
            alert("로그인 실패! 이름 또는 비밀번호를 확인하세요.");
            errorMessage.style.display = "block";
        }
    });
});
