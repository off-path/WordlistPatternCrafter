import argparse
import itertools
import string
from tqdm import tqdm

def generate_wordlist(args):

    input_file = args.word
    number_range = int(args.range)
    start_range = int(args.start_range) if args.start_range else 0
    full_range = args.full_range
    pattern = args.pattern
    output_file = args.output
    special_chars = string.punctuation
    letters = string.ascii_letters
    printable = string.printable

    with open(input_file, 'r') as infile:
        words = infile.read().splitlines()
    
    if args.lowercase:
        words = [word.lower() for word in words]
    
    if args.uppercase:
        words = [word.upper() for word in words]
    
    if args.lower_upper:
        words = [word.lower() for word in words] + [word.upper() for word in words]

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
    parser.add_argument("-sr", "--start_range", type=int, help="Starting point of the number range.")
    parser.add_argument("-fr", "--full_range", action='store_true', help="Use full range for the length of numbers.")
    parser.add_argument("-p", "--pattern", required=True, help="Pattern of the password (c for special characters, n for numbers, l for letters, p for allprintable, w for the word), example: -p=c,n,p,w,n,l")
    parser.add_argument("-o", "--output", help="Output file to write the generated combinations.")
    parser.add_argument("-l", "--lowercase", action='store_true', help="Convert all words to lowercase.")
    parser.add_argument("-u", "--uppercase", action='store_true', help="Convert all words to uppercase.")
    parser.add_argument("-lu", "--lower_upper", action='store_true', help="Convert all words to lower and uppercase.")

    generate_wordlist(parser.parse_args())
