// PART 4 ARRAY EXERCISE
// This is  a .js file with commented hints, its optional to use this.

// Create Empty Student Roster Array
// This has been done for you!
var roster = []


// Create the functions for the tasks

// ADD A NEW STUDENT

// Create a function called addNew that takes in a name
// and uses .push to add a new student to the array
function addnew(name) {
  return roster.push(name);
}

// REMOVE STUDENT
function remove(name){
  const index = roster.indexOf(name);
  if (index > -1) {
    roster.splice(index, 1);
  }
}

// Create a function called remove that takes in a name
// Finds its index location, then removes that name from the roster

// HINT: http://stackoverflow.com/questions/5767325/how-to-remove-a-particular-element-from-an-array-in-javascript
//

// DISPLAY ROSTER

// Create a function called display that prints out the orster to the console.
function display(){
  console.log(roster);
}

// Start by asking if they want to use the web app

// Now create a while loop that keeps asking for an action (add,remove, display or quit)
// Use if and else if statements to execute the correct function for each command.
var quit = true;
while(quit){
  expression = prompt('(add,remove, display or quit)');
  switch (expression) {
    case 'add':
      var add =  prompt('enter name to add');
      addnew(add);
      break;
    case 'remove':
      var name =  prompt('enter name to remove');
      remove(name);
      break;
    case 'display':
      display();
      break;
    case 'quit':
    alert('Thansk for using the roster');
      quit = false;
      break;
    default:
    quit = false;
  }
}
