import pandas as pd
from tqdm.auto import tqdm
import re

df = pd.read_csv('./Electricity_wiki.csv')

print(df.head())

df = df.dropna()  # remove the null rows.


'''
with open('Electricity_text_only.txt', 'a', encoding='utf-8') as f:
    for i in (range(len(df))):
        text = df['text'].iloc[i]
        if len(text) < 100:
            pass
        else:
            for line in text.split('\n'):
                if len(line) > 100:
                    f.write(line)
                    f.write('\n')
                else:
                    f.write('\n')
'''

flist = open('Electricity_text_only.txt', encoding='utf-8').readlines()
lines = [s.rstrip('\n') for s in flist]


def remove_curly(text):
    regex = re.compile('{.*}')
    modified_text = re.sub(regex, ' ', text)
    return modified_text


nf = open('cleaned_wiki_text.txt', 'a', encoding='utf-8')
cleanLines = []
for l in lines:
    if l == '':
        pass
    else:
        t = remove_curly(l)
        cleanLines.append(t + '\n')

nf.writelines(cleanLines)
nf.close()
