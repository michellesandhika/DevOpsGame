import feature_class

#where the feature classes is placed later
feature_selected = []
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
   allocate_points()
      
def allocate_points(feature_selected, point_list):
   for i in range(0,3):
      feature_selected[i].fail_rate = feature_selected[i].fail_rate * (10-point_list[i])*0.1
      
      
      