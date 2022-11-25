
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer

    

df = pd.read_csv("Test.csv")
df.head()
tf=TfidfVectorizer()
text_tf = tf.fit_transform(df['text'])
clf = MultinomialNB().fit(text_tf,df['label'])
newdf = pd.concat([df,pd.DataFrame({'text':["It was actually not bad"],'label': ["1"]})],ignore_index=True)
test_tf = tf.fit_transform(newdf['text'])
descs = newdf['text']
predicted = clf.predict(test_tf)
output = pd.DataFrame({'text':descs,'label':predicted})
print(output.loc[len(newdf)-1][1])
