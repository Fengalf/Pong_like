# My take on PONG

This is my attempt on recreating the pong game. This readme file also is going to be SOMEWHAT of a documentation.

## Dissect the problem

At the very beginning it's imperative to think on how to build the game. For that, it needs to be broken down into smaller bits.
In my opinion for `Pong` to be built these bits are:

* Player paddles
  * A paddle for the left side
  * A paddle for the right side
  * Edit: Make the paddles move
  
* Scoreboard
  * A score text on the left side
  * A score text on the right side
  * A center line
  * Count up a point for the opposing side if
    * Left wall was hit
    * Right wall was hit

* Pong ball
  * Make it bounce of the upper and lower wall
  * Make it bounce of the paddles
  * Calculate the angle when bounce of
    * A paddle
    * A wall

## Programming journey

While at first I had a good idea of what to do and dissecting and noting down the task(-s) at hand,
I learned that the movement could be done by simply setting the X and Y cords. This opens for an easier bouncing mechanic.
At first I was going to change the rotation angle every time the ball hits something where it can bounce off,
then I found the math is way easier to do with the other method.
Additionally a learning was that, while inheriting a class is nice, sometimes a class may still needs to be called in order to get expected results. (For example the scoreboard.)
In general I learned how to pass parameters into classes.

## Future ideas

* Add player modes
  * Add single player mode
    * Add a mode where the computer is controlling one of the paddles.
  * Add 4 player mode
    * This game could be changed to have a 4 player mode (which certainly would need a second keyboard or better gamepads)
* Difficulty game modes
  * 2 game modes could be implemented:
    * Timebased ball and paddle speed increase
      * If the game has been going on for 3 minutes or more the ball may increase speed
    * Pointbased ball and paddle speed increase
      * If the sum of points is higher than 10, the ball may increase speed
* Play again option
  * Prompt the user to hit the Y/y or N/n if they want to replay after the game is done
