import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pickle
import joblib
import pathlib


def model_1(st,age,gender,inp_cause):
    
    df = pd.read_csv('D:/xhacks/xhacks/Model/Suicides_by_causes_state.csv')
    state = df[df['STATE/UT']==st]
    state_i = state.set_index("CAUSE")
    state_i = state_i.drop(["Total","Total Illness"])
    tot_state = state_i["Grand Total"].sum()
    total = state_i.loc[inp_cause].sum()
    cases = total["Grand Total"]
    ratio = cases/tot_state
    output_1 = ratio * 100

    if gender == "Male":
        a = "Total Male"
        if age<15 :
            col = "Male upto 14 years"
        elif age>14 and age<30 :
            col = "Male 15-29 years"
        elif age>29 and age<45 :
            col = "Male 30-44 years"
        elif age>44 and age<60 :
            col = "Male 45-59 years"
        elif age>59 :
            col = "Male 60 years and above"
        
    else:
        a = "Total Female"
        if age<15 :
            col = "Female upto 14 years"
        elif age>14 and age<30 :
            col = "Female 15-29 years"
        elif age>29 and age<45 :
            col = "Female 30-44 years"
        elif age>44 and age<60 :
            col = "Female 45-59 years"
        elif age>59 :
            col = "Female 60 years and above"

        
    age_cause = total[col]
    age_group = total[a]
    ratio_gender = age_cause/age_group
    output_2 = ratio_gender * 100
    
    return round(output_2,2) 

abspath = pathlib.Path('model.sav').absolute()
    
    
with open(str(abspath), 'wb') as f:
    pickle.dump(model_1, f)


print("Pickled")


