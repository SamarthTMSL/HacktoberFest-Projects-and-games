const hourHand = document.querySelector(".hour-hand");
const minuteHand = document.querySelector(".min-hand");
const secondHand = document.querySelector(".second-hand");

setInterval(() => {
  setTime();
}, 1000);

function setTime() {
  const currentDate = new Date();
  const hourDegree = ((currentDate.getHours() % 12) / 12) * 360 + 90;
  const minuteDegree = ((currentDate.getMinutes() % 60) / 60) * 360 + 90;
  const secondDegree = ((currentDate.getSeconds() % 60) / 60) * 360 + 90;

  setRotationStyles(hourDegree, minuteDegree, secondDegree);
}

function setRotationStyles(hourDegree, minuteDegree, secondDegree) {
  hourHand.style.webkitTransform = `rotate(${hourDegree}deg)`;
  hourHand.style.MozTransform = `rotate(${hourDegree}deg)`;
  hourHand.style.msTransform = `rotate(${hourDegree}deg)`;
  hourHand.style.OTransform = `rotate(${hourDegree}deg)`;
  hourHand.style.transform = `rotate(${hourDegree}deg)`;

  minuteHand.style.webkitTransform = `rotate(${minuteDegree}deg)`;
  minuteHand.style.MozTransform = `rotate(${minuteDegree}deg)`;
  minuteHand.style.msTransform = `rotate(${minuteDegree}deg)`;
  minuteHand.style.OTransform = `rotate(${minuteDegree}deg)`;
  minuteHand.style.transform = `rotate(${minuteDegree}deg)`;

  secondHand.style.webkitTransform = `rotate(${secondDegree}deg)`;
  secondHand.style.MozTransform = `rotate(${secondDegree}deg)`;
  secondHand.style.msTransform = `rotate(${secondDegree}deg)`;
  secondHand.style.OTransform = `rotate(${secondDegree}deg)`;
  secondHand.style.transform = `rotate(${secondDegree}deg)`;
}
