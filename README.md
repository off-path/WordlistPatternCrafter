# WordlistCraft

WordlistCraft is a powerful tool for generating customized wordlists based on user-defined patterns. It can combine words, numbers, special characters, and more to create comprehensive wordlists for various purposes, such as password generation, security testing, and more.

## Features

- Combines words, numbers, special characters, and other printable characters based on user-defined patterns.
- Supports full range number formatting.
- Outputs the generated combinations to a specified file.

## Requirements

- Python 3.x
- tqdm (`pip install tqdm`)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/offpath/WordlistCraft.git
    ```
2. Navigate to the project directory:
    ```bash
    cd WordlistCraft
    ```
3. Install the required package:
    ```bash
    pip install tqdm
    ```

## Usage

WordlistCraft can be used via the command line. Below are the arguments it accepts:

- `-w, --word` (required): Path to the file containing the list of words.
- `-r, --range`: Range of numbers to add.
- `-fr, --full_range`: Use full range for the length of numbers (e.g., 001, 002, ...).
- `-p, --pattern` (required): Pattern of the password. The pattern can include:
  - `c` for special characters
  - `n` for numbers
  - `l` for letters
  - `p` for all printable characters
  - `w` for the word from the input file
- `-o, --output` (required): Path to the output file to write the generated combinations.

### Example Command

```bash
python wordlistcraft.py -w words.txt -r 100 -sr 50 -p c,n,w,n,l -o output.txt
```

This command will:
- Read words from words.txt
- Start the range of numbers from 50 up to 149 (100 numbers starting from 50).
- Follow the pattern of special characters, numbers, word, numbers, and letters.
- Write the generated combinations to output.txt.


## Detailed Explanation

#### Patterns

The pattern defines how the wordlist will be generated. Each letter in the pattern represents a different type of element:

  - `c`: Special characters (e.g., !, @, #)
  - `n`: Numbers (requires --range to be specified)
  - `l`: Letters (both uppercase and lowercase)
  - `p`: All printable characters
  - `w`: All printable characters

For example, the pattern c,n,w,n,l will generate combinations where:

 - The first character is a special character.
 - The second character is a number.
 - The third part is a word from the input file.
 - The fourth character is a number.
 - The fifth character is a letter.


#### Full Range

Using the --full_range option will pad the numbers with leading zeros up to the length of the highest number in the range. For example, if the range is 100, numbers will be formatted as 001, 002, ..., 099.

#### start-range

The `-sr` or `--start-range` parameter specific to the starting point of the range of numbers to generate. If this parameter is used, numbers will be generated from this value up to the value `start_range + number_range - 1`, where `number_range` is the number range specified by `-r`.

#### Input File

The input file specified by -w or --word should contain one word per line.

#### Output File

The output file specified by -o or --output will contain the generated wordlist with each combination on a new line.