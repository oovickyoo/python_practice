# -*- coding: UTF-8 -*-
import urllib2
__author__ = 'vicky.han'


def test():
    url = 'http://l-ugcweb.h.beta.cn0.qunar.com:8080/api/h/jiuquan_3156/detail/rank/v1/page/1'
    f = urllib2.urlopen(url)
    response = f.read()
    print(response)

if __name__ == '__main__':
    test()



'http://www.duokan.com/store/v0/web/book/id_list?ids=ecfd74ff607446e79f58faae3e174d18%2C9791be7dd57d4985b497674630d5f015%2C3e234c4839844b378d580e1dbcce84c2%2C482f7ea6d4b74ba29dbbeb8608fe592d%2C25ef12d87d9b4e5fac7cf2e908cb7491%2C8c8fbd740da143b78abe75bc9cd88d77%2C987eb177bf7e47129df6e563302de08c%2Ce19dcc6235da4b149e283c2a4e03556b%2C482ed95631694bf5bb33b8c44d481156%2C4d4570c524fb495bbbe8e9b3ca05e273%2C1ba63e5ab8db4fd1bf062ebcd8b4e6d1%2C673434293250429e8eccc590e4068741%2Cabcbe90283bc45d49e08b5e379039479%2Cfc286261b9b04518b1ca46aaeea7bed2%2C5ca8a35067594a9a9c8a4c306b5676e9%2C61401a960c7d4a66a9f1db52471516b2%2C9e27b54ce81c403bb1d5fc1dab300847&all=1'
'http://www.duokan.com/store/v0/web/book/id_list?all=1'