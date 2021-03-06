from datetime import datetime
import pytest
from sitemapparser.base_data import BaseData


class TestBaseData:
    def test_lastmod_value_correct(self):
        s1 = BaseData()
        s1.lastmod = '2019-12-01T01:33:35+00:00'

        s2 = BaseData()
        s2.lastmod = '2019-11-11'
        assert type(s1.lastmod) is datetime
        assert str(s1.lastmod) == '2019-12-01 01:33:35+00:00'
        assert type(s2.lastmod) is datetime
        assert str(s2.lastmod) == '2019-11-11 00:00:00'

    def test_lastmod_value_incorrect(self):
        s1 = BaseData()
        # tests invalid month value
        with pytest.raises(ValueError):
            s1.lastmod = '2019-13-01T01:33:35+00:00'

    def test_loc_value_correct(self):
        s1 = BaseData()
        s2 = BaseData()
        s1.loc = 'http://www.example.com'
        s2.loc = 'https://www.example.com/file.xml'

        assert s1.loc == 'http://www.example.com'
        assert s2.loc == 'https://www.example.com/file.xml'

    def test_loc_value_incorrect(self):
        s = BaseData()
        with pytest.raises(ValueError):
            s.loc ='www.example.com'



