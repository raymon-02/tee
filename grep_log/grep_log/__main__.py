import sys


def main():
    try:
        from .grep_log import main
        exit_code = main()
    except KeyboardInterrupt:
        exit_code = 130  # ctrl+c
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
