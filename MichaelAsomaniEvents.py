# Author - Michael Asomani        Date - 12/2/21
# Purpose - Design a paddle ball game with GUI animation and events

import random
from tkinter import *
class BallGame:
    def __init__(self):
        my_window = Tk() # create a window
        my_window.title("Ball Game")
        my_width = 400
        my_height = 200
        self.my_canvas = Canvas(my_window, bg = 'white', \
                           width = my_width, height = my_height)
        self.my_canvas.pack()
        ballRadius = 20
        goalRadius = 20
        ballX = ballRadius 
        ballY = ballRadius
        goalX = goalRadius 
        goalY = goalRadius 

        self.my_canvas.create_oval(goalX - goalRadius, my_height/2 + goalRadius,\
                              goalX + goalRadius, my_height/2 - goalRadius,\
                                  fill = "black", tags = "goal")
            
        self.my_canvas.create_oval(ballX - ballRadius, ballY + ballRadius,\
                              ballX + ballRadius, ballY - ballRadius,\
                                  fill = "red", tags = "disk")
        
        self.paddleTop = 50
        self.paddleBottom = 100
        self.my_canvas.create_rectangle(380, self.paddleTop, 390, self.paddleBottom, \
                                   fill = "black", tags = "paddle")
        
        self.my_canvas.bind("<Key>", self.processKeyEvent)
        self.my_canvas.focus_set() # give the canvas the focus at start-up
        # to receive input from the keyboard
        
        dx = 2 # horizontal of disk
        dy = 2 # vertial of disk
        while True :  # move to new x and update x-position
            self.my_canvas.move("disk", dx, dy) # move disk dx amount
            self.my_canvas.after(5) # sleep for a few millisecs
            # redraw/update the canvas w/ new disk position
            self.my_canvas.update()
            
            r1 = random.randint(-1, 1)
            ballX += dx
            ballY += dy
            if ballX + ballRadius > my_width: # hit right boundary
                dx = -dx + r1
            elif ballX - ballRadius <= 0: # hit left boundary
                dx = -dx + r1
            elif ballY + ballRadius > my_height: # hit bottom boundary
                dy = -dy + r1
            elif ballY - ballRadius <= 0: # hit top boundary
                dy = -dy + r1
            elif ballX + ballRadius > 380:
                if ballY + ballRadius >= self.paddleTop and ballY - ballRadius <= self.paddleBottom: # uses paddle to hit ball
                        dx = -dx + r1
            
            elif (ballX - ballRadius) >= (goalX - goalRadius) and (ballX + ballRadius) <= (goalX + goalRadius): 
                print("HIT")
                self.my_canvas.delete("disk")
                if (ballY + ballRadius) >= (my_height/2 + goalRadius) and (ballY - ballRadius) <= (my_height/2 - goalRadius):
                    print("BINGO")
                    self.my_canvas.delete("disk")
        my_window.mainloop()
    def processKeyEvent(self, event):
        self.my_canvas.delete("paddle")
        if event.keycode == 40:
            self.paddleTop = self.paddleTop + 10
            self.paddleBottom = self.paddleBottom + 10
            self.my_canvas.create_rectangle(380, self.paddleTop, 390, self.paddleBottom, \
                                       fill = "black", tags = "paddle")
        elif event.keycode == 38:
            self.paddleTop = self.paddleTop - 10
            self.paddleBottom = self.paddleBottom - 10
            self.my_canvas.create_rectangle(380, self.paddleTop, 390, self.paddleBottom, \
                                       fill = "black", tags = "paddle")
        else:
            self.my_canvas.create_rectangle(380, self.paddleTop, 390, self.paddleBottom, \
                                       fill = "black", tags = "paddle")
         
        
BallGame()