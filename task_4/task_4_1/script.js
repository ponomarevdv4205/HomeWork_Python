/*
1. Написать функцию, преобразующую число в объект. Передавая на вход число от 0 до 999,
надо получить на выходе объект, в котором в соответствующих свойствах описаны единицы,
десятки и сотни. Например, для числа 245 надо получить следующий объект: {‘единицы’: 5,
‘десятки’: 4, ‘сотни’: 2}. Если число превышает 999, необходимо выдать соответствующее
сообщение с помощью console.log и вернуть пустой объект.
*/

let a = prompt("Введите число от 0 до 999:");
let arr = Array.from(a);
let b = arr.reverse();

function myLet(b){
    if (+a <= 999 && +a > 0){
    myObject.transferObject(b);
    alert(`Вы ввели число: ${a}\n"единицы": ${myObject.units}, "десятки": ${myObject.dozens}, "сотни": ${myObject.hundreds}`);
    }
    else {
    alert(`ОШИБКА!!! Вы ввели не верное число!\n"единицы": ${myObject.units}, "десятки": ${myObject.dozens}, "сотни": ${myObject.hundreds}`);
    }
};

let myObject = {
    units: 0,
    dozens: 0,
    hundreds: 0,
    transferObject: function(b){
        if (b[0]){
            this.units = b[0];
        };
        if (b[1]){
            this.dozens = b[1];
        };
        if (b[2]){
            this.hundreds = b[2];
        };
    }
};

myLet(b);
