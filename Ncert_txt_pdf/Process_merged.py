import re
import os


def readFile(path):
    '''
    reads the .txt file from path
    '''
    text = ''
    with open(path, encoding='utf-8') as f:
        lines = [line.rstrip() for line in f.readlines()]

        for line in lines:
            text += line
            text += '\n'

    return text


def removeExercise(text):
    '''
    removes the text between exercises and additional exercises.
    [Note]: Still requires to manually remove the last exercise.
    '''
    regex = re.compile('(?s)(?<=EXERCISES).*?(?=ADDITIONAL EXERCISES)')
    modified_text = re.sub(regex, ' ', text)
    return modified_text


def formSentences(text):
    '''
    1. Based on '.' and '?' sentences are joined together.
    2. Smaller length sentences (<=15) are removed (mostly noise).
    '''
    mtext = ''
    for i in text:
        if i == '.' or i == '?':
            mtext += i+'\n'
        elif i == '\n':
            mtext += ' '
        else:
            mtext += i

    lst = mtext.split('\n')
    toRemove = []
    for i in range(len(lst)):
        if len(lst[i]) <= 15:
            toRemove.append(i)

    newlist = [lst[i] for i in range(len(lst)) if i not in toRemove]
    final = ''
    for i in newlist:
        final += i+'\n'
    return final


if __name__ == '__main__':
    os.makedirs('ProcessedText', exist_ok=True)
    files = os.listdir('./ProcessedText')
    for file in files:
        file_path = './ProcessedText/' + file
        text = readFile(file_path)
        # processedText = removeExercise(text)
        processedText = formSentences(text)
        new_file = open('./ProcessedText/'+file.split('.')[0] + '_processed.txt',
                        'w', encoding='utf-8')
        new_file.writelines(processedText)
        new_file.close()

    # text = readFile('./Dataset/MergedText_v1.txt')
    # processedText = removeExercise(text)

    # text_file = open("./Dataset/Merged_No_Exercises_v2.txt", "w", encoding='utf-8')
    # text_file.write(processedText)
    # text_file.close()

    # text = readFile('./Dataset/Merged_Text_NoExample_v3.txt')
    # processedText = formSentences(text)
    # text_file = open("./Dataset/Merged_with_sentences_v4.txt",
    #                  "w", encoding='utf-8')
    # text_file.write(processedText)
    # text_file.close()
