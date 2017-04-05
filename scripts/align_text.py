#!/usr/bin/python

import regex as re
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description="""
    
    python align_text.py reads_file reference_file

    Align a set of "reads" or chunks of text to a
    reference text.
""")

    parser.add_argument('reads_file')
    parser.add_argument('reference_file')
    #parser.add_argument('-o', '--options', default='yo',
    #					 help="Some option", type='str')
    #parser.add_argument('-u', '--useless', action='store_true', 
    #					 help='Another useless option')

    args = parser.parse_args()

    if args.reads_file == '-':
        f_reads = sys.stdin
    else:
        f_reads = open(args.reads_file)

    f_reference = open(args.reference_file, 'r')

    reference_text = " ".join([l.strip().lower() for l in f_reference.readlines()])
    print("reference_text:", reference_text)

    for line in f_reads:
        read = r"{}".format(line.strip().replace('[', '\[').replace(']', '\]'))
        print("read:", read)
        for m in re.finditer(read + "{e<=2}" , reference_text):
            print("m:", m)


if __name__ == '__main__':
    main()


