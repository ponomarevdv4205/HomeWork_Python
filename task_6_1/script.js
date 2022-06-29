/*
1. Продолжаем реализовывать модуль корзины:
    a. Добавлять в объект корзины выбранные товары по клику на кнопке «Купить» без
перезагрузки страницы;
    b. Привязать к событию покупки товара пересчет корзины и обновление ее внешнего
вида.
*/

// Мой каталог:
let myCatalog = {

    products: [
        {
        product: 'Горный Велосипед UPLAND Count 200',
        image: 'img/Image1.png',
        description: 'Алюминиевый сплав',
        price: 41434,
        discount: -10,
        },
        {
        product: 'Горный Велосипед UPLAND X200',
        image: 'img/Image2.png',
        description: 'Сталь',
        price: 14434,
        discount: -40,
        },
        {
        product: 'Городской Велосипед EmpireAgro',
        image: 'img/Image3.png',
        description: 'Алюминиевый сплав',
        price: 12434,
        discount: 0,
        },
        {
        product: 'Городской Велосипед EmpireAgro Раскладной',
        image: 'img/Image4.png',
        description: 'Алюминиевый сплав',
        price: 23434,
        discount: -10,
        },
        {
        product: 'Велосипед CAPRIOLO MTB DIAVOLO DX 600',
        image: 'img/Image5.png',
        description: 'Сталь',
        price: 20434,
        discount: 0,
        },
        {
        product: 'BMX Велосипед Tech Team Goof',
        image: 'img/Image6.png',
        description: 'Сталь',
        price: 15434,
        discount: 0,
        }
        ]
};

// Функция заполнения каталога элементами (товарами):
function drowItems() {
    myCatalog.products.forEach(function (item, i) {
        drowItem(item, i);
    });
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
                    <h4 class="h4">Модель: ${item.product}</h4>
                    <p class="paragraph__top_elements_h4">Материал рамы: ${item.description}</p>
                    <h4 class="h42">Цена: ${item.price} рублей</h4>
                    <a data-id="${id}" href="#" class="top_button2">Добавить в корзину</a>
                </div>`);
};
drowItems(myCatalog.products);

// Моя корзина:
let myBasket = {
    products: [],

    totalSumFun: function(mas){
        return mas.reduce(function(a, b){
            return +((a + b.price*(1+(b.discount/100))).toFixed(2));
            }, 0);
    },

     renderBasket: function(){
        const $basket = document.querySelector('#basket');
        $basket.textContent = '';

        if (this.products.length === 0 ){
            $basket.insertAdjacentHTML('beforeend', `<div>Ваша корзина пуста!</div>`);
        }
        else {
            $basket.insertAdjacentHTML('beforeend', `В вашей корзине ${this.products.length} товаров на сумму ${this.totalSumFun(this.products)} рублей.`);
        };
    }
};

// Добавление товара в корзину
$catalog.addEventListener('click', function (e) {
    if (e.target.className ==='top_button2') {
        const id = Number(e.target.getAttribute('data-id'));
        const choice = myCatalog.products[id];
        myBasket.products.push({"product": choice.product, "price": choice.price, "discount": choice.discount});
        myBasket.renderBasket();
    }
});

// Очистка корзины
$top_button.addEventListener('click', function (e) {
    if (e.target.className ==='top_button') {
        myBasket.products = [];
        myBasket.renderBasket();
    }
});

myBasket.renderBasket();
