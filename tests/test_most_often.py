from lib.most_often import *
#Create a test for add_new
def test_add_new():
    most_often = MostOften([1, 1, 1, 3, 3, 4, 5, 6, 6, 7])
    most_often.add_new(3)
    result = most_often.get_most_often()
    assert result == "no clear winner"

def test_add_multiple():
    most_often = MostOften([1,1,2,2,3,3,3,4])
    most_often.add_new(4)
    most_often.add_new(4)
    most_often.add_new(4)
    result = most_often.get_most_often()
    assert result == 4

def test_minus():
    most_often = MostOften([-1,-1,1,2])
    result = most_often.get_most_often()
    assert result == -1

def test_zero():
    most_often = MostOften([0,0,0,1,2])
    result = most_often.get_most_often()
    assert result == 0

def test_empty():
    most_often = MostOften([])
    result = most_often.get_most_often()
    assert result == "no clear winner"