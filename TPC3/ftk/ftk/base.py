#!/usr/bin/env python3
"""
Usage:
    python3 ftk [OPTIONS]

Options:
    -s            Exclude stopwords from the analysis.
    --help        Show this help message.
"""

from jjcli import *
import spacy
import sys
from collections import Counter

try:
    nlp = spacy.load("pt_core_news_sm")
except Exception as e:
    print("Error loading spaCy model:", e)
    sys.exit(1)

STOPWORDS = set([
    "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "do", "da", "em","se"
])

def lemmatize(txt, exclude_stopwords=False):
    doc = nlp(txt)
    lemmatized_tokens = []
    stopwords_found = set()

    original_tokens = [token.text.lower() for token in doc]
    print("Original tokens:", original_tokens)

    for token in doc:
        # check if the token is punctuation or whitespace
        if token.is_punct or token.is_space:
            continue
        
        lemma = token.lemma_.lower()

        for part in lemma.split():
            if part in STOPWORDS:
                stopwords_found.add(part)
            # only add non-stopwords to the lemmatized tokens
            if not (exclude_stopwords and part in STOPWORDS):
                lemmatized_tokens.append(part)

    return lemmatized_tokens, stopwords_found

def counter(tokens):
    return Counter(tokens)

def main():
    if "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)
    
    cl = clfilter("s")
    opts = cl.opt
    args = cl.args

    exclude_stopwords = '-s' in opts
    
    all_tokens = []
    all_stopwords_found = set() 
    
    for txt in cl.text():
        lemmatized_tokens, stopwords_found = lemmatize(txt, exclude_stopwords)
        print("Lemmatized:", lemmatized_tokens)
        
        all_tokens.extend(lemmatized_tokens)
        all_stopwords_found.update(stopwords_found)

    if exclude_stopwords:
        print("Stopwords found:", ', '.join(all_stopwords_found))

    c = counter(all_tokens)

    print("\n/// Token Count ///")
    token_counts = ', '.join(f"{token}: {count}" for token, count in c.items())
    print(token_counts)
