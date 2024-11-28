import turtle as t
import random
colors = ["red", "orange", "blue", "pink", "green"]

for i in range(100):
    steps = int(random.random() * 100)
    angle = int(random.random() * 360)
    t.color(random.choice(colors))
    t.right(angle)
    t.fd(steps)
# t.mainloop()