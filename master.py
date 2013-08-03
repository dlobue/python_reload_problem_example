

import imp


import builders


print("loading builder v2")


builder = imp.load_source("builders.builder", "builders/builder.py")
builder.run()

