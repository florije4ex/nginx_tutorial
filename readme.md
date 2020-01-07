vagrant up
vagrant ssh

sudo cp /vagrant/proxy.conf /etc/nginx/sites-available/proxy.conf
sudo ln -sf /etc/nginx/sites-available/proxy.conf /etc/nginx/sites-enabled/proxy.conf

sudo service nginx reload

set local hosts:
127.0.0.1    proxy.com

curl http://proxy.com:8888/name/cp