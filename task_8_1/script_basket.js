/*
Это страница Корзины
*/

let myCatalog_1 = JSON.parse(localStorage.getItem('myCatalog'));
let myBasket_1 = JSON.parse(localStorage.getItem('myBasket'));

let myBasket_list = {
    myBasket_1,

    addToBasket_1(id) {
		const idx = this.myBasket_1.items.findIndex( item => {
			return item.id === +id;
		} );

		this.myBasket_1.items[idx].count++;
	},

	deleteFromBasket_1(id) {
		const idx = this.myBasket_1.items.findIndex( item => {
			return item.id === +id;
		} );

		if ( this.myBasket_1.items[idx].count === 1 ) {
			this.removeFromBasket_1(id);
		} else {
			this.myBasket_1.items[idx].count--;
		}
	},

	removeFromBasket_1(id) {
		const indexItem = this.myBasket_1.items.findIndex( (item) => {
			return item.id === +id;
		} );

		this.myBasket_1.items.splice(indexItem, 1);
	},

    clickHandler(event) {
		if ( event.target.className === 'top_button3 click_1' ) {
			const {id} = event.target.dataset
			this.addToBasket_1(id);
		}

        if ( event.target.className === 'top_button3 click_2' ) {
			const {id} = event.target.dataset
			this.deleteFromBasket_1(id);
		}

        if ( event.target.className === 'top_button3 click_3' ) {
			const {id} = event.target.dataset
			this.removeFromBasket_1(id);
		}

		drowItemsBasket_1(myBasket_1);
	},

    totalSumFun: function(mas){
        return mas.reduce(function(a, b){
            return +((a + b.price*(1+(b.discount/100))*b.count).toFixed(2));
            }, 0);
    },

    totalKolFun: function(mas){
        return mas.reduce(function(a, b){
            return +((a + b.count).toFixed(2));
            }, 0);
    },

	nextHandler() {
		const close = document.getElementById('close');

		let element = null;
		for ( let i = 0 ; i < close.children.length; i++) {
			if ( close.children[i].dataset.display === 'true' ) {
				element = close.children[i];
				element.dataset.display = false;
				element.style.display = 'none';

				if ( close.children[i + 1] ) {
					close.children[i + 1].dataset.display = true;
					close.children[i + 1].style.display = 'block';
				} else {
					close.children[0].dataset.display = true;
					close.children[0].style.display = 'block';
				}
				break;
			}
		}
	}
};

const $bas = document.querySelector('#basket_list');
const $bas0 = document.querySelector('#basket_list0');
const $basket_total = document.querySelector('#basket_total');
const $top_button_ = document.querySelector('#top_button_');
const $basket_list = document.querySelector('#basket_list');

function drowItemsBasket_1(mass) {

    $basket_total.textContent = '';
    $bas0.textContent = '';
    $bas.textContent = '';

    if (mass.items.length === 0 ){
            $basket_total.insertAdjacentHTML('beforeend', `<div>Ваша корзина пуста!</div>`);
            $bas0.insertAdjacentHTML('beforeend', `<div class="h3">Ваша корзина пуста!</div>`);
    }
    else {
    $bas0.insertAdjacentHTML('beforeend', `<div class="h3">Состав моей корзины:</div>`);
    $basket_total.insertAdjacentHTML('beforeend', `В вашей корзине ${myBasket_1.items.length} видов товаров (в количестве ${myBasket_list.totalKolFun(myBasket_1.items)} штук) на сумму ${myBasket_list.totalSumFun(myBasket_1.items)} рублей.`);

    mass.items.forEach(function (item, i) {

    $bas.insertAdjacentHTML('beforeend',
    `<div id="item-${i}" class="item__left2">
                    <div class="img_center2">
                        <img src="${item.image}" width="30%" height="30%" alt="Товар" title="Товар">
                    </div>
                    <h4 class="h4">Модель: ${item.name}</h4>
                    <h4 class="h42">Количество: ${item.count}</p>
                    <h4 class="h42">Общая стоимость (с учетом дисконта): ${((item.price*(1+(item.discount/100))*item.count).toFixed(2))} рублей</h4>
                    <div class="center_button0">
                        <a data-id="${i}" class="top_button3 click_1">Добавить "+1"</a>
                        <a data-id="${i}" class="top_button3 click_2">Удалить "-1"</a>
                        <a data-id="${i}" class="top_button3 click_3">Удалить из корзины</a>
                    </div>
                </div>`)
    })
    }
}

// Очистка корзины
$top_button_.addEventListener('click', function (e) {
    if (e.target.className === 'top_button_') {
        myBasket_1.items = [];
        drowItemsBasket_1(myBasket_1);
    }
});

// Событие на кнопки в товаре
$basket_list.addEventListener('click', function (e) {
    myBasket_list.clickHandler(e);
});

// Событие на кнопку "Оформить далее заказ"
const next = document.getElementById('next');
next.addEventListener('click', () => {
	myBasket_list.nextHandler();
	next.textContent = `Оформить далее заказ (Шаг № ${counter()})`;
});

// ЗАМЫКАНИЕ
function useCounter() {
    var Count = 2;
    return function() {
        if (Count > 3) { // это условие делаю для того, чтобы после ввода всех этапов оформления заказа вернуть счетчик в начальное положение
            Count = 1;
        }
        return Count++;
    };
};
var counter = useCounter();

drowItemsBasket_1(myBasket_1);
