import feature_class as fclass
import json

def feature_reader(feature_array):
    
    with open('json/feature_list.json') as json_file:
        data = json.load(json_file)
        for i in data["features"]:
            a = fclass.feature(i)
            feature_array.append(a) 

    return feature_array



# Below is how you use feature_reader 
# feature_array = []
# feature_reader(feature_array)
# for i in range(0, len(feature_array)):
#    feature_array[i].print_details()