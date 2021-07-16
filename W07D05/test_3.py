# Way of Selecting the test cases or filtering the test cases
# 2) Marking the test cases.

import pytest

def func(x):
	if x%2==0:
		return x+5
	else:
		return x-5

def test_case():
	assert func(3) == 8

@pytest.mark.mohit
def test_method_2():
	assert func(2) == 7

@pytest.mark.mohit
def test_case_2():
	assert func(4) == 12

# cmd: py.test -m mohit