"""
This file is to test the mean function
"""


from molssidevops import mean
import pytest


def test_simple():
    num_list = [1, 2]
    observed = mean(num_list)
    expected = 1.5
    assert observed == expected, 'My test failed'


@pytest.fixture
def num_list():
    return [1,2,3,4,5]


#@pytest.mark.skip('Example of skipping a test')
def test_more(num_list):
    assert mean(num_list) == 3.0


def test_empty():
    with pytest.raises(ZeroDivisionError):
        mean([])


def test_type_error():
    with pytest.raises(TypeError):
        mean(['a','b','c','d'])


@pytest.mark.parametrize("num_list, expected_mean", [
    ([1,2,3,4,5],3.0),
    ([1,2],1.5),
    ([5],5),
])
def test_many(num_list, expected_mean):
    assert mean(num_list) == expected_mean





    
