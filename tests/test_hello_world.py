import pdb
import subprocess
import os
from src.hello_world import PrintWorld

def test_print():
    #pdb.set_trace()
    #raise Exception("Error") 
    # result = PrintWorld()
    # print("main() returned: {result}")
    binary_path = os.path.join(os.environ["RUNFILES_DIR"], "src/hello_world")
    result = subprocess.run(binary_path, capture_output=True, text=True)
    print(f"DEBUG: Binary output -> {result.stdout.strip()}")  # Debugging
    assert result.stdout.strip() == "Hello!"


# def test_fail():
#     assert False  # This should always fail