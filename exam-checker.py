import requests
import pandas as pd
import os

link = "https://lfuonline.uibk.ac.at/public/lfuonline_lv.anmeldetermine?c=search&m=3&d=1&dft=&dfm=&dfj=&dtt=&dtm=&dtj=&r=205853&s=1"
keywords = ["VO Lineare Algebra",
            "VO Funktionale Programmierung",
            "VO Maschinelles Lernen",
            "VO Rechnerarchitektur",
            "VO Betriebssysteme",
            "VO Parallele Programmierung",
            "VO Software Engineering",
            "VO Diskrete Strukturen",
            "VO Angewandte Mathematik",
            "VO Rechnernetze und Internettechnik",
            "VO Verteilte Systeme",
            "VO Visual Computing",
            "VO Logik"]

html = requests.get(link).content
df_list = pd.read_html(html)
for i, df in enumerate(df_list):
    df.to_csv('raw_data.csv')

df = pd.read_csv("raw_data.csv", delimiter=',')
os.remove("raw_data.csv")
df.columns = ["","lv","registration_date","exam_date"]
print(df)

new_df = df.loc[df['lv'].str.contains("|".join(keywords))]
new_df = new_df[["lv","exam_date"]]
print(new_df)
new_df.to_csv("relevant_exams.csv".format(new_df))

