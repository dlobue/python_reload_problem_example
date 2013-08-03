

import imp


import builders


print("loading builder")


builder = imp.load_source("builders.builder", "builders/builder.py")
builder.run()

