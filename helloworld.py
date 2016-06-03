#!/usr/bin/env python

import rpy2.robjects as robjects

print("Hello from Python")

# Source the R script into the R process
robjects.r.source("myscript.R")

# Get a reference to the 'add' function from the script we just sourced
addfn = robjects.r['add']

# Now, we can call it
result = addfn(1,2)

print("Result [Vec %d] = %d" % (len(result), result[0]))

print("Done.")

