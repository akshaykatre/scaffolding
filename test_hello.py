from hello import add, subtract

def test_add():
    assert add(10, 10) == 20
    
def test_sub():
    assert subtract(2,1) == 1 
    