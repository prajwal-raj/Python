import bs4
import requests


def verify_links(url):
    """
    Verifies all links within the page at the provided url. Broken links are
    printed and counted.

    :param str url: address to website to verify links
    """
    result = requests.get(url)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(f'There was a problem with the provided URL: \n\t{e}')
        exit()

    soup = bs4.BeautifulSoup(result.content)
    links = [link.get('href') for link in soup.select('a') if link.get('href')]
    http_links = [link for link in links if link.startswith('http')]

    broken_links = 0

    for link in http_links:
        result = requests.get(link)

        try:
            result.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f'Broken link: {link}')
            broken_links += 1

    print(f'Of the {len(links)} links found at {url}, {broken_links} links were broken.')


if __name__ == '__main__':
    verify_links('https://automatetheboringstuff.com/chapter11/')