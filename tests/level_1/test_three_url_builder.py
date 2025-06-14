from functions.level_1.three_url_builder import build_url


def test_build_url_1():
    assert build_url(
        host_name='https://test-url.com',
        relative_url='api/v1/',
        get_params={'param1': 'pic.gif', 'param2': 'text.txt'}
    ) == 'https://test-url.com/api/v1/?param1=pic.gif&param2=text.txt'


def test_build_url_2():
    assert build_url(
        host_name='https://auto-site.com',
        relative_url='gallery'
    ) == 'https://auto-site.com/gallery'