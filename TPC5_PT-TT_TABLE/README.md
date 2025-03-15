# SPLN - Grammar Parser Tool

## Features

- Parses text to identify and separate Portuguese-Tetum translations and other lines from an excerpt of the input file: "tetum-Dicionario_de_fundamentos_elementares_da".
- Generates a table of Portuguese-Tetum translations.
- Outputs non-translation lines to a separate file.

## Requirements

- Python
- `lark` library

You can install the required packages using:

```bash
pip install lark
```

## Usage

Run the script from the command line with the following syntax:

```bash
python3 grammar.py
```

The script will read the input text, parse it, and generate two output files:
- `pt_tt_table.txt`: Contains the Portuguese-Tetum translation table.
- `other_lines.txt`: Contains all other lines that are not translations.