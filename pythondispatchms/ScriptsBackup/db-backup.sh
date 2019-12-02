#!/bin/sh
/etc/init.d/apache2 stop
now="$(date +'%Y_%m_%d_%H_%M_%S')"
deletedate="$(date +'%Y-%m-%d')"
filename="db_backup_$now".gz
backupfolder="/home/wsgi/backups"
fullpathbackupfile="$backupfolder/$filename"
logfile="$backupfolder/"backup_log_"$(date +'%Y_%m')".txt
echo "mysqldump started at $(date +'%d-%m-%Y %H:%M:%S')" >> "$logfile"
mysqldump --user=gpscontrol --password=qazwsxedc --default-character-set=utf8 dispatch | gzip > "$fullpathbackupfile"
echo "mysqldump finished at $(date +'%d-%m-%Y %H:%M:%S')" >> "$logfile"
mysql --user=gpscontrol --password=qazwsxedc --database=dispatch --execute="delete from traffic where time_stamp<'${deletedate}';"
/etc/init.d/apache2 start
