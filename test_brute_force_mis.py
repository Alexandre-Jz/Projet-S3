from brute_force_MIS import brute_force_mis


def test_brute_force_MIS_1():
    G = {
        "a": ["s", "e", "c", "b"],
        "b": ["a", "c", "f"],
        "c": ["a", "b", "f", "e", "d"],
        "d": ["e", "c", "f"],
        "e": ["s", "a", "c", "d"],
        "f": ["d", "c", "b"],
        "s": ["a", "e"],
    }

    set_test = set()

    for i in brute_force_mis(G):
        set_test.add(i)

    assert set_test == set({"s", "b", "d"})


def test_brute_force_MIS_2():
    G = {
        "a": ["s", "e", "c", "b"],
        "b": ["a", "c", "f"],
        "c": ["a", "b", "f", "e", "d"],
        "d": ["e", "c", "f", "s"],
        "e": ["s", "a", "c", "d"],
        "f": ["d", "c", "b"],
        "s": ["a", "e", "d"],
    }

    set_test = set()

    for i in brute_force_mis(G):
        set_test.add(i)

    assert set_test == set({"s", "b"})
