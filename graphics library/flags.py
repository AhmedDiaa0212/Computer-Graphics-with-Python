from graphics import *

def main():
      """The main function that contains the flags  """
      win = GraphWin("Flags", 600, 500)
      win.setBackground("white") 

      #The upper "red rectangle"
      rec1=Rectangle(Point(106,43),Point(499,99))
      rec1.setFill("red")

      #The middle "white rectangle"
      rec2=Rectangle(Point(106,99),Point(499,157))
      rec2.setFill("white")

      #The lower "black rectangle"
      rec3=Rectangle(Point(106,155),Point(499,217))
      rec3.setFill("black")

      #The Syria's two stars

      #Right star
      starl=Polygon(Point(233,109),Point(228,124),Point(212,124),
      Point(225,134),Point(220,148),Point(233,138),Point(247,148),
      Point(242,134),Point(255,124),Point(238,124))
      starl.setFill("green")

      #Left star
      star2=Polygon(Point(352,109),Point(347,124),Point(331,124),
      Point(344,134),Point(339,148),Point(352,138),Point(364,148),
      Point(361,134),Point(374,124),Point(358,124))
      star2.setFill("green")

      #Allahu Akbar word inside the flag of Iraq
      allahu_Akbar= Text(Point(298, 131), 'الله  أكبر')
      allahu_Akbar.setSize(27)
      allahu_Akbar.setTextColor("green")
      allahu_Akbar.setStyle("bold")

      #Text note  
      Note= Text(Point(296, 270), " Please enter the name of the flag you want to display : \r     ( iraq - syria - yemen )\
      \r Click anywhere to quit. \r By:Ahmed Diaa - CS ")
      Note.setSize(15)
      Note.setStyle("bold")
      Note.draw(win)

      #flag name input
      input = Entry(Point(290, 335),20)
      input.setSize(12)
      input.setStyle("bold italic")
      input.setTextColor("red")
      input.draw(win)

      win.getMouse()

      x=input.getText()

      if x == "iraq":
            rec1.draw(win)
            rec2.draw(win)
            rec3.draw(win)
            allahu_Akbar.draw(win)

      elif x == "syria":
            rec1.draw(win)
            rec2.draw(win)
            rec3.draw(win) 
            starl.draw(win)  
            star2.draw(win)

      elif x == "yemen":
            rec1.draw(win)
            rec2.draw(win)
            rec3.draw(win) 

      win.getMouse()
      win.close()

if __name__ == '__main__':
      main()