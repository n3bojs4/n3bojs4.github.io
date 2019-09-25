---
layout: post
title: 'SNMP my love'
description: "Petit usecase zabbix sur un chassis HP"
comments: true
keywords: "snmp, zabbix, monitoring, système"
author: nebo
---

Dans le cadre de la mise en place de zabbix en tant que monitoring, j'ai du résoudre un certains nombres de problèmes.

J'avais à monitorer un chassis C7000 HP, j'ai donc utilisé le template disponible sur le site de zabbix ( [lien vers le template](https://zabbix.org/mw/images/e/eb/HP_C7000.zip) ).
Ce template a été écrit par un russe (Vladimir Marakshin) j'ai donc eu à modifier quelques valeurs et à ajouter des mappings dans la section Value Mapping (voir le readme dans le zip).
Malgré tout ça j'avais des erreurs de type "**snmp_parse_oid(): Cannot parse OID cpqRackPowerEnclosureRedundant**"

Pour résoudre ce problème j'ai édité les items afin d'ajouter le bon OID correspondant.
Pour cela j'ai utilisé snmpget en m'appuyant sur la MIB HP CPQRACK  (voir [ce lien](http://www.oidview.com/mibs/232/CPQRACK-MIB.html) )

```
snmpget -v 2c -c YourCommunity 192.168.1.254 1.3.6.1.4.1.232.22.2.3.1.1.1.8.1

SNMPv2-SMI::enterprises.232.22.2.3.1.1.1.8.1 = STRING: "4.85"
```

Dans cet exemple on retourne la version de firmware du chassis : **4.85**.

J'ai fait la modification pour trouver l'état de l'alimentation de secours (voir ci-dessous).

[![Capture Zabbix](/assets/images/capture_zabbix.png)](/assets/images/capture_zabbix.png)
