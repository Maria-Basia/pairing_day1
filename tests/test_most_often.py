from lib.most_often import *
#Create a test for add_new
def test_add_new():
    most_often = MostOften([1, 1, 1, 3, 3, 4, 5, 6, 6, 7])
    result = most_often.add_new(8)
    assert result == [1, 1, 1, 3, 3, 4, 5, 6, 6, 7, 8]


