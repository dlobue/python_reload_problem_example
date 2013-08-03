

import imp
import sys


import builders


print("loading builder v3")

imp.reload(sys.modules["builders._common_config"])

builder = imp.load_source("builders.builder", "builders/builder.py")
builder.run()

