import requests
import pandas as pd
import os

LINK_LINE = 1
LECTURE_LINE = 3

config_file = open("config.txt", "r")
keywords = []
lines = config_file.readlines()
link = lines[LINK_LINE][0:-1]

for line in lines[LECTURE_LINE:]:
    if len(line) > 1:
        lecture_to_append = line[0:-1]
        keywords.append(lecture_to_append)

html = requests.get(link).content
df_list = pd.read_html(html)
for i, df in enumerate(df_list):
    df.to_csv('raw_data.csv')

df = pd.read_csv("raw_data.csv", delimiter=',')
os.remove("raw_data.csv")
df.columns = ["", "lv", "registration_date", "exam_date"]

new_df = df.loc[df['lv'].str.contains("|".join(keywords))]
new_df = new_df[["lv", "exam_date"]]
print(new_df)
new_df.to_csv("relevant_exams.csv".format(new_df))
