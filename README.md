## Running the main simulation

- Install CADO-NFS, to `./cado-nfs` from their [gitlab](https://gitlab.inria.fr/cado-nfs/cado-nfs)

## Running firefox

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

when setting up https with Let's encrypt you should see something like :

```
Deploying certificate
Successfully deployed certificate for crypto-project.xyz to /etc/apache2/sites-available/000-default-le-ssl.conf
Congratulations! You have successfully enabled HTTPS on https://crypto-project.xyz
```

- edit `/etc/apache2/mods-available/ssl.conf`, adding the line `SSLProtocol -all +TLSv1` (remove(`-`) all and enable(`+`) only TLSv1 )
- edit `/etc/apache2/sites-available/000-default-le-ssl.conf`, adding the lines `SSLEngine on`, `SSLProtocol -all +TLSv1` (remove(`-`) all and enable(`+`) only TLSv1 )
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
- X.509 certificates for authentication are sometimes also called SSL Certificates/ server certs
- packet capture and analysis: `sudo wireshark`
- custom server ip: `35.239.113.22:443`, wireshark filder : `ip.addr == 35.239.113.22`
- `python mitmattack/driver.py`

# NFS:

- `./cado-nfs.py 90377629292003121684002147101760858109247336549001090677693 -t all > ../nfs_output.txt`

```bash
191907783019725260605646959711 # 98 bit prime
./cado-nfs.py -dlp -ell 101538509534246169632617439 target=129821646158317470002802307860 191907783019725260605646959711
```
