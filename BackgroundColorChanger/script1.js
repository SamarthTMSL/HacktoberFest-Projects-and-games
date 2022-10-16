const hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'];

const btn = document.querySelector(".click-me");
const color = document.querySelector("#code");
const bg = document.querySelector(".sec");
// console.log(bg);

function getRandomElement(){
    return Math.floor(Math.random() * hex.length);
}

btn.addEventListener("click",function(){
    let hexvalue = "#";
    for(let i = 0;i<6;i++){
        let random = getRandomElement();
        hexvalue += hex[random];
    }
    bg.style.backgroundColor = hexvalue;
    color.innerText = hexvalue;
})