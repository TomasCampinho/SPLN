# FTK - Text Analysis Tool

## Features

- Tokenizes input text into words and punctuation.
- Lemmatizes tokens to their base forms using the spaCy library.
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

### Example

To analyze a text and exclude stopwords:

```bash
echo "A casa azul à beira-mar é o meu sítio favorito!! Agora que penso, não me recordo se a casa é azul ou vermelha..." | python3 ftk -s
```

```bash
Tokens: ['casa', 'azul', 'à', 'é', 'meu', 'sítio', 'favorito', 'Agora', 'penso', 'não', 'me', 'recordo', 'casa', 'é', 'azul', 'vermelha']

Lemmatized: ['casa', 'azul', 'ser', 'meu', 'sítio', 'favorito', 'agora', 'pensar', 'não', 'eu', 'recordar', 'casa', 'ser', 'azul', 'vermelho']

Stopwords found: que, a, ou, o, se
```

```bash
### Token Count ###
casa: 2, azul: 2, ser: 2, meu: 1, sítio: 1, favorito: 1, agora: 1, pensar: 1, não: 1, eu: 1, recordar: 1, vermelho: 1
```


