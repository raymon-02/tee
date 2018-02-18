import functools
import io
import sys

import pytest

from tee import suppressed, suppressed_recursive, open_files, tee_command


class check_call_times:
    def __init__(self, call_at_least):
        self.call_at_least = call_at_least
        self.count = 0

    def __call__(self, func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            if self.call_at_least > self.count:
                self.count += 1
                func(*args, **kwargs)
            else:
                return
            assert self.call_at_least <= self.count

        return inner


def test_check_times():
    @check_call_times(3)
    def recursive_func(count):
        if count >= 3:
            return
        recursive_func(count + 1)

    recursive_func(1)


def test_check_times_raise_assertion_error():
    @check_call_times(3)
    def recursive_func(count):
        if count >= 2:
            return
        recursive_func(count + 1)

    with pytest.raises(AssertionError):
        recursive_func(1)


def test_suppressed_key_error():
    @suppressed(KeyError)
    def raise_exception():
        raise KeyError

    raise_exception()


def test_suppressed_exception():
    @suppressed(Exception)
    def raise_exception():
        raise Exception

    raise_exception()


def test_suppressed_subclass_exception():
    @suppressed(Exception)
    def raise_exception():
        raise KeyError

    raise_exception()


def test_not_suppressed_io_error():
    @suppressed(KeyError)
    def raise_exception():
        raise IOError

    with pytest.raises(IOError):
        raise_exception()


def test_suppressed_key_error_recursive():
    @suppressed_recursive(KeyError)
    @check_call_times(2)
    def raise_exception():
        raise KeyError

    raise_exception()


def test_suppressed_exception_recursive():
    @suppressed_recursive(Exception)
    @check_call_times(2)
    def raise_exception():
        raise Exception

    raise_exception()


def test_suppressed_subclass_exception_recursive():
    @suppressed_recursive(Exception)
    @check_call_times(2)
    def raise_exception():
        raise KeyError

    raise_exception()


def test_not_suppressed_io_error_recursive():
    @suppressed_recursive(KeyError)
    def raise_exception():
        raise IOError

    with pytest.raises(IOError):
        raise_exception()


def test_open_files(tmpdir):
    message = "Work"
    file_first = "{}/first.txt".format(tmpdir)
    file_second = "{}/second.txt".format(tmpdir)
    with open_files([file_first, file_second], "w") as handles:
        for handle in handles:
            handle.write(message)
    for handle in handles:
        assert handle.closed
    with open(file_first) as handle:
        assert handle.readline() == message
    with open(file_second) as handle:
        assert handle.readline() == message


def test_tee_console_output(capsys, monkeypatch):
    message = "Work"
    handle = io.StringIO("Work")
    monkeypatch.setattr(sys, "stdin", handle)

    tee_command()

    output, _err = capsys.readouterr()
    assert output == message
