import gensim
model = gensim.models.Word2Vec.load("wiki.zh.text.model")
print(model[u'汽车'])