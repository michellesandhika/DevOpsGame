import json
import feature_class as fclass

import random

# HIIII NIC DALL AND DANIEL
# if you wanna know more, read the READMEPLS.txt :)))
class Backend:
   def __init__(self):
      self.feature_array = []
      self.featureSelected = []

      #read from json and turn to feature class. taken idea from ideas.py
      f = open("../feature_list.json")
      data = json.load(f)
      for i in data["features"]:
         a = fclass.feature(i)
         self.feature_array.append(a) 
         
   def returnFeatureClasses(self):
      return self.feature_array

# Idea page #
#############################################################################################
# the purpose of this stage is to select features to work on
# the harder the feature, the better it is to release fast. 


   def process_selected(self, selected_interger):
      if selected_interger in self.featureSelected:
         self.featureSelected.remove(selected_interger)
      else:
         self.featureSelected.append(selected_interger)

# also kinda need a function to map the integer with the actual feature
# need a function that changes the fail_rate to be higher or lower depending on the time it is chose to be developed.
   
'''
# Develop # 
###############################################################################################
# the purpose of this stage is to show random errors and how to handle it in the middle of production

#read data from the feature class for the error messages
#show error message, with random number generator?

index_featureError = random.randint(0,len(featureSelected)-1)
if random.randint(0,10) > 6:
   if random.randint(0,10) > 6:
      error_message(index_featureError, 0)
   else:
      error_message(index_featureError, 1)
   
# show error message. can take this function if you want to output which error message
def error_message(feature_index, index):
   return featureSelected[feature_index].error_messages[index]
   
# need a new structure in json where the error message have another level of options.
# also need a function that can state if they pick the right function then they will get less failing error

# Testing #
###############################################################################################
# the purpose of this stage is to give the players freedom to spend more time on specific features
# but at the same time teaching them that the more time they put, the operating environment wont be that good
# but the shorter you give time to the feature, the more bug it may appear.

# this is the function to create the fail rate and stored in the class.
# the higher the time, the more the chances of it failing and the higher the importance, the higher the fail_rate
# both random int and time is 10 max, so the maximum is 10
# failing rate is not always the same, sometimes its by chance
for feature in featureSelected:
   feature.fail_rate = ((random.randint(0,10) + feature.time)/2 * feature.fail_rate)/10

point_list = []
for i in range(0, len(featureSelected)):
   point_list.append(0)
   
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
   if sum(point_list) > 10:
      print("total should only be 10")
   allocate_points()
      
# this function is to allocate the points, so that if more time spent on it, the fail rate decrease
def allocate_points(feature_selected, point_list):
   for i in range(0,3):
      feature_selected[i].fail_rate = feature_selected[i].fail_rate * (10-point_list[i])*0.1
      

# Deployment #
################################################################################################
# the purpose of this stage is to select which feature to actually deploy or not

feature_deployed = []
def feature_deployed(selected_interger):
   if selected_interger in feature_deployed:
      featureSelected.remove(selected_interger)
   else:
      featureSelected.append(selected_interger)
      
# if they decide to deploy, then remove the feature from the feature_list
feature_array = feature_array - feature_deployed

# if they decided not to deploy, but then still want to keep the fail rate, so...


# Production #
################################################################################################
# bugs found 
def deployment_failure(feature):
    # the random is float for 1%-9% 
    fail = random.uniform(0,10) 
    # im assuming failure rate is always < 1
    if fail < feature.fail_rate * 100: 
        return True
    else: 
        return False 


# After Everything else #
################################################################################################
# After every production, there is going to be the customer feedback, this section is basically for this.
# using the devOp metrics to decide.

def customer_feedback():
   

# Also, there will be an overview of the devop metrics, and a graph if possible? of the progress of the changing devOps


# After the game ends #
#################################################################################################
'''