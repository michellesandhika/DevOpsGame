import json
import classes.feature_class as fclass
import classes.devOps_class as dclass

import random


class Backend:
   def __init__(self):
      self.featureArray = []
      self.customer_feedback = []
      # this one store the index of the selected feature 
      self.featureSelected = []
      # to store the selected feature, for removing just remove the instance here
      self.selected = []
      self.featureDeployed = []
      # initial point 
      self.point = 10 
      
      self.noFeatureDeployed = 0
      self.devopMetrics = dclass()
      self.currentMetrics = dclass()

 
      #read from json and turn to feature class. taken idea from ideas.py
      f = open("json/feature_list.json")
      data = json.load(f)
      for i in data["features"]:
         a = fclass.feature(i)
         self.featureArray.append(a)

      f = open("json/customer_feedback.json")
      data = json.load(f)
      for i in data: 
         self.customer_feedback.append(i)
         
         
   def returnFeatureClasses(self):
      return self.featureArray
   
   # Utility 
   # To remove multiple feature from list. remove is which array you want to remove
   def remove_multiple_features(self, key, remove): 
      idx = []
      print(key)
      for i in key: 
         for j in range (0, len(remove)): 
            if i.feature_name == remove[j].feature_name:
               idx.append(j)
      
      # Sort the collection of index so they dont collapse on each other 
      idx = sorted(idx, reverse = True)
      for i in idx: 
         remove.pop(i)
      
      
   # Idea page #
   #############################################################################################
   # the purpose of this stage is to select features to work on
   # the harder the feature, the better it is to release fast. 

   def process_selected(self, selected_interger):
      if selected_interger in self.featureSelected:
         self.featureSelected.remove(selected_interger)
      else:
         self.featureSelected.append(selected_interger)

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
   
   def add_leadtime(self):
      for feature in self.featureSelected:
         self.currentMetrics.leadTime = self.currentMetrics.leadTime + feature.lead_time
   
   def show_error(self):
      self.process_mapping()
      self.add_leadtime()
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
         #the more the feature is the more each will be likely to fail
         feature.fail_rate = feature.fail_rate + 1-(0.9/len(self.featureSelected))

         # if it is not on order, give penalty that it would be harder
         penalty = (self.noFeatureDeployed - feature.id)/10
         if penalty > 0:
            feature.fail_rate = penalty * feature.fail_rate
   
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
   # to remove the deployed feature from the featureSelected
   def remove_featureSelected(self):
      # a list of index of what to remove 
      idx = []
      self.remove_multiple_features(self.featureDeployed, self.featureSelected)
     
   def reset_points(self, feature):
      feature.points = 0
   
   def reset_all_points(self):
      self.point = 0
      for feature in featureSelected: 
         self.reset_points(feature)
   
   # Production #
   ################################################################################################
   # bugs found 
   def deployment_failure(self, feature):
      # the random is float for 1%-9% 
      fail = random.uniform(0,10) 
      # im assuming failure rate is always < 1
      if fail < feature.fail_rate * 100: 
         self.devopsMetrics.failedDeployment = self.devopsMetrics.failedDeployment + 1
         return True # the feature failed
      else: 
         return False 
   
   def deploy(self):
      deployed = []
      for i in self.featureDeployed:
         if not self.deployment_failure(i): 
            deployed.append(i)
      
      # remove the feature from the list 
      self.remove_multiple_features(deployed, self.featureDeployed)
      # remove it from the featureArray too
      self.remove_multiple_features(deployed, self.featureArray)
      # reduce the time for the failed feature in the featureDeployed
      for feature in self.featureDeployed: 
         feature.lead_time = feature.lead_time / 2
         
      # add the number of featuresDeployed
      self.noFeatureDeployed = self.noFeatureDeployed + len(deployed)
      
      # clear the selected array 
      self.featureSelected.clear()
      self.featureDeployed.clear()

   # After Everything else #
   ################################################################################################
   # After every production, there is going to be the customer feedback, this section is basically for this.
   # using the devOp metrics to decide.

   def customer_feedback(self):
      # if the current lead time is higher than ? point 


      # if 

   
   def add_total_metrics(self):
      self.devopMetrics.leadTime += self.currentMetrics.leadTime
      self.devopMetrics.failedDeployment += self.currentMetrics.failedDeployment
      self.devopMetrics.deploymentSize += self.currentMetrics.deploymentSize 

      self.devops.leadTime = 0 
      self.devopMetrics.failedDeployment = 0 
      self.devopMetrics.deploymentSize = 0
      
   def ending(self):
      self.round = self.round + 1

   # Also, there will be an overview of the devop metrics, and a graph if possible? of the progress of the changing devOps
   # dont forget to reset point list

   # After the game ends #
   #################################################################################################
   def calculate_score(self):
      score = 0
      #30% for lead time
      score = self.devopMetrics.leadTime
      #50% for deployment failure
      score = self.devopMetrics.failedDeployment
      #20% for average failed per deploy?