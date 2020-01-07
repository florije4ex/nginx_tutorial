vagrant up

set local hosts:
127.0.0.1    proxy.com

curl http://proxy.com:8888/name/cp
will call server api: /cp

todo: will add rewrite rules.