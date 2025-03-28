# Escape! App Instructions

Python app designed to accompany the play "Escape!" by Sharon Rutland. This app is in no way connected to the author of the play, and is distributed under the MIT license.

## Requirements

The app was built on Windows using Python 3.12.4 and Pygame 2.6.1. A requirements.txt file is provided for completeness.

The app runs in full screen mode by default but you are, of course, free to adapt this to suit your needs.

## Main Screens

There are 4 main screens: Timer, Hints, Messages, and Flicker. These are activated by pressing T, H, M, or F respectively.

When the app is launched you will see the Timer screen and the clock will be stopped (more information below).

When you select the Hints or Messages screen it will initially display only the default background image. (This can be useful if you don't want any text on screen for a while!)

## Timer Screen (T)

Displays the remaining time on screen and counts down. If you need to alter the clock speed, to sync with the progress of the play, see "Clock Speed" below.

## Hint Screen (H)

When you select the Hint screen you will initially only see the office background picture. Press numbers 1-6 to display the corresponding hint. You can also cycle through the hints by pressing the left and right arrow keys (left moves back 1, right moves forward 1).

## Message Screen (M)

Operates in very much the same way as the Hint screen, except there are only 2 text messages: 1 = Steve's original message, 2 = Lisa's reply. It's less useful here, but you can use the left and right arrow keys here too.

## Flicker Screen (F)

The fourth screen is called the "Flicker" screen. The background will switch to a screen full of random grey squares, which constantly change, with a "Stand By" message displayed over the top.

This is useful for Act 2 when Karen says something like "there's something happening to the screen", just before the text messages appear.

## Clock Speed

You can make the timer run faster or slower use the + and - buttons. The slowest that time can run on screen is half normal speed, i.e. 1 second on screen is 2 seconds in real time. The fastest is twice normal speed. This should help you to synchronise the timer with the play.

Press \* to reset passage of time to normal.

Alternatively, when on the Timer screen, you can also use the left and right arrows to slow down or speed up the clock. The up and down arrows both reset clock speed to normal.

## Change Remaining Time

To change the remaining time left on the timer, press C followed by the number of minutes you want and finally ENTER. Decimals are allowed. For example typing C25.5 followed by ENTER will change the time remaining to 25 minutes 30 seconds.

To cancel this, without changing the time, simply press C again.

This only accepts values between 0 and 60 minutes. Numbers outside this range are ignored. Entries that are not valid numbers are also ignored.

## Start or Stop the Timer

Press the S key to start or stop (pause) the timer.

When the app launches, the timer will show 60 minutes and it will not be running. Press S to start it, then S again to stop it when needed. Upon restarting, it will carry on from where it was stopped. And so on.

## Panic Button

The space bar can be used as a panic button! If you're ever stuck just press the space bar and you will jump straight back to the Timer screen. It doesn't matter what you were doing at the time, this will just get you back to safety!

## Game Over

When the timer reaches zero the message "GAME OVER!" will be displayed.

## Quit the App

If you need to quit the app, either click the X button to close the window or press Escape several times in quick succession.
