
from trafficSimulator import *
import numpy as np


class Intersection:
    def __init__(self):
        self.sim = Simulation()
        lane_space = 3.5
        intersection_size = 24
        island_width = 8 #increasing this will increase the gap between the lanes
        length = 100 #each square on the simulation is 10 so 100 means 10 squares in each direction


#---------------------------------------------------------------Variables----------------------------------------------------------------------------#
        self.vehicle_rate = 10
        self.v = 17
        self.speed_variance = 0
        self.self_driving_vehicle_proportion = 0 #number between 0 and 1, 0 means no self driving vehicles, 1 means entirely self driving vehicles
        if self.self_driving_vehicle_proportion == 1:
            self.v = self.v * 1.5
#----------------------------------------------------------------------------------------------------------------------------------------------------#
    #this section defines all the paths that a vehicle can take
    # SOUTH, EAST, NORTH, WEST 
    # create_segment((x1,y1),(x2,y2))
    # create_quadratic_beizer_curve(start, control, exit)
    # start is the entry, control guides the car along the curve

        #INNER, OUTER
        # Intersection in
            #paths 0-7
        self.sim.create_segment((lane_space/2 + island_width/2, length + intersection_size/2), (lane_space/2 + island_width/2, intersection_size/2)) 
        self.sim.create_segment((lane_space*3/2 + island_width/2, length+intersection_size/2), (lane_space*3/2+island_width/2, intersection_size/2)) 
        self.sim.create_segment((length + intersection_size/2, -lane_space/2 - island_width/2), (intersection_size/2, -lane_space/2 - island_width/2)) 
        self.sim.create_segment((length + intersection_size/2, -lane_space*3/2 - island_width/2), (intersection_size/2, - lane_space*3/2 - island_width/2)) 
        self.sim.create_segment((-lane_space/2 - island_width/2, -length - intersection_size/2), (-lane_space/2 - island_width/2, - intersection_size/2)) 
        self.sim.create_segment((-lane_space*3/2 - island_width/2, -length - intersection_size/2), (-lane_space*3/2 - island_width/2, -intersection_size/2)) 
        self.sim.create_segment((-length - intersection_size/2, lane_space/2 + island_width/2), (-intersection_size/2, lane_space/2 + island_width/2)) 
        self.sim.create_segment((-length - intersection_size/2, lane_space*3/2 + island_width/2), (-intersection_size/2, lane_space*3/2 + island_width/2))
        # Intersection out
            #paths 8-15
        self.sim.create_segment((-lane_space/2 - island_width/2, intersection_size/2), (-lane_space/2 - island_width/2, length + intersection_size/2))
        self.sim.create_segment((-lane_space*3/2 - island_width/2, intersection_size/2), (-lane_space*3/2 - island_width/2, length + intersection_size/2)) #9
        self.sim.create_segment((intersection_size/2, lane_space/2 + island_width/2), (length+intersection_size/2, lane_space/2 + island_width/2))
        self.sim.create_segment((intersection_size/2, lane_space*3/2 + island_width/2), (length+intersection_size/2, lane_space*3/2 + island_width/2)) #11
        self.sim.create_segment((lane_space/2 + island_width/2, -intersection_size/2), (lane_space/2 + island_width/2, -length - intersection_size/2))
        self.sim.create_segment((lane_space*3/2 + island_width/2, -intersection_size/2), (lane_space*3/2 + island_width/2, -length-intersection_size/2)) #13
        self.sim.create_segment((-intersection_size/2, -lane_space/2 - island_width/2), (-length-intersection_size/2, -lane_space/2 - island_width/2))
        self.sim.create_segment((-intersection_size/2, -lane_space*3/2 - island_width/2), (-length - intersection_size/2, -lane_space*3/2 - island_width/2)) #15

        # Straight
            #paths 16-23
        self.sim.create_segment((lane_space/2 + island_width/2, intersection_size/2), (lane_space/2 + island_width/2, -intersection_size/2))
        self.sim.create_segment((lane_space*3/2 + island_width/2, intersection_size/2), (lane_space*3/2 + island_width/2, -intersection_size/2))
        self.sim.create_segment((intersection_size/2, -lane_space/2 - island_width/2), (-intersection_size/2, -lane_space/2 - island_width/2))
        self.sim.create_segment((intersection_size/2, -lane_space*3/2 - island_width/2), (-intersection_size/2, -lane_space*3/2 - island_width/2))
        self.sim.create_segment((-lane_space/2 - island_width/2, -intersection_size/2), (-lane_space/2 - island_width/2, intersection_size/2))
        self.sim.create_segment((-lane_space*3/2 - island_width/2, -intersection_size/2), (-lane_space*3/2 - island_width/2, intersection_size/2))
        self.sim.create_segment((-intersection_size/2, lane_space/2 + island_width/2), (intersection_size/2, lane_space/2 + island_width/2))
        self.sim.create_segment((-intersection_size/2, lane_space*3/2 + island_width/2), (intersection_size/2, lane_space*3/2 + island_width/2))
    
    # SOUTH, EAST, NORTH, WEST
        #Right turn
            #paths 24-27 
        self.sim.create_quadratic_bezier_curve((lane_space*3/2 + island_width/2, intersection_size/2), (lane_space*3/2 + island_width/2, lane_space*3/2 + island_width/2), (intersection_size/2, lane_space*3/2 + island_width/2))
        self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space*3/2 - island_width/2), (lane_space*3/2 + island_width/2, -lane_space*3/2 - island_width/2), (lane_space*3/2 + island_width/2, -intersection_size/2))
        self.sim.create_quadratic_bezier_curve((-lane_space*3/2 - island_width/2, -intersection_size/2), (-lane_space*3/2 - island_width/2, -lane_space*3/2 - island_width/2), (-intersection_size/2, -lane_space*3/2 - island_width/2))
        self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space*3/2 + island_width/2), (-lane_space*3/2 - island_width/2, lane_space*3/2 + island_width/2), (-lane_space*3/2 - island_width/2, intersection_size/2))

        '''
        #Left turn - for no left turn lanes - original
            #paths 28-31
        self.sim.create_quadratic_bezier_curve((lane_space/2 + island_width/2, intersection_size/2), (lane_space/2 + island_width/2, -lane_space/2 - island_width/2), (-intersection_size/2, -lane_space/2 - island_width/2))
        self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space/2 - island_width/2), (-lane_space/2 - island_width/2, -lane_space/2 - island_width/2), (-lane_space/2 - island_width/2, intersection_size/2))
        self.sim.create_quadratic_bezier_curve((-lane_space/2 - island_width/2, -intersection_size/2), (-lane_space/2 - island_width/2, lane_space/2 + island_width/2), (intersection_size/2, lane_space/2 + island_width/2))
        self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space/2 + island_width/2), (lane_space/2 + island_width/2, lane_space/2 + island_width/2), (lane_space/2 + island_width/2, -intersection_size/2))
        '''

        #Dedicated Left-Turn Lanes (Paths 32-35) - added the 10 is an offset
        self.sim.create_segment((lane_space*5/2 + island_width/2 - 10 , length + intersection_size/2), (lane_space*5/2 + island_width/2 - 10, intersection_size/2))  #South Approach
        self.sim.create_segment((length + intersection_size/2, -lane_space*5/2 - island_width/2 +10), (intersection_size/2, -lane_space*5/2 - island_width/2 + 10))  #East Approach
        self.sim.create_segment((-lane_space*5/2 - island_width/2 +10, -length - intersection_size/2), (-lane_space*5/2 - island_width/2 +10, -intersection_size/2))  #North Approach
        self.sim.create_segment((-length - intersection_size/2, lane_space*5/2 + island_width/2 - 10), (-intersection_size/2, lane_space*5/2 + island_width/2 - 10))  #West Approach

        #these are the curves that the left turning cars take
        self.sim.create_quadratic_bezier_curve((lane_space*5/2 + island_width/2 - 10, intersection_size/2),(lane_space*5/2 + island_width/2 - 10, -lane_space/2 - island_width/2),(-intersection_size/2, -lane_space/2 - island_width/2))  #South to East
        self.sim.create_quadratic_bezier_curve((intersection_size/2, -lane_space*5/2 - island_width/2 + 10),(-lane_space/2 - island_width/2, -lane_space*5/2 - island_width/2 + 10),(-lane_space/2 - island_width/2, intersection_size/2))  #East to North
        self.sim.create_quadratic_bezier_curve((-lane_space*5/2 - island_width/2 + 10, -intersection_size/2),(-lane_space*5/2 - island_width/2 + 10, lane_space/2 + island_width/2),(intersection_size/2, lane_space/2 + island_width/2))  #North to West
        self.sim.create_quadratic_bezier_curve((-intersection_size/2, lane_space*5/2 + island_width/2 - 10),(lane_space/2 + island_width/2, lane_space*5/2 + island_width/2 - 10),(lane_space/2 + island_width/2, -intersection_size/2))  #West to South

        #Dedicated Right-Turn Lanes (36-39) - added same way the as the left turn lanes
        self.sim.create_segment((lane_space*5/2 + island_width/2  , length + intersection_size/2), (lane_space*5/2 + island_width/2 , intersection_size/2 + 10))  #South Approach
        self.sim.create_segment((length + intersection_size/2, -lane_space*5/2 - island_width/2 ), (intersection_size/2 + 10, -lane_space*5/2 - island_width/2 ))  #East Approach
        self.sim.create_segment((-lane_space*5/2 - island_width/2 , -length - intersection_size/2), (-lane_space*5/2 - island_width/2 , -intersection_size/2 -10))  #North Approach
        self.sim.create_segment((-length - intersection_size/2, lane_space*5/2 + island_width/2 ), (-intersection_size/2 - 10, lane_space*5/2 + island_width/2 ))  #West Approach

        #these are the curves the right turning cars take
        self.sim.create_quadratic_bezier_curve((lane_space*5/2 + island_width/2 , intersection_size/2 + 10),(lane_space*5/2 + island_width/2, lane_space*5/2),(lane_space*5/2 + island_width/2 +10, lane_space*5/2))
        self.sim.create_quadratic_bezier_curve((intersection_size/2 + 10, -lane_space*5/2 - island_width/2 ),(lane_space*5/2, -lane_space*5/2 - island_width/2),(lane_space*5/2, -lane_space*5/2 - island_width/2 - 10))
        self.sim.create_quadratic_bezier_curve((-lane_space*5/2 - island_width/2 , -intersection_size/2 -10),(-lane_space*5/2 - island_width/2, -lane_space*5/2),(-lane_space*5/2 - island_width/2 -10, -lane_space*5/2))
        self.sim.create_quadratic_bezier_curve((-intersection_size/2 - 10, lane_space*5/2 + island_width/2),(-lane_space*5/2, lane_space*5/2 + island_width/2),(-lane_space*5/2, lane_space*5/2 + island_width/2 +10))


        #dont worry about these (44-47)
        #they make it so that when the cars turn right they dont glitch back to the start of the road (make sure you have them in the right order tho)
        #the offsets took so long to figure out it actually made me mad

        self.sim.create_segment((-lane_space*3/2 - island_width/2, intersection_size/2 + 10), (-lane_space*3/2 - island_width/2, length + intersection_size/2 + 10)) #9 South
        self.sim.create_segment((intersection_size/2 + 10, lane_space*3/2 + island_width/2), (length+intersection_size/2 + 10, lane_space*3/2 + island_width/2)) #11 East
        self.sim.create_segment((lane_space*3/2 + island_width/2, -intersection_size/2 - 10), (lane_space*3/2 + island_width/2, -length-intersection_size/2 - 10)) #13 North 
        self.sim.create_segment((-intersection_size/2 - 10, -lane_space*3/2 - island_width/2), (-length - intersection_size/2 - 10, -lane_space*3/2 - island_width/2)) #15 West
        

        #all interfearing paths - original
    
        #left turn from the South intersects with the inner and outer straights coming from the North
        self.sim.define_interfearing_paths([0, 28], [4, 20],turn=True)
        self.sim.define_interfearing_paths([0, 28], [5, 21],turn=True)
        #left turn from the Rast intersects with the inner and outer straights coming from the Weat
        self.sim.define_interfearing_paths([2, 29], [6, 22],turn=True)
        self.sim.define_interfearing_paths([2, 29], [7, 23],turn=True)
        #left turn from the North intersects with the inner and outer straights coming from the south
        self.sim.define_interfearing_paths([4, 30], [0, 16],turn=True)
        self.sim.define_interfearing_paths([4, 30], [1, 17],turn=True)
        #left turn from the West intersects with the inner and outer straights coming from the East
        self.sim.define_interfearing_paths([6, 31], [2, 18],turn=True)
        self.sim.define_interfearing_paths([6, 31], [3, 19],turn=True)


        '''
        this section creates vehicle generators, we have two vehicle generators one; that creates regular vehicles (self.vg)
        and one that creates self-driving vehicles (self.sdvg)
        '''
        #regular vehicle generator
        self.vg = VehicleGenerator({
            #The first variable: 1 defines the weight if the vehicle; the higher the weight the more likely that type of vehicle will generate
            # 'path' defines the order of segments the vehicle will drive over
            #'v_max' defines the fastest speed a vehicle can drive at

            'vehicles': [ 
                #South [Inner Straight, Outer Straight, Right Turn, Left Turn] - change the left turn values to fix the path taken -4 on the value for the removed lanes
                (1, {'path': [0, 16, 12], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [1, 17, 13], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [36, 40, 45], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [28, 32, 14], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                #remember -4 for the removed lanes!!!!! [entry, path, exit]
                
                #East [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [2, 18, 14], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [3, 19, 15], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [37, 41, 46], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [29, 33, 8], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),

                #North [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [4, 20, 8], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [5, 21, 9], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [38, 42, 47], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [30, 34, 10], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
           
                #West [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [6, 22, 10], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [7, 23, 11], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [39, 43, 44], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                (1, {'path': [31, 35, 12], 'v_max': self.v+ 2*self.speed_variance*np.random.random() -self.speed_variance}),
                ], 'vehicle_rate' : self.vehicle_rate*(1-self.self_driving_vehicle_proportion) 
            })
        
        
        #self-driving vehicle generator
        self.sdvg = VehicleGenerator({
 
            #The first variable: 1 defines the weight if the vehicle; the higher the weight the more likely that type of vehicle will generate
            # 'path' defines the order of segments the vehicle will drive over
            #'v_max' defines the fastest speed a vehicle can drive at
            #'T' defines the raction time of the vehicle, the base is 1
            #'s0' defines the shortest distance a vehicle is able to drive behind another vehicle
            'vehicles': [
                #South [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [0, 16, 12], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [1, 17, 13], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [1, 24, 11], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [0, 28, 14], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),

                #East [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [2, 18, 14], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [3, 19, 15], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [3, 25, 13], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [2, 29, 8], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),

                #North [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [4, 20, 8], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [5, 21, 9], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [5, 26, 15], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [4, 30, 10], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
           
                #West [Inner Straight, Outer Straight, Right Turn, Left Turn]
                (1, {'path': [6, 22, 10], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [7, 23, 11], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [7, 27, 9], 'v_max': self.v, 'T' : 0.1,'s0' : 4}),
                (1, {'path': [6, 31, 12], 'v_max': self.v ,'T' : 0.1,'s0' : 4}),
                ], 'vehicle_rate' : self.vehicle_rate*self.self_driving_vehicle_proportion 
            })
        
        #adding both vehicle generators
        self.sim.add_vehicle_generator(self.vg)
        self.sim.add_vehicle_generator(self.sdvg)

    

        #adding the traffic signal
        self.sim.create_traffic_signal([self.sim.segments[0],self.sim.segments[1], self.sim.segments[4], self.sim.segments[5]],[self.sim.segments[2],self.sim.segments[3],self.sim.segments[6], self.sim.segments[7]])

    
    #this function returns an instance of the simulation defined above
    def get_sim(self):
        return self.sim