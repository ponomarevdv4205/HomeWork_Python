/*
5. Реализовать четыре основные арифметические операции в виде функций с двумя
параметрами. Обязательно использовать оператор return.
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


let perFunSum = funSum(x, y);
let perFunRaz = funRaz(x, y);
let perFunPro = funPro(x, y);
let perFunDel = funDel(x, y);

document.write(`Задано число х = ${x} и y = ${y}.<br>`);
document.write("Четыре основных арифметических операции в виде функций с двумя параметрами и их результат:<br>");
document.write(`Сложение: ${perFunSum}<br>`);
document.write(`Разность: ${perFunRaz}<br>`);
document.write(`Умножение: ${perFunPro}<br>`);
document.write(`Деление: ${perFunDel}<br>`);
