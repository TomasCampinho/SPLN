# TPC2: Filter Out Duplicate Lines

This Python script filters out duplicate lines from a text file, helping to clean up documents by simply removing or commenting out repeated lines. It also provides optional handling for empty lines. This tool is built with `jjcli`, a lightweight command-line interface library.

## Installation

1. Download the `filter_duplicate_lines.py` script or clone this repository:
   ```bash
   git clone https://github.com/TomasCampinho/TPC2.git
   cd TPC2
   ```

2. Make the script executable:
   ```bash
   chmod +x filter_duplicate_lines.py
   ```

3. Ensure `jjcli` is installed. If not, install it using pip:
   ```bash
   pip install jjcli
   ```

## Usage

Run the script with the following command:
```bash
./filter_duplicate_lines.py [OPTIONS] FILE
```

### Options

- default (no options): Removes all duplicate non-empty lines;
- `-e`: Also removes duplicate empty lines;
- `-c`: Comments out duplicate lines instead of removing them outright.

#### Help

To see all available options, you can also run:
```bash
./filter_duplicate_lines.py --help
```