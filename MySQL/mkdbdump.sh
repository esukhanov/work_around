#!/bin/bash
# ###
export DB_NAME='mydb'
export IP_ADDR='192.168.31.13'
# v_yr=`date +%Y`; v_mo=`date +%m`; v_dd=`date +%d`
v_dt=`date +%Y%m%d%H%M`; dumpfilename=dbdump-${DB_NAME}-${v_dt}.sql
# echo ������� ����������� ����: ${v_yr}${v_mo}${v_dd}, v_dt=${v_dt}
# echo ��� ����� �����: $dumpfilename
SQLOPTIONS="--add-drop-table -CRcq --create-options --single-transaction --dump-date --triggers"
# ���������� ������� ������� ����� ��:
mysqldump -r${HOME}/sqldump/${dumpfilename} ${SQLOPTIONS} -h${IP_ADDR} -uroot -ppassword ${DB_NAME}
echo "mysqldump complete"
# ������ ��� � 10:
echo "Compressing the ${HOME}/sqldump/${dumpfilename}..."
gzip -9 ${HOME}/sqldump/${dumpfilename}
echo "Done!"
# *** Done! ***
