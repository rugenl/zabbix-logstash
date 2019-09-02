# zabbix-logstash

Monitor logstash pipelines and persistent queues with Zabbix 

Last tested on Logstash 6.8.2

Contents:

*  zabbix_stats.yml - Ansible task file to install host items
*  logstash-lld.xml - Zabbix template
*  files/*zsender - cron.d files
*  files/*.py - gather stats and lld information  
