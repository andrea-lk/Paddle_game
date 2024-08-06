# Breakout Game

This project is an implementation of the classic Breakout game using the `graphics` module for creating the canvas and handling animations.

## Table of Contents
- [Project Description](#project-description)
- [Features](#features)

## Project Description

The Breakout game involves a ball bouncing around the screen, breaking bricks by colliding with them, and being kept in play by a movable paddle controlled by the player. The objective is to break all the bricks without letting the ball fall off the bottom of the screen. The game includes features like multiple rows and columns of bricks, a paddle that follows the mouse, and a bouncing ball with variable velocity.

## Features
- **Brick Setup**: Creates a grid of colored bricks.
- **Bouncing Ball**: A ball that moves and bounces off walls, the paddle, and bricks.
- **Paddle Movement**: Paddle controlled by the mouse to keep the ball in play.
- **Collision Detection**: Detects and handles collisions between the ball, bricks, and paddle.
- **Game Over Conditions**: Tracks the number of turns and ends the game if the player loses all turns or breaks all bricks.
