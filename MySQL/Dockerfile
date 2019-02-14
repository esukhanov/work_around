FROM mysql
COPY my.cnf /etc/mysql/my.cnf
COPY dbdump-mydb-201902141736.sql /etc/dbdump-mydb-201902141736.sql
RUN mysql -uroot -ppassword < /etc/dbdump-mydb-201902141736.sql