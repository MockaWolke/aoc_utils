import http.client
import urllib.parse
import http.cookiejar
import datetime
import os
from .utils import validate_date
from typing import Optional

def get_aoc_input(day: Optional[int] = None, year: Optional[int] = None):
    
    
    date : datetime.date = validate_date(day = day, year = year)
    
    
    
    session_cookie = os.environ.get("AOC_SESSION")
    if session_cookie is None:
        raise ValueError("Please set the AOC_SESSION environment variable!")
        

    url = f"https://adventofcode.com/{date.year}/day/{date.day}/input"
    parsed_url = urllib.parse.urlparse(url)
    
    cookie_jar = http.cookiejar.CookieJar()
    cookie = http.cookiejar.Cookie(
        version=0, name='session', value=session_cookie, port=None, port_specified=False,
        domain='adventofcode.com', domain_specified=True, domain_initial_dot=False, path='/',
        path_specified=True, secure=True, expires=None, discard=True, comment=None,
        comment_url=None, rest={}, rfc2109=False
    )
    cookie_jar.set_cookie(cookie)

    conn = http.client.HTTPSConnection(parsed_url.netloc)
    
    headers = {
        'Cookie': f'session={session_cookie}'
    }

    conn.request("GET", parsed_url.path, headers=headers)
    response = conn.getresponse()
    
    if response.status != 200:
        raise http.client.HTTPException(f"Could not load AOC input, HTTP status code: {response.status}")
    
    data = response.read().decode('utf-8')

    conn.close()
    
    return data
