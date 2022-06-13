/*
1. С помощью цикла while вывести все простые числа в промежутке от 0 до 100.
*/

document.write("Все простые числа в промежутке от 0 до 100:<br>");
let flag = true;
for (let i = 1; i < 101; i++){
    if (i === 1){
    document.write(`${i}<br>`);
    continue;
    }
    for (let j = i - 1; j > 1; j--){
        if (i % j === 0){
        flag = false;
        }
    }
    if (flag === true){
        document.write(`${i}<br>`);
    }
    flag = true;
}
