from hello import add

def setup_function(function):
    print(f" Running Setup: {function.__name__}")
    function.x = 10
    function.y = 5

def teardown_function(function):
    print(f" Running Teardown: {function.__name__}")
    del function.x
    del function.y

def test_add():
    assert add(test_add.x, test_add.y) == 15