const simple = ['red','green','blue', 'pink', 'neon', 'aquablue', 'yellow','violet', 'purple', 'grey', 'orange','gold']

const btn = document.querySelector(".click-me");
const color = document.querySelector("#code");
const bg = document.querySelector(".sec");
console.log(bg);
function getRandomElement(){
    return Math.floor(Math.random() * simple.length);
}


btn.addEventListener("click",function(){
    let random = getRandomElement();
    bg.style.backgroundColor = simple[random];
    color.innerText = simple[random];
});
