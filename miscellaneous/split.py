import nltk.data

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
fp = open("test.txt")
data = fp.read()
listdata = list(data)
print(type(data))
print(list(tokenizer.tokenize(data)))
print('\n-----\n'.join(tokenizer.tokenize(data)))
