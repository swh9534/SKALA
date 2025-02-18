document.addEventListener("DOMContentLoaded", function () {
    let navbarContainer = document.getElementById("navbar-container");

    // 현재 문서의 경로 확인
    let depth = (window.location.pathname.match(/\//g) || []).length;

    // navbar.html의 상대 경로 설정
    let navbarPath = depth > 1 ? "../../navbar.html" : "../navbar.html";

    fetch(navbarPath)
        .then((response) => response.text())
        .then((data) => {
            navbarContainer.innerHTML = data;

            // 🔹 홈 버튼 경로 자동 조정
            let homeLink = navbarContainer.querySelector(".home-link");
            if (homeLink) {
                let currentPath = window.location.pathname;
                let homePath = depth > 1 ? "../../main.html" : "../main.html";
                homeLink.href = homePath;
            }

            // 🔹 부트스트랩 기능 다시 활성화
            setTimeout(() => {
                if (typeof bootstrap !== "undefined") {
                    let dropdowns =
                        document.querySelectorAll(".dropdown-toggle");
                    dropdowns.forEach(
                        (dropdown) => new bootstrap.Dropdown(dropdown)
                    );

                    let offcanvas = document.querySelectorAll(".offcanvas");
                    offcanvas.forEach(
                        (panel) => new bootstrap.Offcanvas(panel)
                    );
                } else {
                    console.error("Bootstrap이 로드되지 않았습니다!");
                }
            }, 100);
        })
        .catch((error) => console.error("Navbar 로드 오류:", error));
});
