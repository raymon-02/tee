import argparse
import functools
import sys
from contextlib import contextmanager, ContextDecorator, suppress as _suppress


class suppressed(_suppress, ContextDecorator):
    pass


class suppressed_recursive:
    def __init__(self, exception):
        self.exception = exception

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except self.exception:
                return inner(*args, **kwargs)

        return inner


@contextmanager
def open_files(files, mode):
    handles = []
    for file in files:
        try:
            handles.append(open(file, mode))
        except IOError:
            print("IOError during opening file: {}".format(file))
    try:
        yield handles
    finally:
        for handle in handles:
            handle.close()


def parse_args():
    parser = argparse.ArgumentParser(description="tee command")
    parser.add_argument("-i", dest="keyboard_interrupt", const=KeyboardInterrupt, default=None, action="store_const",
                        help="disable interruption")
    parser.add_argument("-a", dest="mode", const="a", default="w", action="store_const",
                        help="append output to files")
    parser.add_argument("files", metavar="file", type=str, nargs="*",
                        help="file to write output")
    return parser.parse_args()


@suppressed(Exception)
def tee_command(files=None, mode="w", keyboard_interrupt=None):
    files = files or []

    @suppressed_recursive(keyboard_interrupt)
    def tee_write_output(handles):
        for line in sys.stdin:
            print(line, end="")
            for handle in handles:
                handle.write(line)
                handle.flush()

    with open_files(files, mode) as handles:
        tee_write_output(handles)


def main():
    args = parse_args()
    files = args.files
    mode = args.mode
    keyboard_interrupt = args.keyboard_interrupt
    tee_command(files, mode, keyboard_interrupt)


if __name__ == '__main__':
    main()
