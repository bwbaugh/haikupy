# Copyright (C) 2013 Brian Wesley Baugh
"""Provides syllable counting tools."""
from nltk.corpus import cmudict


# Pronunciation dictionary (CMU)
pdict = cmudict.dict()


def count(word, all=False):
    """Counts the number of syllables in a word.

    Args:
        word: The word (string) to count syllables for.
        all: Boolean indicating whether to return maximum syllable-count
            or a set of all possible counts (if the word has different
            pronunciations).

    Returns the maximum number of syllables the word contains, or if
        `all` is True, return the set of all possible counts.
    """
    all_counts = set()
    for pronunciation in pdict[word]:
        count = sum(1 for syllable in pronunciation if syllable[-1].isdigit())
        all_counts.add(count)
    if all:
        return all_counts
    else:
        return max(all_counts)
