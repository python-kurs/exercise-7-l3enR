# Exercise 5
from pathlib import Path
import numpy as np
import pandas as pd
import xarray as xr
from satpy import Scene, MultiScene
from pyresample.geometry import AreaDefinition
from glob import glob
from satpy.multiscene import timeseries

# import functions from utils here

data_dir = Path("data")
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

#load the data
data_mon1 = glob("./data/W_XX-EUMETSAT-Darmstadt,VIS+IR+HRV+IMAGERY,MSG3+SEVIRI_C_EUMG_*.nc")
data_mon2 = glob("./data/W_XX-EUMETSAT-Darmstadt,VIS+IR+HRV+IMAGERY,MSG4+SEVIRI_C_EUMG_*.nc")


#filter 12am
for i in data_mon1:
    if i[-9:-7] != "12":
        data_mon1.remove(i)
        
for i in data_mon2:
    if i[-9:-7] != "12":
        data_mon2.remove(i)

#load multiscene object
scenes_mon1 = [Scene(reader="seviri_l1b_nc", filenames=[f]) for f in data_mon1]
mscn_mon1 = MultiScene(scenes_mon1)

scenes_mon2 = [Scene(reader="seviri_l1b_nc", filenames=[f]) for f in data_mon2]
mscn_mon2 = MultiScene(scenes_mon2)

#show all available spectral bands
scenes_mon1[1].all_dataset_names()

#https://sentinel.esa.int/web/sentinel/technical-guides/sentinel-2-msi/level-1c/cloud-masks
#https://gisgeography.com/spectral-signature/

#load SWIR
mscn_mon1.load(["IR_134"])
mscn_mon2.load(["IR_134"])

#Area definition dem. rep kongo
area_def_kongo = AreaDefinition("Kongo",
                                "A Lambert Azimutal Equal Area projection of Kongo",
                                "Projection of Kongo", {"proj":"laea", "lat_0":2.5, "lon_0":6},
                                1000, 1000, (4E5, -17E5, 30E5, 8E5))


mscn1_kongo = mscn_mon1.resample(area_def_kongo)
mscn2_kongo = mscn_mon2.resample(area_def_kongo)

blended_scene1 = mscn1_kongo.blend()
blended_scene2 = mscn2_kongo.blend()

#blended_scene1["IR_134"].plot(x="x", y="y")
#blended_scene2["IR_134"].plot(x="x", y="y")

output_sc1 = output_dir / "month1_plot.png"
output_sc2 = output_dir / "month2_plot.png"

blended_scene1.show("IR_134").save(output_sc1)
blended_scene2.show("IR_134").save(output_sc2)
#add country borders

# 5. If you encounter any difficulties or have any other questions which you can't solve after first 
#    researching yourself don't hesitate to write us an email early so we can try to help you.

