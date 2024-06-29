import argparse
import itertools
import string
from tqdm import tqdm

def generate_wordlist(input_file, output_file, start_range, number_range, pattern, full_range):

    if not input_file:
        print("You must provide a file containing the list of words.")
        return

    if not pattern:
        print("You must provide a pattern.")
        return
    
    if not output_file:
        output_file = 'output.txt'

    if 'n' in pattern and not number_range:
        print("You must provide a range of numbers to use with the pattern.")
        return

    if number_range and (not number_range.isdigit() or int(number_range) <= 0):
        print("The range must be a positive number.")
        return

    if start_range and (not start_range.isdigit() or int(start_range) < 0):
        print("The start range must be a non-negative number.")
        return

    if 'n' not in pattern or 'c' not in pattern:
        print("You must provide at least one pattern with the range.")
        return

    number_range = int(number_range)
    start_range = int(start_range) if start_range else 0
    special_chars = string.punctuation
    letters = string.ascii_letters
    printable = string.printable

    with open(input_file, 'r') as infile:
        words = infile.read().splitlines()

    total_combinations = 1
    for p in pattern.split(','):
        if p == 'w':
            total_combinations *= len(words)
        elif p == 'n':
            total_combinations *= number_range
        elif p == 'c':
            total_combinations *= len(special_chars)
    
    with open(output_file, 'w') as outfile:
        for word in tqdm(words, desc="Generating wordlist", unit="word"):
            # Generate all possible combinations
            for combo in itertools.product(*(get_pattern_elements(p, word, start_range, number_range, special_chars, full_range, letters, printable) for p in pattern.split(','))):
                new_word = ''.join(combo)
                outfile.write(new_word + '\n')

def get_pattern_elements(p, word, start_range, number_range, special_chars, full_range, letters, printable):
    if p == 'w':
        return [word]
    elif p == 'n':
        if full_range:
            width = len(str(number_range - 1))
            return [f"{start_range + i:0{width}}" for i in range(number_range)]
        else:
            return [f"{start_range + i:0}" for i in range(number_range)]
    elif p == 'c':
        return list(special_chars)
    elif p == 'l':
        return list(letters)
    elif p == 'p':
        return list(printable)
    else:
        return ['']

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate combined passwords.")
    parser.add_argument("-w", "--word", required=True, help="File containing the list of words.")
    parser.add_argument("-r", "--range", help="Range of numbers to add.")
    parser.add_argument("-sr", "--start-range", type=int, help="Starting point of the number range.")
    parser.add_argument("-fr", "--full_range", action='store_true', help="Use full range for the length of numbers.")
    parser.add_argument("-p", "--pattern", required=True, help="Pattern of the password (c for special characters, n for numbers, l for letters, p for allprintable, w for the word), example: -p=c,n,p,w,n,l")
    parser.add_argument("-o", "--output", required=True, help="Output file to write the generated combinations.")

    args = parser.parse_args()

    generate_wordlist(args.word, args.output, args.range, args.pattern, args.full_range)
