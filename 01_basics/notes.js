//! Q1 . What is modules in python?
// Python me module ek file hoti hai jisme functions, variables aur classes likhe hote hain, jinko hum dusre programs me reuse kar sakte hain.
//? example :
//todo:  Create a file called mymodule.py
// def add(a, b):
// return a + b

//todo:  Now use it in another file:
// import mymodule
// print(mymodule.add(2, 3))

//! Q2. What is packages in python?
// Python me package ek folder hota hai jisme multiple Python files (modules) hote hain aur ek special file hoti hai __init__.py.
// Ye large projects ko proper structure dene me help karta hai.

//? Folder Structure:
// myproject/
//  └── mathutils/
//      ├── __init__.py
//      ├── add.py //? modules
//      └── subtract.py //? modules

//* mathutils folder ko hai vo package hoga because vo special file contain kar raha hai and multiple python files(modules) bhi contain kar raha hai.

//! Q3. What is virtual environment in python?
// Python me virtual environment ek isolated (alag) environment hota hai, jisme hum kisi project ke packages alag se install kar sakte hain, bina system ke global Python ko affect kiye.

// Agar virtual environment na ho, to sab projects same global packages use karenge, jisse version conflict ho sakta hai.

//* How to Create a Virtual Environment
// Step 1 – Create(terminal me below command run karo)
// python -m venv myenv

// Step-2 Activate karna (terminal me below command run karo)
// myenv\Scripts\activate

// Step 3 – Install Packages (terminal me below command run karo)
// pip install flask

// Step 4 – Deactivate
// deactivate

//! Important baat inside the python ecosystem always work in virtual environment (venv)

//? venv is a traditional way to ship and organize the code.
