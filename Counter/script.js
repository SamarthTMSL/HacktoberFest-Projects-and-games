const inc = document.querySelector(".increase");
const dec = document.querySelector(".decrease");
const res = document.querySelector(".reset");
const num = document.querySelector("#count");

let n = 0;
console.log(num.innerText);
inc.addEventListener("click",function(){
    num.innerText=++n;  
    if(n == 0 ){
        num.style.color = "white";
    }
    if(n>0){
        num.style.color = "lawngreen";
    }
});
dec.addEventListener("click",function(){
    num.innerText=--n ; 
    if(n == 0 ){
        num.style.color = "white";
    }
    if(n<0){
        num.style.color = "red";
    }
});
res.addEventListener("click",function(){
    n = 0;
    num.innerText= n ; 
    num.style.color="white";
});