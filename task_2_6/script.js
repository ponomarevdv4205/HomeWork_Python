/*
6. Реализовать функцию с тремя параметрами: function mathOperation(arg1, arg2, operation),
где arg1, arg2 — значения аргументов, operation — строка с названием операции. В
зависимости от переданного значения выполнить одну из арифметических операций
(использовать функции из пункта 5) и вернуть полученное значение (применить switch).
*/

let x = 5;
let y = 3;

function funSum(x, y){
    return x + y;
}

function funRaz(x, y){
    return x - y;
}

function funPro(x, y){
    return x * y;
}

function funDel(x, y){
    return x / y;
}

function mathOperation(arg1, arg2, operation){
    switch(operation){
        case "сложение":
            return funSum(arg1, arg2);
        case "разность":
            return funRaz(arg1, arg2);
        case "умножение":
            return funPro(arg1, arg2);
        case "деление":
            return funDel(arg1, arg2);
        default:
            return "введена не правильная операция!";
    }
}

var operation = prompt(`Задано число х = ${x} и y = ${y}. Введите операцию с ними (сложение, разность, умножение или деление):`);

alert(`Результат равен: ${mathOperation(x, y, operation)}`);
