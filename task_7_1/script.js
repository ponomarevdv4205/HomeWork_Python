/*
1. Реализовать страницу корзины:
    a. Добавить возможность не только смотреть состав корзины, но и редактировать его,
        обновляя общую стоимость или выводя сообщение «Корзина пуста».

2. На странице корзины:
    a. Сделать отдельные блоки «Состав корзины», «Адрес доставки», «Комментарий»;
    b. Сделать эти поля сворачиваемыми;
    c. Заполнять поля по очереди, то есть давать посмотреть состав корзины, внизу которого
есть кнопка «Далее». Если нажать ее, сворачивается «Состав корзины» и открывается
«Адрес доставки» и так далее.
*/


// Мой каталог:
let myCatalog = {

    products: [
        {
        id: 0,
        name: 'Горный Велосипед UPLAND Count 200',
        image: 'img/Image1.png',
        description: 'Алюминиевый сплав',
        price: 41434,
        discount: -10,
        },
        {
        id: 1,
        name: 'Горный Велосипед UPLAND X200',
        image: 'img/Image2.png',
        description: 'Сталь',
        price: 14434,
        discount: -40,
        },
        {
        id: 2,
        name: 'Городской Велосипед EmpireAgro',
        image: 'img/Image3.png',
        description: 'Алюминиевый сплав',
        price: 12434,
        discount: 0,
        },
        {
        id: 3,
        name: 'Городской Велосипед EmpireAgro Раскладной',
        image: 'img/Image4.png',
        description: 'Алюминиевый сплав',
        price: 23434,
        discount: -10,
        },
        {
        id: 4,
        name: 'Велосипед CAPRIOLO MTB DIAVOLO DX 600',
        image: 'img/Image5.png',
        description: 'Сталь',
        price: 20434,
        discount: 0,
        },
        {
        id: 5,
        name: 'BMX Велосипед Tech Team Goof',
        image: 'img/Image6.png',
        description: 'Сталь',
        price: 15434,
        discount: 0,
        }
        ],

        clickHandler(event) {
		if ( event.target.className === 'top_button2' ) {
			const idx =  this.products.findIndex( item => {
				return item.id === +event.target.dataset.id;
			} );
			myBasket.addToBasket(this.products[idx]);
		}
	}
};

//Функция заполнения каталога элементами (товарами):
function drowItems() {
    myCatalog.products.forEach(function (item, i) {
        drowItem(item, i);
    })
};

const $catalog = document.querySelector('#catalog');
const $top_button = document.querySelector('#top_button');

function drowItem(item, id) {
    $catalog.insertAdjacentHTML('beforeend',
    `<div id="item-${id}" class="item__left">
                    <div class="p0">
                        <div class='sale_lable ${item.discount != 0 ? 'show' : ''}'>${item.discount}%</div>
                    </div>
                    <div class="img_center">
                        <img src="${item.image}" alt="Товар" title="Товар">
                    </div>
                    <h4 class="h4">Модель: ${item.name}</h4>
                    <p class="paragraph__top_elements_h4">Материал рамы: ${item.description}</p>
                    <h4 class="h42">Цена: ${item.price} рублей</h4>
                    <a data-id="${id}" href="#" class="top_button2">Добавить в корзину</a>
                </div>`)
};

// Моя корзина:
let myBasket = {

    items: [],

    getBasketLength() {
		return this.items.length;
	},

    addToBasket(product) {
		const idx = this.items.findIndex( item => {
			return item.productId === +product.id;
		} );

		if ( idx === -1 ) {
			this.items.push({
				id: this.items.length === 0 ? 0 : this.items[this.items.length - 1].id + 1,
				productId: product.id,
				name: product.name,
				price: product.price,
				discount: product.discount,
				count: 1,
				image: product.image,
			});
		} else {
			this.items[idx].count++;
		}
		this.renderBasket();
	},

    deleteFromBasket(id) {
		const indexItem = this.items.findIndex( (item) => {
			return item.id === +id;
		} );
		this.items.splice(indexItem, 1);
		this.renderBasket();
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

     renderBasket: function(){
        const $basket = document.querySelector('#basket');
        $basket.textContent = '';

        if (this.items.length === 0 ){
            $basket.insertAdjacentHTML('beforeend', `<div>Ваша корзина пуста!</div>`);
        }
        else {
            $basket.insertAdjacentHTML('beforeend', `В вашей корзине ${this.items.length} видов товаров (в количестве ${this.totalKolFun(this.items)} штук) на сумму ${this.totalSumFun(this.items)} рублей.`);
        }
    }
};

// Событие на кнопку "Добавить в корзину"
$catalog.addEventListener('click', (event) => {
    myCatalog.clickHandler(event);
}
);

// Очистка корзины
$top_button.addEventListener('click', function (e) {
    if (e.target.className ==='top_button') {
        myBasket.items = [];
        myBasket.renderBasket();
    }
});

// Событие на кнопку "Перейти в корзину"
const $top_button_list = document.querySelector('#top_button_list');
$top_button_list.addEventListener('click', (event) => {
    localStorage.setItem('myCatalog', JSON.stringify(myCatalog));
    localStorage.setItem('myBasket', JSON.stringify(myBasket));
}
);

drowItems(myCatalog.products);
myBasket.renderBasket();
