
import sys
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Count words in files.")

    parser.add_argument("input", help="Path to the input folder containing files to process")
    parser.add_argument("output", help="Path to the output folder for results")

    parsed_args = parser.parse_args()

    return parsed_args.input, parsed_args.output

def main():
    input_folder, output_folder = parse_args()