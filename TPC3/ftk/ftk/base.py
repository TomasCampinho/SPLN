#!/usr/bin/env python3
"""
Usage:
    python3 ftk [OPTIONS]

Options:
    -s            Exclude stopwords from the analysis.
    --help        Show this help message.
"""

from jjcli import *
import re
from collections import Counter
import spacy
import sys

try:
    nlp = spacy.load("pt_core_news_sm")
except Exception as e:
    print("Error loading spaCy model:", e)
    sys.exit(1)

STOPWORDS = set([
    "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "do", "da", "em", "para",
    "com", "que", "se", "ou"
])

def lexer(txt, exclude_stopwords=False):
    tokens = re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)
    stopwords_found = set()
    
    for token in tokens:
        lower_token = token.lower()
        if lower_token in STOPWORDS:
            stopwords_found.add(lower_token)

    if exclude_stopwords:
        tokens = [token for token in tokens if token.lower() not in STOPWORDS and token.isalpha()]
        
    return tokens, stopwords_found

def lemmatize(tokens, exclude_stopwords=False):
    doc = nlp(" ".join(tokens))
    return [token.lemma_.lower() for token in doc if (not exclude_stopwords or token.lemma_ not in STOPWORDS) and token.lemma_.isalpha()]

def counter(tokens):
    return Counter(tokens)

def main():
    if "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)
    
    cl = clfilter("s")
    opts = cl.opt
    args = cl.args

    exclude_stopwords = '--stopwords' in opts or '-s' in opts
    
    tokens = []
    all_stopwords_found = set() 
    
    for txt in cl.text():
        t, stopwords_found = lexer(txt, exclude_stopwords)
        print("\nTokens:", t)
        lemmatized_tokens = lemmatize(t, exclude_stopwords)
        print("\nLemmatized:", lemmatized_tokens)
        tokens.extend(lemmatized_tokens)
        all_stopwords_found.update(stopwords_found)

    if exclude_stopwords:
        print("\nStopwords found:", ', '.join(all_stopwords_found))

    c = counter(tokens)

    print("\n### Token Count ###")
    token_counts = ', '.join(f"{token}: {count}" for token, count in c.items())
    print(token_counts)