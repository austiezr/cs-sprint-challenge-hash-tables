# Your code here


def finder(files, queries):
    """
    YOUR CODE HERE
    """
    table = {x: [] for x in files}
    for x in range(len(queries)):
        for y in table:
            if y[y.rindex('/')+1:] in queries[x]:
                table[y].append(queries[x])

    table = {k: v for k, v in table.items() if v != []}

    return [x for x in table.keys()]


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz',
        '/usr/foo'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
