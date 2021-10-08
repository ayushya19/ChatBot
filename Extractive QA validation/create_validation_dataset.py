import pandas as pd
import json
import os


file_path = './validation_data.csv'
old_file = 0


if os.path.isfile(file_path):
    print("[INFO]...Found existing files :- Continuting")
    old_file = 1
else:
    print("[INFO]...Creating new files")


questions = []
expected_answers = []

while(1):
    question = input("Enter Question: ")
    if question == '-1':
        break
    e_ans = input("Enter Answer: ")

    questions.append(question)
    expected_answers.append(e_ans)


df = pd.DataFrame(list(zip(questions, expected_answers)), columns=[
                  'Question', 'ExpectedAnswer'])

if old_file:
    old_df = pd.read_csv(file_path)
    old_df = old_df.append(df)
    newjson = old_df.to_json(orient='records', indent=4)
    old_df.to_csv(file_path, index=False)
    with open(file_path.replace('.csv', '.json'), 'w') as f:
        f.write(newjson)
else:
    df2json = df.to_json(orient='records', indent=4)
    df.to_csv(file_path, index=False)
    with open(file_path.replace('.csv', '.json'), 'w') as f:
        f.write(df2json)
