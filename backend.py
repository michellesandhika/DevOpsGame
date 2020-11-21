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

   # pick which error to show
   # loop through the different features and see which one has the highest fail rate
   # returns the index of the failMax in featureSelected
   def pick_error(self):
      failMax_idx = 0
      for i in range (1, len(self.featureSelected)):
        
         if self.featureSelected[i].error_messages["fail_weight"] > self.featureSelected[failMax_idx].error_messages["fail_weight"]:
            failMax_idx = i
      return failMax_idx
          
   # with the error picked, find out whether there is the possibility of it coming through
   # if it comes through then +point on the fail rate of that feature
   # returns none if there is no bug
   def show_error(self):
      self.process_mapping()
      feature_forError = self.featureSelected[self.pick_error()]
      error_selected = feature_forError.error_messages
      
      error_chance = (error_selected["fail_weight"] + random.randint(2, 10))/2
      if error_chance > 5:
         feature_forError.fail_rate = feature_forError.fail_rate + (error_chance/10)
         return error_selected
      else:
         return None
   
   # to get the message error use show_error().messgage, and the solution with show_error().solution
      
   # from the error, which solution can decrease the fail rate?
   # selected_solution is the input from the option
   def solution_picked(self, selected_solution):
      #featureSelected[pick_error()].fail_rate = featureSelected[pick_error()].fail_rate - (featureSelected[pick_error()].fail_weight/10)
      self.featureSelected[self.pick_error()].fail_rate = self.featureSelected[self.pick_error()].error_messages["solution"][selected_solution]["weight"]


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
            
    
   def new_failrate(self, feature): 
      # each point worth 5% flat reduction 
      feature.fail_rate = feature.fail_rate - feature.points * 0.05      

   # Deployment #
   ################################################################################################
   # the purpose of this stage is to select which feature to actually deploy or not
   def feature_deployed(self, feature):
      if feature in self.featureDeployed:
         self.featureDeployed.remove(feature)
      else:
         self.featureDeployed.append(feature)
               
   # if they decide to deploy, then remove the feature from the feature_list
   def remove_feature(self):
      # a list of index of what to remove 
      idx = []
      for i in self.featureDeployed:
         for j in range (0, len(self.featureSelected)):
            if i.feature_name == self.featureSelected[j].feature_name:
               idx.append(j)
               
      # Sort the collection of index so they dont collapse on each other 
      idx = sorted(idx, reverse = True)
      for i in idx: 
         self.featureSelected.pop(i)
      # self.featureArray = self.featureArray - self.featureDeployed

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
