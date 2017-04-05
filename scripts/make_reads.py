#!/usr/bin/python

import random
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python make_reads.py reference_text

    Chop a text up into smaller "reads"
""")

    parser.add_argument('reference')
    parser.add_argument('-l', '--read-length', default=10,
    					 help="Read length",
                                         type=int) 
    parser.add_argument('-n', '--num-reads', default=100,
                                         help="The number of reads to generate",
                                         type=int)

    args = parser.parse_args()

    whole_text = " ".join([l.strip().lower() for l in open(args.reference,'r').readlines()])

    args = parser.parse_args()

    for i in range(args.num_reads):
        start_pos = random.randint(0, len(whole_text) - args.read_length)
        read = whole_text[start_pos:start_pos + args.read_length]
        print(read)
    

if __name__ == '__main__':
    main()


