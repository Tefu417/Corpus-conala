import json

with open('corpus-conala2.txt', 'a') as newfile :

    with open('conala-json/conala-test.json') as fin :
        for data in json.load(fin) :
        # for line in fin :
            # data = json.load(line)
            # load() 辞書型になる
            s = str(data['snippet'])
            i = str(data['intent'])
            ri = str(data['rewritten_intent'])
            l = str(s + '\t' + i + '\t' + ri)
            newfile.write(l)
            newfile.write('\n')

    with open('conala-json/conala-train.json') as fin :
        for data in json.load(fin) :
        # for line in fin :
            # data = json.load(line)
            s = str(data['snippet'])
            i = str(data['intent'])
            ri = str(data['rewritten_intent'])
            l = str(s + '\t' + i + '\t' + ri)
            newfile.write(l)
            newfile.write('\n')