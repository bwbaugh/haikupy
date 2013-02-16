# Copyright (C) 2013 Brian Wesley Baugh
from haikupy import syllables


def test_correct_count():
    assert syllables.count('good') == 1
    assert syllables.count('comically') == 4


def test_correct_count_all():
    assert syllables.count('comically', all=True) == set([3, 4])
