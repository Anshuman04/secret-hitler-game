import pdb
import subprocess
import os
from src.hello_world import PrintWorld

def test_print():
    #pdb.set_trace()
    #raise Exception("Error") 
    result = PrintWorld()
    assert result == "World Hello!"


# def test_fail():
#     assert False  # This should always fail