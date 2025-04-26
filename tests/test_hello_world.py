from src.hello_world_lib import PrintWorld

def test_print():
    #pdb.set_trace()
    #raise Exception("Error")
    result = PrintWorld()
    assert result == "Hello!"
    
# def test_fail():
#     assert False  # This should always fail