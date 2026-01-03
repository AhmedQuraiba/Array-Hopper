# Array-Hopper
This is a test project I'm doing to learn git and github. It's a basic code about moving a letter in a 2D array.
This repository comes with two python files
<h1>Main.py</h1>
<p>This file is the one you're supposed to run to execute the program and be able to interact with the 2D Array.
It uses builtin python libraries "keyboard" and "time" to manage input and intervals between inputs, it also calls a third custom module called "utils" which is our second python file. 
The program first creates the 2d array of size 20*20, then enters the game loop and allows the user to endlessly move the character within it.</p>

<h1>Utils.py</h1>
<p>This works as a supporting module of the main one, and it contains two methods. First one is for showing the user options and to take input from them, this method is no longer used in the current version and has been replaced with functionalities of the keyboard library. Second one is for converting the 2d array into a screen-like representation by passing it into it as a parameter.</p>
