import random



def mock_process(img):
	mock_dic = {
	    "car_type_small": None,
        "car_type_middle": None,
        "car_type_large": None,
        "car_total_num": None
	}
	car_type_small = random.randint(0,20)
	car_type_middle = random.randint(0,10)
	car_type_large = random.randint(0,8)
	car_total_num = car_type_small + car_type_middle + car_type_large

	mock_dic['car_type_small'] = car_type_small
	mock_dic['car_type_middle'] = car_type_middle
	mock_dic['car_type_large'] = car_type_large
	mock_dic['car_total_num'] = car_total_num
	
	return mock_dic