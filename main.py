import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt_tab')


nltk.download('punkt')

url = 'https://edition.cnn.com/2023/04/02/us/tiktok-american-culture-effects-cec/index.html'

# The NLP work is done by the libraries
article = Article(url)
article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')

# Sentimental Analysis
analysis = TextBlob(article.text)
print(analysis.polarity)
print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')