import pytest
from functions.level_1.three_url_builder import build_url


@pytest.mark.parametrize(
    "host_name,relative_url,get_params,expected_result",
    [
        ('https://test-url.com', 'api/v1/', {'param1': 'pic.gif', 'param2': 'text.txt'}, 'https://test-url.com/api/v1/?param1=pic.gif&param2=text.txt'),
        ('https://auto-site.com', 'api/v1/', None, 'https://auto-site.com/api/v1/'),
    ]
)
def test__build_url__return_address_with_relative_url_and_params(host_name, relative_url, get_params, expected_result):
    assert build_url(host_name, relative_url, get_params) == expected_result
