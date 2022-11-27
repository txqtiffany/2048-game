# 2048-game

This is a game 2048 realized in pythonm which is in the form of a 4 * 4 grid(matrix).
Initially there would be 2 random cells with a number 2 in it, and the rest are empty. 
For each round, there will be a new random 2 inserted into the grid. 

Users can press w, s, a, d to move up, down, left, or right. 
When users press any key, the elements of the cell move in that direction such that if any two numbers are at the same row when you move horizontally,
or in the same column when you move vertically they get added up in that direction and fill itself with that number, the rest cells go empty again.

If no numbers are the same and next to each other with one move, all numbers will move to the same direction to fill all the space at that row/column.

If you reach 2048, you win the game, and can restart the game or end. 
If you cannot make further moves, end the game or restart the game. 
