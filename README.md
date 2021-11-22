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

- edit `apache2/mods-available/ssl.conf`, adding the line `SSLProtocol -all +TLSv1` (remove(`-`) all and enable(`+`) only TLSv1 )
- edit `apache2/sites-available/000-default-le-ssl.conf`, adding the lines `SSLEngine on`, `SSLProtocol -all +TLSv1` (remove(`-`) all and enable(`+`) only TLSv1 )
- make same changes as above to `/etc/letsencrypt/options-ssl-apache.conf.`

## refs

- https://www.tenable.com/plugins/nessus/84581
- https://github.com/concise/logjam-attack-poc
- https://download-installer.cdn.mozilla.net/pub/firefox/releases/38.0.5/linux-x86_64/en-US/

## Tricks:

- search all files in a folder for a keyword: `grep -rnw '/etc/apache2' -e 'SSLProtocol'` ([ref](https://stackoverflow.com/a/16957078/6274300))
- restart and view status : `sudo systemctl restart apache2 && sudo systemctl status apache2`

## Research:

- https://docs.mitmproxy.org/stable/ proxy for mitm attacks and intercepting requests. From
  - `sudo mv mitmproxy-ca-cert.pem /usr/local/share/ca-certificates/mitmproxy.crt`
  - `sudo update-ca-certificates`
  - Install and upload certificate to firefox (http://mitm.it/#Firefox)
