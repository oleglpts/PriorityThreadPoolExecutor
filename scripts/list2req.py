#!/usr/bin/python3

import argparse


if __name__ == '__main__':
    parameters = argparse.ArgumentParser()
    parameters.add_argument('input_file', default='./venv_installed.txt', nargs='?')
    parameters.add_argument('output_file', default='./venv_requirements.txt', nargs='?')
    args = parameters.parse_args()
    input_file = None
    try:
        input_file = open(args.input_file, 'r').readlines()
    except FileNotFoundError:
        print("File '%s' not found" % args.input_file)
        exit(1)
    output_file = open(args.output_file, 'w')
    for line in input_file:
        if line.startswith('Package') or line.startswith('---') or line.startswith('pkg-resources'):
            continue
        output_file.write('=='.join([x for x in line.strip().split(' ') if x]) + '\n')
    output_file.close()
    print('Done')
