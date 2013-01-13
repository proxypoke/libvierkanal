# Author: slowpoke <mail+git@slowpoke.io>
#
# This program is Free Software under the terms of the
# Do What The Fuck You Want To Public License.

'''Functions to get proper URLs for everything.

This module contains templates for all relevant URLs on 4chan, for
both http and https. Currently, they have to be formatted manually, but this is
supposed to change in the future.
'''

# url templates
_url = {"board": "http://boards.4chan.org/{board}/",
        "index": "http://boards.4chan.org/{board}/{index}",
        "thread": "http://boards.4chan.org/{board}/res/{no}",
        "reply": "http://boards.4chan.org/{board}/res/{resto}#{no}",
        "image": "http://images.4chan.org/{board}/src/{tim}.{ext}",
        "thumb": "http://thumbs.4chan.org/{board}/thumb/{tim}s.jpg",
        "customspoiler":
        "http://static.4chan.org/image/spoiler-{board}{custom_spoiler}.png"
        }
for key, value in _url.items():
    globals()[key] = value


# https versions of the above urls
_urls = dict((k, v.replace("p", "ps", 1)) for k, v in _url.items())
for key, value in _urls.items():
    globals()[key + 's'] = value
