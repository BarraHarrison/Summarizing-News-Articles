import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article

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