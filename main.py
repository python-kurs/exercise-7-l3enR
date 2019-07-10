# Exercise 5
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
from satpy import Scene, MultiScene
from pyresample.geometry import AreaDefinition
# import functions from utils here

output_dir = Path("data")
output_dir = Path("solution")

#For this exercise you will need many of the things you learned during the course.
#It is an example of how you can use these tools to process a bigger satellite dataset
#consisting of multiple timeslots to find answers to your research questions.

#The question in this exercise is:
#Do the cloud cover frequencies in the Kongo differ through the seasons of the year?

#Normaly you would use a longer timeseries with all daytimes and month but due to restrictions to 
#hard disk space we prepared a dataset of two month of 12:00 MSG Seviri data slots for you.

# 1. Make a plan of the steps (in bullet points) and what you need for each of them to be able to answer the question above.
#    The steps should be driven by content, meaning what intermediate steps do you need 
#    and how can you achieve this step programmatically.

# 2. Commit the steps to the repository after the session into a new text file named steps.txt.

# 3. If any research is needed for any step do it until friday. Add the results of your research to
#    the steps.txt file (the information needed and the source of the information) and push it to the
#    remote repository.

# 4. Start programming.

# 5. If you encounter any difficulties or have any other questions which you can't solve after first 
#    researching yourself don't hesitate to write us an email early so we can try to help you.

