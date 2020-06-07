//One way of selecting event and solving the problem
// var headOne = document.querySelector('#one');
// var headTwo = document.querySelector('#two');
// var headThree = document.querySelector('#three');
// var headfour = document.querySelector('#four');
// var headfive = document.querySelector('#five');
// var headsix = document.querySelector('#six');
// var headseven = document.querySelector('#seven');
// var headeight = document.querySelector('#eight');
// var headnine = document.querySelector('#nine');

// alert("select")
// headOne.addEventListener("click",function(){
//   headOne.textContent = 'X';
//   headOne.style.color = 'blue';
// })
//
// // Double Click
// headOne.addEventListener("dblclick",function(){
//   headOne.textContent = 'O';
//   headOne.style.color = 'red';
// })

//button
var restart = document.querySelector("#restart");

//Select all the squares
var squares = document.querySelectorAll('td');

function clearBoard() {
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}

function game() {
  if(this.textContent === ''){
    this.textContent = 'X';
  }  else if(this.textContent === 'X'){
    this.textContent = 'O';
  }else {
    this.textContent = '';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click',game);
}

//Restart button
restart.addEventListener('click',clearBoard);
