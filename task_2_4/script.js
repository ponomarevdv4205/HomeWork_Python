/*
4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch
организовать вывод чисел от a до 15.
*/

var a = Math.floor(Math.random()*16);

document.write(`Случайное число (a) равно: ${a}<br>`);
document.write("Вывод чисел от a до 15 с помощью оператора switch: <br>");

switch(a){
    case 0:
        document.write("0<br>");
    case 1:
        document.write("1<br>");
    case 2:
        document.write("2<br>");
    case 3:
        document.write("3<br>");
    case 4:
        document.write("4<br>");
    case 5:
        document.write("5<br>");
    case 6:
        document.write("6<br>");
    case 7:
        document.write("7<br>");
    case 8:
        document.write("8<br>");
    case 9:
        document.write("9<br>");
    case 10:
        document.write("10<br>");
    case 11:
        document.write("11<br>");
    case 12:
        document.write("12<br>");
    case 13:
        document.write("13<br>");
    case 14:
        document.write("14<br>");
    default:
        document.write("15");
}
