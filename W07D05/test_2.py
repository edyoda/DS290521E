# Way of Selecting or filtering out the test cases:
# 1) Running the test cases with substring matching approach

import pytest

def func(x):
	if x%2==0:
		return x+5
	else:
		return x-5

def test_case():
	assert func(3) == 8

def test_method_2():
	assert func(2) == 7

def test_case_2():
	assert func(4) == 12

# cmd: py.test -k test_case
# -k flag means we are picking test cases which are starting with
# test_case as the substring.