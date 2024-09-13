function greeting() {
    console.log("Selamat sore!");
 }
  
 greeting();
 
// Choosing Function Parameter

function greeting(greet) {
    console.log("Selamat " + greet + "!");
  }
   
  greeting('Malam');
  greeting('Sore');
  greeting('Siang');
  greeting('Pagi');

// Parameter also can be set in default

function greeting(greet, name = "Bapak/Ibu") {
    console.log("Selamat " + greet + ", " + name + "!");
  }
   
  greeting("sore", "Dimas");
  greeting("pagi");


