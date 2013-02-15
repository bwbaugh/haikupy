# Copyright (C) 2013 Brian Wesley Baugh
"""An English language haiku generator that uses the 5-7-5 syllable pattern."""
import nltk


def download_nltk_requirements(data_list):
    if not all(nltk.download(data.strip()) for data in data_list):
        return False
    return True
