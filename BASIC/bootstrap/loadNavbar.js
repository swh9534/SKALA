document.addEventListener("DOMContentLoaded", function () {
    let navbarContainer = document.getElementById("navbar-container");

    fetch("../navbar.html")
        .then((response) => response.text())
        .then((data) => {
            navbarContainer.innerHTML = data;

            // 🔹 현재 페이지가 sub 폴더에 있는지 확인
            let homeLink = navbarContainer.querySelector(".home-link");
            if (homeLink) {
                let currentPath = window.location.pathname;
                if (currentPath.includes("/sub/")) {
                    homeLink.href = "../index.html"; // 하위 폴더에서는 ../index.html
                } else {
                    homeLink.href = "index.html"; // 최상위 폴더에서는 index.html
                }
            }

            // 🔹 부트스트랩 기능 다시 활성화 (Dropdown & Offcanvas)
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
