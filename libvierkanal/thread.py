# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the terms of the
# Do What The Fuck You Want To Public License.

'''Handles threads on 4chan.'''

import requests


class Thread(dict):
    '''Representation of a single thread.'''

    def __init__(self, board, json_thread):
        super().__init__(self, json_thread)

    def __hash__(self):
        return self['no']


def get_threads(board, page=None):
    '''Get threads from a board.

    If page is specified, get that page's threads. Else get all (page=None).
    '''
    if page is None:
        url = "http://api.4chan.org/{0}/catalog.json".format(board)
    else:
        url = "http://api.4chan.org/{0}/{1}.json".format(board, page)

    content = requests.get(url).json()

    threads = []
    if page is None:
        for page in content:
            threads.extend(page['threads'])
    else:
        threads = content['threads']

    return [Thread(t) for t in threads]


def check404(url):
    '''Check if a thread is still alive.'''
    req = requests.get(url)
    if req.status_code == 404:
        return True
    return False
