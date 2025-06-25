from functions.level_2.one_pr_url import is_github_pull_request_url


def test__is_github_pull_request_url__domain_correct():
    url = "https://github.com/alexmtb/testing_exercises/pull/01"
    assert is_github_pull_request_url(url) == True


def test__is_github_pull_request_url__domain_incorrect():
    url = "https://gitlab.com/alexmtb/testing_exercises/pull/01"
    assert is_github_pull_request_url(url) == False


def test__is_github_pull_request_url__mode_not_pull():
    url = "https://github.com/alexmtb/testing_exercises/actions/new"
    assert is_github_pull_request_url(url) == False


def test__is_github_pull_request_url__bad_splitted_url_len():
    url = "https://github.com/alexmtb/testing_exercises/tree/main/functions"
    assert is_github_pull_request_url(url) == False


if __name__ == '__main__':
    # check corect url
    url = "https://github.com/alexmtb/testing_exercises/pull/01"
    print(is_github_pull_request_url(url))