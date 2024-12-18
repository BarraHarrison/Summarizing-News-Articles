## Python News Article Summarizer 
This project is a Python News Article Summarizer application that uses Natural Language Processing (NLP) to extract and summarize news articles.
The application is built with tkinter for a graphical user interface (GUI) and utilizes popular Python libraries like newspaper3k, nltk, and textblob for NLP operations.

## Libraries Used
- tkinter: For the GUI interface.
- newspaper3k: For downloading and parsing news articles.
- nltk: For NLP operations such as sentence tokenization.
- textblob: For sentiment analysis.

## How the summarizer works
- The user inputs a URL into the "URL" textbox.
- Upon clicking the "Summarize" button, the application:
- Downloads and parses the article using newspaper3k.
- Extracts the title, authors, publication date, and summary.
- Analyzes the sentiment of the article using textblob.
- The results are displayed in the respective textboxes in the GUI.
