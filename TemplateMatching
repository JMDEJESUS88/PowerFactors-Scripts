import pandas as pd
import numpy as np

# ingest both files into a dataframe
df1 = pd.read_csv('input.csv', sep=',')
df2 = pd.read_csv('templates.csv', sep=',')
tags = df1.groupby('Parent').agg(list)['Name']['test']
template_series = df2.groupby('Parent').agg(list)['Name']

best_template_percent = 0.0
best_template_index = -1
# comparing to each template and search for the best match
print("TEMPLATE MATCHES:")
for index, value in template_series.items():
    match_percent = len([v for v in tags if v in value])/len(tags)
    if match_percent >= best_template_percent:
        best_template_percent = match_percent
        best_template_index = index   
        if best_template_percent >= 0.5:
            print(f"{best_template_index}, {best_template_percent*100 :.4f}%")
            #break

match_list = template_series[best_template_index]
match_tags = sorted(list(set(tags).intersection(match_list)))
       
if len(tags) > len(match_list):
    non_match_tags = sorted(list(set(match_list).difference(tags)))
else:
    non_match_tags = sorted(list(set(tags).difference(match_list)))

#print("\nMATCHING TAGS FROM INPUT: ")
#print(*match_list, sep='\n')

print("\nMATCHING TAGS FROM INPUT: ")
print(*match_tags, sep='\n')

print("\nNON-MATCHING TAGS FROM INPUT: ")
print(*non_match_tags, sep='\n')
