from sinc2d import *

def test_xzero():
	x = 0
	y = 90
	calculated_value = sinc2d(x,y)
	expected_value = np.sin(y) / y
	assert calculated_value == expected_value
	
def test_yzero():
	x = 90
	y = 0
	calculated_value = sinc2d(x,y)
	expected_value = np.sin(x) / x
	assert calculated_value == expected_value
	
def test_xyzero():
	x = 0
	y = 0
	calculated_value = sinc2d(x,y)
	expected_value = 1
	assert calculated_value == expected_value

def test_xy():
	x = 90
	y = 90
	calculated_value = sinc2d(x,y)
	expected_value =(np.sin(x) / x) * (np.sin(y) / y)
	assert calculated_value == expected_value
