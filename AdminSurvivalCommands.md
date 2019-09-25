---
title: Admin Survival Commands
layout: default
comment: true
---
## Catégories:
--------------
 >* [Git](#git)
   * [Auth](#gitauth)
   * [Tag](#gittag)
 * [Shell](#shell)
 * [SGBD](#sgbd)
   * [Mysql/Postgresql](#mysqlpostgresql)
 * [Openssl](#openssl)
   * [Centos](#centos)
 * [Windows](#windows)
   * [Powershell](#powershell)
 * [Docker](#docker)
   * [Proxy](#dockerproxy)


### Git <a id="git">
------

#### Auth <a id="gitauth">
-------------------------


Sauvegarder son authentification : 
```bash
git config --global credential.helper cache
```

#### Tag <a id="gittag">
------------------------

ajouter un tag : 
```bash
    git tag -a v1.0 -m 'version 1.0'

    git commit -a -m 'add tag'

    git push origin v1.0
```

### Shell <a id="shell">
--------

`ctrl + R` : Rechecher dans l'historique des dernieres commandes

`ctrl + E` / `ctrl+A` : Aller au debut ou a la fin de la ligne

`esc + .` : Coller le dernier argument de la derniere commande

`esc + #` : Commenter la ligne actuelle

`ctr + D / ctrl + W` : Effacer des mots

### SGBD <a id="sgbd">

#### MySQL/Postgresql (équivalences) <a id="mysqlpostgresql">


| Action           | MySQL           | Postgresql |
|------------------|-----------------|------------|
|lister les bases  |`show databases;`|`\l`        |
|lister les tables | `show tables ;` | `\dt` |
|décrire une table | `describe tablename;` | `\d tablename` |


### Openssl <a id="openssl">
----------

#### Centos 7 <a id="centos">

- ajouter une CA :

```bash

yum install ca-certificates

cp foo.crt /etc/pki/ca-trust/source/anchors/

update-ca-trust extract
```
 
### Windows <a id="windows">
-----------

#### PowerShell <a id="powershell">

- CRC check :

Sha256 : 
```powershell 
Get-FileHash .\filename.iso -Algorithm SHA256 | Format-List
``` 

### Docker

#### Proxy

Déclarer un proxy pour le client docker:

```bash
mkdir /etc/systemd/system/docker.service.d
vi /etc/systemd/system/docker.service.d/http-proxy.conf
systemctl daemon-reload
systemctl restart docker
```

```vim
# /etc/systemd/system/docker.service.d/http-proxy.conf
[Service]
Environment="HTTP_PROXY=http://xx.xx.xx.xx:xxxx/"
Environment="HTTPS_PROXY=http://xx.xx.xx.xx:xxxx/"
```

