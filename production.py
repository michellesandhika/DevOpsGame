import feature_list
import random 

def failure(feature):
    # the random is float for 1%-9% 
    fail = random.uniform(0,10) 
    # im assuming failure rate is always < 1
    if fail < feature.fail_rate * 100: 
        return True
    else: 
        return False 
