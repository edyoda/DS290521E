# fixtures: They are used to have something pre run before the test case
# so that we can use it inside test cases.

import pytest

@pytest.fixture
def pre_data():
	data = {'python':3,'django':2,'numpy':1}
	return data
# pre_data is considered as data now.

def test_case_1(pre_data):
	python = 3
	assert pre_data['python'] == python

def test_case_2(pre_data):
	django = 1
	assert pre_data['django'] == django