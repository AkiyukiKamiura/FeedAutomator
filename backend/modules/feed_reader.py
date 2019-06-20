import urllib
import xml.etree.ElementTree as ET

from backend import db
from backend.models import Feed, Entry

import datetime

class FeedReader:
    def __init__(self):
        self.target_url = None
        self.xml_root = None
        self.entries = []
        self.feed_id = None

    def init_feed(self, feed_id):
        feed = Feed.query.get(feed_id)
        if feed is None:
            print('存在しない id を指定しています。')

        self.feed_id = feed.id
        self._fetch(feed.url)

    def to_entries(self):
        if self.target_url == None: print('fetch url first')

        if self.target_url.startswith('https://www.google.co.jp/alerts/feeds'):
            self.entries = self._google_alert_to_entries()

    def save_entries(self):
        if self.target_url == None:
            print('fetch url first')
            return None

        if self.feed_id is None:
            print('set feed first')
            return None

        for _ent in self.entries:
            if len(Entry.query.filter(Entry.url==_ent['url']).all()) != 0:
                print("{title} はすでに取得済み！".format(title=_ent['title']))
                continue

            entry = Entry()
            entry.title = _ent['title']
            entry.url = _ent['url']
            entry.published = _ent['published']
            entry.content = _ent['content']
            entry.feed_id = self.feed_id

            db.session.add(entry)
            db.session.commit()

            print("{title} を取得完了！".format(title=_ent['title']))

    def _fetch(self, url):
        self.target_url = url
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            xml_data = response.read().decode('utf-8')
            self.xml_root = ET.fromstring(xml_data)

    def _google_alert_to_entries(self):
        if len(self.xml_root) < 4: return []

        _entries = []
        for i in range(4, len(self.xml_root)):
            entry = {}
            entry['title'] = self.xml_root[i][1].text
            entry['url'] = self.xml_root[i][2].attrib['href']
            entry['published'] = datetime.datetime.strptime(self.xml_root[i][3].text, '%Y-%m-%dT%H:%M:%SZ')
            entry['content'] = self.xml_root[i][5].text
            _entries.append(entry)
        return _entries
