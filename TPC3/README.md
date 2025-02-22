# FTK - Text Analysis Tool

## Features

- Lemmatizes tokens to their base (pt-pt) forms using the spaCy library.
- Counts the frequency of each token.
- Optionally excludes common stopwords from the analysis.

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
```

## Usage

Run the program from the command line with the following syntax:

```bash
python3 ftk [OPTIONS]
```

### Options

- `-s`: Exclude stopwords from the analysis.
- `--help`: Show the help message with usage instructions.

## Examples

To analyze a text (default):

```bash
echo "pensa-se em vice-versa. Sim, em vice-versa." | python3 ftk
```

```bash
Original tokens: ['pensa-se', 'em', 'vice-versa', '.', 'sim', ',', 'em', 'vice-versa', '.', '\n']
Lemmatized: ['pensar', 'se', 'em', 'vice-versa', 'sim', 'em', 'vice-versa']

/// Token Count ///
pensar: 1, se: 1, em: 2, vice-versa: 2, sim: 1
```

To also exclude stopwords:

```bash
echo "pensa-se em vice-versa. Sim, em vice-versa." | python3 ftk -s
```

```bash
Original tokens: ['pensa-se', 'em', 'vice-versa', '.', 'sim', ',', 'em', 'vice-versa', '.', '\n']
Lemmatized: ['pensar', 'vice-versa', 'sim', 'vice-versa']
Stopwords found: em, se

/// Token Count ///
pensar: 1, vice-versa: 2, sim: 1
```