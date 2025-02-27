#This is the file that will start the simulation

#from base_intersection import *
#from intersection import *
#from example_intersection import *
from enhanced_intersection import *

#defining the intersection
intersection = Intersection()
#assigning the simulation
sim = intersection.get_sim()
#defining the window that displays the simulation
win = Window(sim)

#starts running the simulation then displays it
win.run()
win.show()