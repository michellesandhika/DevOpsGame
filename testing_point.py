import random
import feature_class

def failing_rate(feature):
   # the higher the time, the more the chances of it failing
   # the more the weighting, the more chances of it failing
   # both random int and time is 10 max, so the maximum is 
   # failing rate is not always the same, sometimes its by chance
   return ((random.randint(0,10) + feature.time)/2 * feature.fail_rate)/10

# the code for the testing page
point_list = [0,0,0]
def point_increase(point_index):
   if point_list[point_index] > 10:
      print("point too much")
   else:
      point_list[point_index] = point_list[point_index] + 1


def point_decrease(point_index):
   if point_list[point_index] < 0:
      print("point too little")
   else:
      point_list[point_index] = point_list[point_index] - 1
   
def point_check():
   if sum(point_list) != 10:
      print("total should only be 10")
      
      
      