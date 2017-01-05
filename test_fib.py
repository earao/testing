from fib import *

def test_zero():
	input = 0
	calculated_value = fib(input)
	expected_value = 1
	assert calculated_value == expected_value
	
def test_one():
	input = 1
	calculated_value = fib(input)
	expected_value = 1
	assert calculated_value == expected_value
	
def test_two():
	input = 2
	calculated_value = fib(input)
	expected_value = 1 + 1
	assert calculated_value == expected_value
	
def test_three():
	input = 3
	calculated_value = fib(input)
	expected_value = 1 + 2
	assert calculated_value == expected_value
	
def test_four():
	input = 4
	calculated_value = fib(input)
	expected_value = 2 + 3
	assert calculated_value == expected_value