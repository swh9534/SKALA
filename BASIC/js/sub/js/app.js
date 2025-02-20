import { add, divide, multiply, subtract } from "./math.js"; // math.js에서 함수 가져오기

function calculate(operation) {
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let resultElement = document.getElementById("result");

    if (isNaN(num1) || isNaN(num2)) {
        resultElement.textContent = "숫자를 입력하세요!";
        return;
    }

    let result;
    switch (operation) {
        case "add":
            result = add(num1, num2);
            break;
        case "subtract":
            result = subtract(num1, num2);
            break;
        case "multiply":
            result = multiply(num1, num2);
            break;
        case "divide":
            result = divide(num1, num2);
            break;
        default:
            result = "잘못된 연산입니다!";
    }

    resultElement.textContent = `결과: ${result}`;
}

// 전역에서 사용할 수 있도록 window 객체에 바인딩
window.calculate = calculate;
