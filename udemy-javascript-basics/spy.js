// // For this project you will be building a generic website that will seem to ask mundane questions to normal users, but you secretly are looking for a spy! Anyone visiting your website will be asked a series of questions, only the Spy will be able to give specific answers you expect. If all questions are answered correctly, you will post a secret message in console for the Spy to read!
//
// Here are the four conditions you will check for the spy:
//
// The Spy has the same first letter of her First Name and Last Name
// The Spy is between the Age of 20 and 30 (exclusive of 20 and 30)
// The Spy is at least 170 centimeters tall.
// The Spy has a pet name that ends with the letter "y".

var firstname = prompt('Please enter your firstname');
var spyfirstchar = firstname[0];
var lastname =  prompt('Please enter your firstname');
var spylastfirstchar = lastname[0];
var age =  prompt('Please enter your age');
var height = prompt('Please enter your height');
var petName = prompt('Please enter your petname');
var petNameLastChar = petName[petName.length-1];
console.log(petNameLastChar);
if (spyfirstchar === spylastfirstchar && (age > 20 || age < 30) && height >= 170 && petNameLastChar === 'y' ) {
console.log("please find your secret code : XYZ");
}else{
  console.log("Hello normal");
}
