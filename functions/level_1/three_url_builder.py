from typing import Mapping


def build_url(
        host_name: str,
        relative_url: str,
        get_params: Mapping[str, str] = None
    ) -> str:
    get_params = get_params or {}
    querypart = ''
    if get_params:
        querypart = '?' + '&'.join([f'{k}={v}' for (k, v) in get_params.items()])
    return f'{host_name}/{relative_url}{querypart}'


if __name__ == '__main__':
    # Test function
    url = build_url('https://test-url.com', 'api/v1/', {'param1': 'pic.gif', 'param2': 'text.txt'})
    print(url)