import module

values = [1,2854,2854,2854,2854, 3376 ,4569, 4569]

value = 4569

lowerOne = module.find_nearest_values(target_list = values, target_value = value)[0]
upperOne = module.find_nearest_values(target_list = values, target_value = value)[1]

print(lowerOne, upperOne)
