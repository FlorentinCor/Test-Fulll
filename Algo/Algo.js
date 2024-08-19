
a = 3
b = 5

for (let x = 1; x <= 100; x++) {
    if (x % (a * b) === 0) {
        console.log("FizzBuzz");
    } else if (x % a === 0) {
        console.log("Buzz");
    } else if (x % b === 0) {
        console.log("Fizz");
    } else {
    console.log(x);
    }
        
}