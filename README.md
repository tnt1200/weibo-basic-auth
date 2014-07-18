Weibo Basic Authentication
================

A warpper class of sina weibo api based on basic authentication

## Requirement

* [requests](http://docs.python-requests.org/en/latest/)

## Basic Usage
Edit weibasic.py, change SOURCE to your app_key

```
from weibasic import ApiClient

client = ApiClient(weibo_username,weibo_password)
client.statuses.home_timeline.get()
```

## API reference

[weibo api document](http://open.weibo.com/wiki/微博API)