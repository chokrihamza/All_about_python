import importlib
import module_a
importlib.reload(module_a)

print(dir(module_a))
print(module_a.__name__)