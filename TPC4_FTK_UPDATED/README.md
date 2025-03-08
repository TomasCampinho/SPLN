# FTK - Text Analysis Tool

## Features

- Counts the frequency (relative and absolute) of each token.
- Optionally excludes common stopwords from the analysis.
- Lemmatizes tokens to their base (pt-pt) forms using the spaCy library.
- Calculates the ratio of token frequencies between two files.

## Requirements

- Python
- `jjcli` library
- `spaCy` library
- `pt_core_news_sm` spaCy model for Portuguese

You can install the required packages using:

```bash
pip install jjcli
pip install spacy
python -m spacy download pt_core_news_sm
pip install .
```

## Usage

Run the programs from the command line with the following syntax:

```bash
ftk-occ [OPTIONS] FILE
ftk-ratio FILE1 FILE2
```

### Options for `ftk-occ`

- (default): Print relative frequency (per million).
- `-a`: Print absolute frequency.
- `-s`: Exclude stopwords from the analysis.
- `-l`: Lemmatize the text before analyzing (pt-pt).
- `--help`: Show the help message with usage instructions.