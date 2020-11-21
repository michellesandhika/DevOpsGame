import json
import classes.feature_class as fclass

import random


class Backend:
   def __init__(self):
      self.featureArray = []
      # this one store the index of the selected feature 
      self.featureSelected = []
      # to store the selected feature, for removing just remove the instance here
      self.selected = []
      self.featureDeployed = []
      # initial point 
      self.point = 10 
 
      #read from json and turn to feature class. taken idea from ideas.py
      f = open("json/feature_list.json")
      data = json.load(f)
      for i in data["features"]:
         a = fclass.feature(i)
         self.featureArray.append(a) 
         
   def returnFeatureClasses(self):
      return self.featureArray

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
   # this function maps the integer to the actual feature 
   def mapper(self, idx):
      return self.featureArray[idx]
   
   def process_mapping(self):
      for i, process in enumerate(self.featureSelected):
         self.featureSelected[i] = self.mapper(self.featureSelected[i])

   # Develop # 
   ###############################################################################################
   # the purpose of this stage is to show random errors and how to handle it in the middle of production

   
   def pick_errors(self):
      errorList = []
      for feature in self.featureSelected:
         for error in feature.error_messages:
            if random.uniform(0, 1) < error["possibility"]:
               errorList.append([feature, error])
               feature.fail_rate += error["fail_weight"] / 10
      return errorList

   
   def show_error(self):
      self.process_mapping()
      self.errorList = self.pick_errors()
            
   
   # apply the weights by the solution picked, return true if no more error need to select, false vice versa
   def solution_picked(self, selected_solution):
      current = self.errorList.pop(0)
      current[0].fail_rate = current[0].fail_rate - (current[1]["solution"][selected_solution]['weight']/10)
      if len(self.errorList) == 0:
         return True
      return False
      #self.featureSelected[self.pick_error()].fail_rate = self.featureSelected[self.pick_error()].error_messages["solution"][selected_solution]["weight"]


   # Testing #
   ###############################################################################################
   # the purpose of this stage is to give the players freedom to spend more time on specific features
   # but at the same time teaching them that the more time they put, the operating environment wont be that good
   # but the shorter you give time to the feature, the more bug it may appear.

   # this is the function to create the fail rate and stored in the class.
   # the higher the time, the more the chances of it failing and the higher the importance, the higher the fail_rate
   # both random int and time is 10 max, so the maximum is 10
   # failing rate is not always the same, sometimes its by chance
   
   def calculate_failrate (self):
      for feature in self.featureSelected:
         # modified it so that time affects harder on fail rate - nic
         feature.fail_rate = ((random.randint(0,10) * feature.time)/2 * feature.fail_rate)/10

   
   # dont need populate points, added points in the class - nic
   
   # increase the point on feature -nic
   def point_increase(self,feature):
      if self.point > 0:
         self.point -= 1 
         feature.points += 1
      
   # decrease the point on feature -nic
   def point_decrease(self,feature):
      if self.point < 10: 
         self.point += 1
         feature.points -= 1
         
   # return the point (budget) that we have left         
   def point_check(self):
      return self.point
            
    
            

   # Deployment #
   ################################################################################################
   # the purpose of this stage is to select which feature to actually deploy or not
   def new_failrate(self, feature): 
      # each point worth 5% flat reduction 
      feature.fail_rate = feature.fail_rate - feature.points * 0.05 
      
   def feature_deployed(self, selected_interger):
      if selected_interger in self.featureDeployed:
         self.featureSelected.remove(selected_interger)
      else:
         self.featureSelected.append(selected_interger)
         
   # if they decide to deploy, then remove the feature from the feature_list
   def remove_feature(self):
      self.featureArray = self.featureArray - self.featureDeployed

   # if they decided not to deploy, but then still want to keep the fail rate, so...


   # Production #
   ################################################################################################
   # bugs found 
   def deployment_failure(self, feature):
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

   def customer_feedback(self):
      pass
      

   # Also, there will be an overview of the devop metrics, and a graph if possible? of the progress of the changing devOps
   # dont forget to reset point list

   # After the game ends #
   #################################################################################################
