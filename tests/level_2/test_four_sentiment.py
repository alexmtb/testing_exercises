from functions.level_2.four_sentiment import check_tweet_sentiment
import pytest


def test__check_tweet_sentiment__good_sentiment():
    test_text = 'I love programming and writing tests'
    test_good_words = {'love', 'programming', 'tests'}
    test_bad_words = {'hate', 'bugs'}

    tweet_sentiment =  check_tweet_sentiment(
        text=test_text,
        good_words=test_good_words,
        bad_words=test_bad_words
    )
    assert tweet_sentiment == "GOOD"
    

def test__check_tweet_sentiment__bad_sentiment():
    test_text = 'I hate JavaScript and frontend development'
    test_good_words = {'development', 'programming', 'tests'}
    test_bad_words = {'hate', 'frontend'}

    tweet_sentiment =  check_tweet_sentiment(
        text=test_text,
        good_words=test_good_words,
        bad_words=test_bad_words
    )
    assert tweet_sentiment == "BAD"


def test__check_tweet_sentiment__neutral_sentiment():
    test_text = 'I like coding on Python but I also dislike bugs'
    test_good_words = {'coding', 'python'}
    test_bad_words = {'dislike', 'bugs'}

    tweet_sentiment =  check_tweet_sentiment(
        text=test_text,
        good_words=test_good_words,
        bad_words=test_bad_words
    )
    assert tweet_sentiment is None


def test__check_tweet_sentiment__empty_word_dictionaries():
    test_text = 'I like coding on Python but I also dislike bugs'
    test_good_words = {}
    test_bad_words = {}

    tweet_sentiment =  check_tweet_sentiment(
        text=test_text,
        good_words=test_good_words,
        bad_words=test_bad_words
    )
    assert tweet_sentiment is None


def test__check_tweet_sentiment__input_():
    test_text = 179345682
    test_good_words = {'coding', 'python'}
    test_bad_words = {'dislike', 'bugs'}

    with pytest.raises(AttributeError):
        check_tweet_sentiment(
            text=test_text,
            good_words=test_good_words,
            bad_words=test_bad_words
        )


if __name__ == "__main__":
    func_test = check_tweet_sentiment(
        text = 179345682,
        good_words = {'coding', 'python'},
        bad_words = {'dislike', 'bugs'}
    )
    print(func_test)