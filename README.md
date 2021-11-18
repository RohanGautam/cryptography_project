untar firefox

```bash
tar -xvf firefox-38.0.5.tar.bz2
cd firefox
./firefox -no-remote
```

## Get certificate :

```
openssl s_client -showcerts -connect www.google.com:443 </dev/null
```

In a GCE instance,

```bash
sudo apt update && sudo apt -y install apache2 snapd




sudo systemctl status apache2
cd /etc/apache2
# sudo chmod +rw apache2.conf
sudo snap install core; sudo snap refresh core
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --apache # make sure to have a domain name with a proper A-record for resolving the DNS. It's crypto-project.xyz here
```

when setting up https, you should see something like :

```
Deploying certificate
Successfully deployed certificate for crypto-project.xyz to /etc/apache2/sites-available/000-default-le-ssl.conf
Congratulations! You have successfully enabled HTTPS on https://crypto-project.xyz
```

## refs

- https://www.tenable.com/plugins/nessus/84581
- https://github.com/concise/logjam-attack-poc
- https://download-installer.cdn.mozilla.net/pub/firefox/releases/38.0.5/linux-x86_64/en-US/
