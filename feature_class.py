 
class feature:
   def __init__(self, feature_detail):
      super().__init__()
      self.id = feature_detail["id"]
      self.feature_name = feature_detail["feature_name"]
      self.lead_time = feature_detail["time"]
      self.fail_rate = feature_detail["fail_rate"]
      self.error_messages = feature_detail["error_messages"]
      
   def modify_failrate(self, point):
      self.fail_rate = self.fail_rate + point

   def print_details(self):
      print("id:", self.id)
      print("feature name:", self.feature_name)
      print("time:", self.lead_time)
      print("fail rate:", self.fail_rate)
      print("error:", self.error_messages)


