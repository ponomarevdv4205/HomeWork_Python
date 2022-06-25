/*
2. Сделать генерацию корзины динамической: верстка корзины не должна находиться в
HTML-структуре. Там должен быть только div, в который будет вставляться корзина,
сгенерированная на базе JS:
   a. Пустая корзина должна выводить строку «Корзина пуста»;
   b. Наполненная должна выводить «В корзине: n товаров на сумму m рублей».
*/


let myBasket = {

    products: [
        {
        name: "Товар 1",
        prices: 100,
        count: 1,
        },
        {
        name: "Товар 2",
        prices: 200,
        count: 2,
        },
        {
        name: "Товар 3",
        prices: 300,
        count: 3,
        }
        ],

    totalSum: 0,

    totalSumFun: function(mas){
        return totalSum = mas.reduce(function(a, b){
            return a + (b.prices*b.count);
            }, 0);
    },

     renderBasket: function(mas){
        const cartWrapperElem = document.getElementById('cart');
        const cartElem = document.createElement('div');

        if (this.products.length === 0 ){
            cartElem.textContent = "Корзина пуста!";
        }
        else {
            cartElem.textContent = `Корзина не пуста. В корзине ${this.products.length} товаров на сумму ${this.totalSumFun(this.products)} рублей.`;


        };
        cartWrapperElem.appendChild(cartElem);
    }
};

myBasket.renderBasket(myBasket.products);
