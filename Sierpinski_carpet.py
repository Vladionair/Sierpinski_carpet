from tkinter import *
import random
root = Tk()
c = Canvas(root, width=600, height=600, bg='white')
c.pack()
x = 0
y = 0
for i in range(100000):
  coord = random.choice([(100, 100), (300, 100), (500, 100), (100, 300), 
                         (500, 300), (100, 500), (300, 500), (500, 500)])
  x = (x + 2*coord[0])/3
  y = (y + 2*coord[1])/3
  point = c.create_line(x, y, x + 1, y, fill='black')
root.mainloop()