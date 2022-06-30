import json
import os


if __name__ == '__main__':
    files = [i for i in os.listdir() if '.json' in i]
    #print(files)
    for file in files:
        print('\n\n====================\n\n')
        print(file)
        with open(file, 'r') as infile:
            data = json.load(infile)
        #print(data)
        ordered = sorted(data, key=lambda d: d['date'], reverse=False)
        full_text = ''
        for o in ordered:
            full_text = full_text + o['author'] + ': ' + o['content'] + '\n'
        full_text = full_text.strip()
        print(full_text)