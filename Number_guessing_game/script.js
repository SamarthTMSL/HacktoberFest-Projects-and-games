var msg1 = document.getElementById("message1");
var msg2 = document.getElementById("message2");
var msg3 = document.getElementById("message3");

var answer = Math.floor(Math.random() * 100) + 1;
var no_of_guesses = 0;
var guessed_nums = [];
var hint = [];
var index = 0;

function test_prime(n) {
    if (n === 1) {
        return false;
    }
    else if (n === 2) {
        return true;
    } else {
        for (var x = 2; x < n; x++) {
            if (n % x === 0) {
                return false;
            }
        }
        return true;
    }
}

function create_hints() {
    if (answer % 10 === 0) {
        hint.push("Number is divisible by 10.");
    }
    if (answer % 2 === 0) {
        hint.push("Number is Even.");
    }
    else {
        hint.push("Number is Odd.");
    }
    if (test_prime(answer)) {
        hint.push("Number is Prime.");
    }
    var range = Math.trunc(answer / 10);
    if (range === 0) {
        hint.push("Number lie between 1 10 9.");
    }
    else {
        hint.push("Number lie between " + (range * 10) + " to " + (range + 1) * 10);
    }
    if (answer % 3 === 0) {
        hint.push("Number is divisible by 3.");
    }
    if (answer % 5 === 0) {
        hint.push("Number is divisible by 5.");
    }
    var right = answer % 10;
    hint.push("Number is contain of "+right+" and "+range);
}


function play() {
    var user_guess = document.getElementById("guess").value;
    var guess = document.getElementById("guess");
    create_hints();
    if (user_guess < 1 || user_guess > 100) {
        alert("Please enter a number between 1 and 100.");
    }
    else {
        guessed_nums.push(user_guess);
        no_of_guesses += 1;
        msg3.style.display = "block";
        if (user_guess == answer) {
            guess.style.backgroundColor = "#63f563";
            guess.style.borderColor = "rgb(62 122 62)";
            msg1.textContent = "Yippie You Win!!";
            msg2.textContent = "The number was: " + answer;
            msg3.textContent = "You guessed it in " + no_of_guesses + " guesses";
            document.getElementById("my_btn").disabled = true;
        } else {

            if (user_guess < answer) {
                msg1.textContent = "Your guess is too low.";
                msg2.textContent = "No. of guesses: " + no_of_guesses;
                msg3.textContent = "Guessed numbers are: " +
                    guessed_nums;
            }
            else if (user_guess > answer) {
                msg1.textContent = "Your guess is too high.";
                msg2.textContent = "No. of guesses: " + no_of_guesses;
                msg3.textContent = "Guessed numbers are: " +
                    guessed_nums;
            }
        }
    }
}


function hide_funct() {
    var hide = document.getElementById("hintbox");
    if (hide.style.display === 'none') {
        if(index === hint.length){
            index = 0;
        }
        hide.textContent = hint[index];
        index = index+1;
        hide.style.display = "block";
    }
    else {
        hide.style.display = "none";
    }
    return;
}
