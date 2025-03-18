import sys
import sysconfig
print(f"Python version: {sys.version}")
 
    # GIL Status
status = sysconfig.get_config_var("Py_GIL_DISABLED")
if status is None:
    print("GIL cannot be disabled")
if status == 0:
    print("GIL is active")
if status == 1:
        print("GIL is disabled")