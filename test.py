from backend import Backend

if __name__ == "__main__":
    backend = Backend()
    backend.process_selected(1)
    backend.process_selected(2)
    backend.process_selected(3)

   
    backend.process_mapping()
    # print(backend.featureSelected)
    for i in backend.featureSelected:
        print(i.feature_name)
    print()
    feature1 = backend.featureSelected[0]
    feature2 = backend.featureSelected[1]
    backend.feature_deployed(feature1)
    backend.feature_deployed(feature2)
    for i in backend.featureDeployed:
        print(i.feature_name)
    print()
    backend.remove_feature()
    for i in backend.featureSelected:
        print(i.feature_name)