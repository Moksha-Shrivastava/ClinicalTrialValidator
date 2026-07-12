import pandas as pd
from Preprocessor import load_and_preprocess as prep 
from Validator import Validator
from Report import report

data, symptoms, vax = prep( r'C:\Users\admin\Desktop\Python\2025VAERSDATA.csv', r'C:\Users\admin\Desktop\Python\2025VAERSSYMPTOMS.csv', r'C:\Users\admin\Desktop\Python\2025VAERSVAX.csv')
v = Validator (data, symptoms, vax)

v.datediedcheck()
v.hospcheck()
v.vaxdatecheck()
v.vaxtypecheck()
v.hospdayscheck()
v.numdayscheck()
v.aecheck()
v.deathdatecheck()
v.vaxroutecheck()
v.admincheck()
v.sexcheck()
v.refidcheck()

report(v.queries, data.shape[0], r"C:\Users\admin\Desktop\Python\output") 