import re
import os

txtFiles = os.listdir('../ReferenceBooks/txtFiles')

for Text in txtFiles:
    finalFile = open('../ReferenceBooks/txtFiles/v2/'+Text.split('.')
                     [0].replace(' ', '_') + '_v2.txt', 'w', encoding='utf-8')
    with open('../ReferenceBooks/txtFiles/' + Text, encoding="utf8") as f:
        lines = [line.rstrip() for line in f.readlines()]

        regex = re.compile('^Fig|^[0-9]|^[\(]|^|^n|^SCIENCE')

    for line in lines:
        if re.match(regex, line):
            pass
        elif len(line) in [0, 1]:
            pass

        elif len(line) < 5:
            finalFile.write(line + " ")
        else:
            finalFile.write(line + "\n")

    finalFile.close()
