/*
2. Продолжить работу с интернет-магазином:
   a. В прошлом домашнем задании вы реализовали корзину на базе массивов. Какими
объектами можно заменить их элементы?
   b. Реализуйте такие объекты.
   c. Перенести функционал подсчета корзины на объектно-ориентированную базу
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
    }
};

document.write(`Стоимость корзины равна:<br>${myBasket.totalSumFun(myBasket.products)}`);
