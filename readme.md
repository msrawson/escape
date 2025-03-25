# Escape! App Instructions

Python app designed to accompany the play "Escape!" by Sharon Rutland. This app is in no way connected to the author of the play, and is distributed under the MIT license.

## Requirements

The app was built on Windows using Python 3.12.4 and Pygame 2.6.1. A requirements.txt file is provided for completeness.

The app runs in full screen mode by default but you are, of course, free to adapt this to suit your needs.

## Main Screens

There are 3 main screens: Timer, Hints, Messages. These are activated by pressing T, H, or M, respectively.

When the app is launched you will see the Timer screen and the clock will be stopped (more information below).

When you select the Hints or Messages screen it will initially display only the default background image. (This can be useful if you don't want any text on screen for a while!) Press a number key to display the desired hint or message. Hints are numbered 1-6 and messages 1-2.

## Clock Speed

You can make the timer run faster or slower use the + and - buttons. The slowest that time can run on screen is half normal speed, i.e. 1 second on screen is 2 seconds in real time. The fastest is twice normal speed. This should help you to synchronise the timer with the play.

Press \* to reset passage of time to normal.

## Change Remaining Time

To change the remaining time left on the timer, press C followed by the number of minutes you want and finally ENTER. Decimals are allowed. For example typing C25.5 followed by ENTER will change the time remaining to 25 minutes 30 seconds.

To cancel this, without changing the time, simply press C again.

This only accepts values between 0 and 60 minutes. Numbers outside this range are ignored. Entries that are not valid numbers are also ignored.

## Start or Stop the Timer

Press the S key to start or stop (pause) the timer.

When the app launches, the timer will show 60 minutes and it will not be running. Press S to start it, then S again to stop it when needed. Upon restarting, it will carry on from where it was stopped. And so on.

## Game Over

When the timer reaches zero the message "GAME OVER!" will be displayed.

## Quit the App

If you need to quit the app, either click the X button to close the window or press Escape several times in quick succession.
