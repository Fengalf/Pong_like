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
