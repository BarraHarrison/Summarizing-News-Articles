import tkinter as tk
import nltk 
from textblob import TextBlob
from newspaper import Article
import nltk
nltk.download('punkt_tab')

def summarize():
    pass


# nltk.download('punkt')

# url = 'https://edition.cnn.com/2023/04/02/us/tiktok-american-culture-effects-cec/index.html'

# # The NLP work is done by the libraries
# article = Article(url)
# article.download()
# article.parse()

# article.nlp()

# print(f'Title: {article.title}')
# print(f'Authors: {article.authors}')
# print(f'Publication Date: {article.publish_date}')
# print(f'Summary: {article.summary}')

# # Sentimental Analysis
# analysis = TextBlob(article.text)
# print(analysis.polarity)
# print(f'Sentiment: {"positive" if analysis.polarity > 0 else "negative" if analysis.polarity < 0 else "neutral"}')

# Creating the GUI using tkinter
root = tk.Tk()
root.title("Python News Article Summarizer")
root.geometry('1200x600')

# Creating the individual buttons and textboxes
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140)
author.config(state='disabled', bg='#dddddd')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publication = tk.Text(root, height=1, width=140)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack()

root.mainloop()
