#!/usr/bin/env python3
"""
Usage:
    ftk-occ [OPTIONS] FILE

Options:
    (default)     Print relative frequency (per million).
    -a            Print absolute frequency.
    -s            Exclude stopwords from the analysis.
    -l            Lemmatize the text before analyzing (pt-pt).
    --help        Show this help message.
"""

from jjcli import *
import spacy
import sys
from collections import Counter
import re

try:
    nlp = spacy.load("pt_core_news_sm")
except Exception as e:
    print("Error loading spaCy model:", e)
    sys.exit(1)

def lexer(txt):
    return re.findall(r'\b\w+(?:-\w+)*\b|[^\w\s]', txt)

STOPWORDS = set([
    "a", "o", "as", "os", "um", "uma", "uns", "umas", "de", "do", "da", "em","se"
])

def lemmatize(txt, exclude_stopwords=False):
    doc = nlp(txt)
    lemmatized_tokens = []
    stopwords_found = set()

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

def absolute_frequency(counter):
    return dict(counter.most_common())

def relative_frequency(counter):
    total_count = sum(counter.values())
    return {token: (count / total_count) * 1000000 for token, count in counter.most_common()}

def main():
    if "--help" in sys.argv:
        print(__doc__)
        sys.exit(0)
    
    cl = clfilter("sal")
    opts = cl.opt
    args = cl.args

    exclude_stopwords = '-s' in opts
    print_absolute = '-a' in opts
    lemmatize_text = '-l' in opts
    
    all_tokens = []
    all_stopwords_found = set() 
    
    for txt in cl.text():
        if lemmatize_text:
            lemmatized_tokens, stopwords_found = lemmatize(txt, exclude_stopwords)
            all_tokens.extend(lemmatized_tokens)
            all_stopwords_found.update(stopwords_found)
        else:
            tokens = lexer(txt)
            if exclude_stopwords:
                tokens = [token for token in tokens if token not in STOPWORDS]
            all_tokens.extend(tokens)

    if exclude_stopwords:
        print("Stopwords found:", ', '.join(all_stopwords_found))

    c = counter(all_tokens)

    total_tokens = sum(c.values())
    print(f"Total tokens: {total_tokens}\n")

    if print_absolute:
        abs_freq = absolute_frequency(c)
        #print("/// Absolute Frequency ///")
        for token, count in abs_freq.items():
            print(f"{count}  {token}")
    else:
        rel_freq = relative_frequency(c)
        #print("/// Relative Frequency ///")
        for token, freq in rel_freq.items():
            print(f"{freq:.3f}  {token}")
