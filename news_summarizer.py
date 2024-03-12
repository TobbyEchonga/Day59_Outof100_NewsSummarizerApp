from newspaper import Article
from gensim.summarization import summarize

def extract_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

def generate_summary(text, ratio=0.2):
    summary = summarize(text, ratio=ratio)
    return summary

if __name__ == '__main__':
    # Example news article URL
    article_url = "https://example.com/sample-news-article"

    # Extract the article content
    article_text = extract_article(article_url)

    # Generate and print the summary
    summary = generate_summary(article_text)
    print(f"Original Article:\n{article_text}\n\nSummary:\n{summary}")
