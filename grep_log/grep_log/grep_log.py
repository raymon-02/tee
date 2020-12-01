import argparse
import os
from functools import partial

import ahocorasick


def parse_args():
    parser = argparse.ArgumentParser(description="Grep file or files in folder for several patterns")
    parser.add_argument("file", metavar="file", type=str, nargs=1,
                        help="input file/folder name")
    parser.add_argument("patterns", metavar="patterns", type=str, nargs="+",
                        help="a pattern used for grep")
    parser.add_argument("-r", "--result", metavar="result",
                        help="greped output file name")
    return parser.parse_args()


def get_result_name(file):
    greped = "-greped"

    parts = file.rsplit(".", 1)
    if len(parts) == 1:
        return "{}{}".format(parts[0], greped)

    parts[-2] += greped
    return ".".join(parts)


def search_in_file(file, res_handler, automaton, include_name=False):
    with open(file) as handler:
        for i, line in enumerate(handler.readlines()):
            found = False
            for _, _ in automaton.iter(line):
                found = True
                break
            line = line.rstrip()
            if found:
                if include_name:
                    res_handler.write(
                        "{}  :: {}:{}\n".format(line, os.path.basename(file), i)
                    )
                else:
                    res_handler.write("{}  :: {}\n".format(line, i))


def search(file, patterns, result_file):
    automaton = ahocorasick.Automaton()
    for i, key in enumerate(patterns):
        automaton.add_word(key, (i, key))
    automaton.make_automaton()

    with open(result_file, "w") as res_handler:
        search_in = partial(search_in_file, res_handler=res_handler, automaton=automaton)
        if os.path.isdir(file):
            for root, _, files in os.walk(file):
                for f in sorted(files, key=os.path.splitext):
                    search_in(os.path.join(file, f), include_name=True)
        else:
            search_in(file)


def main():
    args = parse_args()
    file = args.file[0]
    result_file = args.result or get_result_name(file)
    patterns = args.patterns

    search(file, patterns, result_file)

    return 0  # success
