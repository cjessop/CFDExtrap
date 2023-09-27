from Framework import *

# Create a new framework instance
fw = CFD_Extrapolation()
fw.finite_diff([1.0, 1.2, 1.4, 1.6, 1.8, 2.0], 1.5)