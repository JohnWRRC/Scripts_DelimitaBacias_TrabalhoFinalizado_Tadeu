import grass.script as grass
from grass.script import raster as grassR
import os
import string
import glob
import re
import fnmatch

p=grass.mlist_grouped ('rast', pattern='(*)') ['PERMANENT']
for i in p:
    if "streams" in i:
        out=i+'_shp'
        out=out.replace("-",'_')
        grass.run_command('g.region',rast=i)
        grass.run_command('r.to.vect',input=i,out=out,feature='line',overwrite=True)