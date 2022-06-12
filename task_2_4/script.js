/*
4. Присвоить переменной а значение в промежутке [0..15]. С помощью оператора switch
организовать вывод чисел от a до 15.
*/

var a = Math.floor(Math.random()*16);

document.write(`Случайное число (a) равно: ${a}<br>`);
document.write("Вывод чисел от a до 15 с помощью оператора switch: <br>");

switch(a){
    case 0:
        document.write("0<br>1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 1:
        document.write("1<br>2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 2:
        document.write("2<br>3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 3:
        document.write("3<br>4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 4:
        document.write("4<br>5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 5:
        document.write("5<br>6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 6:
        document.write("6<br>7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 7:
        document.write("7<br>8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 8:
        document.write("8<br>9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 9:
        document.write("9<br>10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 10:
        document.write("10<br>11<br>12<br>13<br>14<br>15");
        break;
    case 11:
        document.write("11<br>12<br>13<br>14<br>15");
        break;
    case 12:
        document.write("12<br>13<br>14<br>15");
        break;
    case 13:
        document.write("13<br>14<br>15");
        break;
    case 14:
        document.write("14<br>15");
        break;
    default:
        document.write("15");
}
