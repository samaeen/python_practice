from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

sents="this is a bullshit thing to do . so please go fuck yourself"
stop_words=set(stopwords.words("english"))

words=word_tokenize(sents)
filt_sents=[]

for w in words:
	if w not in stop_words:
		filt_sents.append(w)

print(filt_sents)