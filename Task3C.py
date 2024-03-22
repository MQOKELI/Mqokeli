import pandas as pd
mthozami = pd.read_csv("C:\\Users\\user\\Downloads\\motor_insure.csv\\motor_data11-14lats.csv")

filter_mthozami= mthozami [mthozami['SEATS_NUM']>40]

#print(mthozami.columns)

print(filter_mthozami.head(10))