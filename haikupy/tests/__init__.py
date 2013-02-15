"""Unit tests using the `nose` framework."""
import haikupy


def setup():
    test_download_nltk_works()


def test_download_nltk_works():
    with open('nltk_requirements.txt') as f:
        assert haikupy.download_nltk_requirements([x.strip() for x in f])


def test_download_nltk_fails():
    assert not haikupy.download_nltk_requirements(['not-a-real-corpus'])
