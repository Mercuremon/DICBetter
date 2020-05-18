import re
import os
import json
import time
import requests
import mechanize
import HTMLParser
from cStringIO import StringIO


def upload():
    url = "http://115.29.204.44/dic.html"
    s = requests.session()
    response = s.get(url)
    forms = mechanize.ParseFile(StringIO(response.text.encode('utf-8')), url)
    form = forms[-1]
    # form.find_control('file_input').add_file(open(new_torrent), 'application/x-bittorrent',
    #                                          os.path.basename(new_torrent))
    # if torrent['remastered']:
    #    form.find_control('remaster').set_single('1')
    print form
    # form['remaster_year'] = str(1984)
    # form['remaster_title'] = 'cool'
    # form['remaster_record_label'] = 'fuck'
    # form['remaster_catalogue_number'] = 'you'
    # form.find_control('format').set('1', 'FLAC')
    # form.find_control('bitrate').set('1', '320')
    # form.find_control('media').set('1', 'WEB')
    # form['release_desc'] = 'FUCK YOU MAN'
    #
    # _, data, headers = form.click_request_data()
    # return s.post(url, data=data, headers=dict(headers))

print upload()