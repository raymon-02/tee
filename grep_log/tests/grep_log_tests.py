from grep_log.grep_log import search


def test_search(tmpdir):
    inp_file = "{}/input".format(tmpdir)
    res_file = "{}/result".format(tmpdir)
    with open(inp_file, "w") as handler:
        handler.writelines(
            map(
                lambda s: "{}\n".format(s),
                [
                    "cat and dog",
                    "cat and",
                    "dog",
                    "cat dog"
                ]
            )
        )

    search(inp_file, ["cat a"], res_file)

    with open(res_file, "r") as handler:
        lines = list(map(lambda s: s.strip(), handler.readlines()))
    assert len(lines) == 2
    assert lines[0] == "cat and dog  :: 0"
    assert lines[1] == "cat and  :: 1"
