//声明一个实例对象
let xhr = new XMLHttpRequest();

xhr.open('GET', 'https://dog.ceo/api/breeds/image/random')
//向服务器发送请求
xhr.send()

xhr.onload = function () {
    let date = JSON.parse(xhr.response);
    console.log('date.message')
    pic.src = `${date.message}`
}  