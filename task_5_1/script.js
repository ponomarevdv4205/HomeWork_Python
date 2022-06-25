/*
1. Создать функцию, генерирующую шахматную доску. Можно использовать любые html-теги.
Доска должна быть верно разлинована на черные и белые ячейки. Строки должны
нумероваться числами от 1 до 8, столбцы — латинскими буквами A, B, C, D, E, F, G, H.
*/

const body = document.body;
body.insertAdjacentHTML('afterbegin', '<div class="chessBoard"></div>');

const letters = ["", "A", "B", "C", "D", "E", "F", "G", "H", ""];
const numbers = ["", "8", "7", "6", "5", "4", "3", "2", "1", ""];

function createChessBoord(){
    let table = document.createElement('table');

    for (let row = 0; row < letters.length; row++) {
        let tr = document.createElement("tr");
        table.append(tr);

        for (let col = 0; col < numbers.length; col++) {
            let td = document.createElement("td");
            td.style.width = "60px";
            td.style.height = "60px";
            td.style.textAlign = "center";

            if (row == 0 || row == 9) {
                td.textContent = letters[col];
            }
            else if (col == 0 || col == 9) {
                td.textContent = numbers[row];
            }
            else {
                if ((row + col) % 2 == 1) {
                    td.style.backgroundColor = 'black';
                }
            }
            tr.append(td);
        }
    }
    body.querySelector('.chessBoard').append(table);
}

createChessBoord();
