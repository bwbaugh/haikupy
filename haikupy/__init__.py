# Copyright (C) 2013 Brian Wesley Baugh
"""An English language haiku generator that uses the 5-7-5 syllable pattern."""
import nltk


NLTK_DEPENDENCIES = [
                     'cmudict',
                     'maxent_treebank_pos_tagger',
                     'wordnet',
                    ]
nltk.download(NLTK_DEPENDENCIES)
