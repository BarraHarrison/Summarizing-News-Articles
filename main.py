import tkinter as tk
from tkinter import messagebox
import nltk
from textblob import TextBlob
from newspaper import Article
from newspaper.article import ArticleException

nltk.download('punkt_tab')
nltk.download('punkt')

def clear_fields():
    for field in [title, author, publication, summary, sentiment]:
        field.config(state="normal")
        field.delete('1.0', 'end')
        field.config(state="disabled")

def summarize():
    url = utext.get('1.0', 'end').strip()
    if not url:
        messagebox.showerror("Error", "Please enter a valid URL.")
        return

    try:
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
    except ArticleException:
        messagebox.showerror("Error", "Unable to fetch or parse the article. Please check the URL.")
        return
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
        return

    clear_fields()

    # Insert data into the textboxes
    title.config(state="normal")
    title.insert('1.0', article.title)

    author.config(state="normal")
    author.insert('1.0', ", ".join(article.authors))

    publication.config(state="normal")
    publication.insert('1.0', article.publish_date)

    summary.config(state="normal")
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment_result = "Positive" if analysis.polarity > 0 else "Negative" if analysis.polarity < 0 else "Neutral"
    sentiment.config(state="normal")
    sentiment.insert('1.0', f'Polarity: {analysis.polarity:.2f}, Sentiment: {sentiment_result}')

    for field in [title, author, publication, summary, sentiment]:
        field.config(state="disabled")

# GUI Setup
root = tk.Tk()
root.title("Python News Article Summarizer")
root.geometry('1200x600')

# Layout
tlabel = tk.Label(root, text='Title')
tlabel.pack()
title = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
title.pack()

alabel = tk.Label(root, text='Author')
alabel.pack()
author = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
author.pack()

plabel = tk.Label(root, text='Publication Date')
plabel.pack()
publication = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
publication.pack()

slabel = tk.Label(root, text='Summary')
slabel.pack()
summary = tk.Text(root, height=20, width=140, bg='#dddddd', state='disabled')
summary.pack()

selabel = tk.Label(root, text='Sentiment Analysis')
selabel.pack()
sentiment = tk.Text(root, height=1, width=140, bg='#dddddd', state='disabled')
sentiment.pack()

ulabel = tk.Label(root, text='URL')
ulabel.pack()
utext = tk.Text(root, height=1, width=140)
utext.pack()

frame = tk.Frame(root)
frame.pack(pady=10)

btn = tk.Button(frame, text="Summarize", command=summarize)
btn.grid(row=0, column=0, padx=10)

clear_btn = tk.Button(frame, text="Clear", command=clear_fields)
clear_btn.grid(row=0, column=1, padx=10)

root.mainloop()
