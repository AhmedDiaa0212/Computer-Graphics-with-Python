from graphics import *

def moveAll(shapeList, dx, dy):
    """Function for Move all shapes in shapeList by (dx, dy)"""
    for shape in shapeList: 
        shape.move(dx, dy)
            

def moveAllOnLine(shapeList, dx, dy, repetitions, delay):
    """Animate the shapes in shapeList along a line.
      Repeat the specified number of repetitions and have the specified delay after each repeat."""
    for i in range(repetitions):
        moveAll(shapeList, dx, dy)
        time.sleep(delay)

def main():
  """The main function that contains the shapes  """
  win = GraphWin("Wow emoji", 700, 500)
  win.setBackground("white") 

  #Head
  head = Circle(Point(250,250),100)
  head.setFill(color_rgb(255, 203, 76))
  head.setWidth(3)
  head.draw(win)

  #Left eye
  eye1 = Circle(Point(300,223),20)
  eye1.setFill("white")
  eye1.draw(win)

  bl1 = Circle(Point(301,222),12)
  bl1.setFill("blue")
  bl1.draw(win)

  b1 = Circle(Point(301,222),8)
  b1.setFill("black")
  b1.draw(win)

  #left eyebrow
  br1 = Circle(Point(300,184),12)
  br1.setWidth(4) 
  br1.draw(win)

  d1 = Circle(Point(300,186),12)
  d1.setWidth(4)
  d1.setFill(color_rgb(255, 203, 76)) 
  d1.setOutline(color_rgb(255, 203, 76)) 
  d1.draw(win)

  #Right eye
  eye2 = Circle(Point(196,226),20)
  eye2.setFill("white")
  eye2.draw(win)
  
  bl2 = Circle(Point(196,227),12)
  bl2.setFill("blue")
  bl2.draw(win)
  
  b2 = Circle(Point(196,227),8)
  b2.setFill("black")
  b2.draw(win) 

  #Right eyebrow
  br2= Circle(Point(192,191),12)
  br2.setWidth(4) 
  br2.draw(win)

  d2 = Circle(Point(192,193),12)
  d2.setWidth(4)
  d2.setFill(color_rgb(255, 203, 76)) 
  d2.setOutline(color_rgb(255, 203, 76)) 
  d2.draw(win)

  #mouth 
  mouth = Oval(Point(263, 315),Point(233, 280))
  mouth.setFill("black")
  mouth.draw(win)

  #text note  
  Note= Text(Point(win.getWidth()/2, 50), 'By:Ahmed Diaa - CS \r Click anywhere to quit. ')
  Note.draw(win)

  #shapeList
  faceList = [head, eye1 , b1, bl1, br1 , d1 , eye2, b2 , bl2 ,br2,d2,mouth  ]

  #methods call
  moveAllOnLine(faceList, 7.5, 0, 46, .08)
  moveAllOnLine(faceList, -10.5, 0, 46, .08)

  #pause for click in window
  win.getMouse()
  win.close()

if __name__ == '__main__':
  main()