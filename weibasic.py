#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from requests.auth import HTTPBasicAuth

SOURCE = 0000000000  # replace to your APP_KEY


class ApiClient(object):

    def __init__(self, username, password):  # init with your Weiboaccount
        self.source = SOURCE
        self.auth = HTTPBasicAuth(username, password)
        self.base_url = "https://api.weibo.com/2/"
        self.json_url = "https://api.weibo.com/2/%s.json"  # API v2 address

    def __getattr__(self, attr):
        return _Callable(self, attr)

    def http_call(self, method, path, **params):
        if method == 'get':
            params['source'] = self.source
            req = requests.get(self.json_url %
                               path, params=params, auth=self.auth) # reference http://open.weibo.com
            return req.json()
        if method == 'post':
            params['source'] = self.source
            req = requests.get(self.json_url %
                               path, data=params, auth=self.auth)
            return req.json()


class _Callable(object):

    def __init__(self, client, name):
        self._client = client
        self._name = name

    def __getattr__(self, attr):
        if attr == 'get':
            return _Executable(self._client, attr, self._name)
        if attr == 'post':
            return _Executable(self._client, attr, self._name)
        name = '%s/%s' % (self._name, attr)
        return _Callable(self._client, name)

    def __str__(self):
        return '_Callable (%s)' % self._name

    __repr__ = __str__


class _Executable(object):

    def __init__(self, client, method, path):
        self._client = client
        self._method = method
        self._path = path # API path 

    def __call__(self, **kw):
        if self._method == 'get':
            data = self._client.http_call('get', self._path, **kw)
            return data
        if self._method == 'post':
            data = self._client.http_call('post', self._path, **kw)
            return data
        else:
            pass

    def __str__(self):
        return '_Executable (%s %s)' % (self._method, self._path)

    __repr__ = __str__

if __name__ == '__main__':
    pass
