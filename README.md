### dispatch 1.0 ###

## How to Install Apache WSGI with Turbo Gears
0. Install enchant: 
    sudo apt-get install libenchant1c2a
    sudo apt-get install myspell-es
    pip install pyenchant
    >>> import enchant
    >>> d=enchant.Dict("es")
    >>> d.check("Hola")
    True
    >>> d.check("Hello")
    False

1. Install Apache2 with user jorge  
  https://www.digitalocean.com/community/tutorials/how-to-install-the-apache-web-server-on-ubuntu-16-04
  
2. In the server install mod WSGI
    ```
    sudo apt install apache2-dev 
    sudo apt-get install libapache2-mod-wsgi
    rm /usr/lib/apache2/modules/mod_wsgi.so
    ```
      
    To find new releases: https://github.com/GrahamDumpleton/mod_wsgi/releases  
    Update to the newest:

    ```
    sudo apt-get install libtool    
    cd /tmp    
    wget https://github.com/GrahamDumpleton/mod_wsgi/archive/4.5.15.tar.gz    
    tar xvzf 4.5.15.tar.gz    
    cd mod_wsgi-4.5.15/
    ./configure    
    make    
    sudo cp /tmp/mod_wsgi-4.5.15/src/server/.libs/mod_wsgi.so /usr/lib/apache2/modules/.   
    sudo chmod 644 /usr/lib/apache2/modules/mod_wsgi.so
    ``` 
3.  Create a virtualenvironment with the specific TurboGears version your application depends on installed
    ```
    virtualenv /var/tg2env
    /var/tg2env/bin/pip install  tg.devtools
    ```
4. Activate the virtualenvironment
    ```
    source /var/tg2env/bin/activate
    (tg2env)$ #virtualenv now activated
    ```
5. Install your TurboGears application.
    ```
    cd /var/www/python.dispatch
    python setup.py develop
    ```
6. Within the application director, create a script named app.wsgi. Give it these contents:
    ```
    import os
    os.environ['PYTHON_EGG_CACHE'] = '/home/jorge/.python-eggs'
    APP_CONFIG = "/var/www/python.dispatch/production.ini"
    import logging.config
    logging.config.fileConfig(APP_CONFIG)
    from paste.deploy import loadapp
    application = loadapp('config:%s' % APP_CONFIG)
    ```
    create user jorge
    usermod -a -G www-data jorge
    
    54ayXLZoTxHJ
    
7. Change permisions  
    ```    
    sudo chown -R www-data:www-data /var/www
    sudo chmod go-rwx /var/www
    sudo chmod go+x /var/www
    sudo chgrp -R www-data /var/www
    sudo chmod -R go-rwx /var/www
    sudo chmod -R g+rx /var/www
    sudo chmod -R g+rwx /var/www
    
    #### IMPORTANT!!
    
    sudo chgrp -R www-data /home/jorge/.python-eggs
    sudo chown www-data:www-data /home/jorge/.python-eggs

    ```

8. Edit your Apache configuration and add some stuff.
    ```
    vim /etc/hosts
    ```
    Add The following line
     165.227.3.58 dispatch.dwim.mx
    ``` 
    cd /etc/apache2
    vim apache2.conf
    ```
    Add the Following line:
        ServerName dispatch.dwim.mx
    ```    
    cd /etc/apache2/sites-available
    rm *    
    sudo vim dispatch.dwim.mx.conf
    ```
    
    Insert the following lines:
    
        <VirtualHost *:80>
            ServerName dispatch.dwim.mx
            WSGIProcessGroup dispatch.dwim.mx
            WSGIDaemonProcess dispatch.dwim.mx user=www-data group=www-data threads=4 python-path=/var/tg2env/lib/python2.7/site-packages
            WSGIScriptAlias / /var/www/python.dispatch/app.wsgi
            #Serve static files directly without TurboGears
            Alias /images /var/www/python.dispatch/pythondispatch/public/images
            Alias /css /var/www/python.dispatch/pythondispatch/public/css
            Alias /js /var/www/python.dispatch/pythondispatch/public/js
            ErrorLog ${APACHE_LOG_DIR}/error.log
            CustomLog ${APACHE_LOG_DIR}/access.log combined
        </VirtualHost>
        WSGIPythonHome /var/tg2env
        WSGIPythonPath /var/tg2env/lib/python2.7
    ```
9. Start the Service
    ```
    * To enable WSGI
    sudo a2enmod wsgi
    * To enable site
    sudo a2ensite dispatch.dwim.mx.conf
    Enabling site Enabling site c4neza.dwim.space.
To activate the new configuration, you need to run:
  service apache2 reload
To activate the new configuration, you need to run:
  service apache2 reload
    (After this will appear in "sites-enabled")
    sudo service apache2 restart
    ```
   	
10. Give access to users to /var/log/apache2
    ```     
    adduser maria
    sudo usermod -aG sudo maria
    sudo usermod -aG adm maria
    ```
    
11. Custom Roller Theme
```
http://jqueryui.com/themeroller/#!zThemeParams=5d000001003006000000000000003d8888d844329a8dfe02723de3e5701dc2cb2be0d98fe676bb46e85f3b85ff2d347a9c5170a6c17a4a3d926b08b9d199c4e573fcbf9cc1a2dd092a9d80b65cc27a41c959e1c11c3f58747718755b7fc90eb73b9c06df29f308cd293b47a7ab61c1e5e9b99171b192d897cd71287aad2ba0f6393f9ad3ac85395b3d3818c28974be44c68b979fcec5140b900159d382f1a789f53fbd60fbdd8851bdbcf235a486045816d68270740cf98cfa8009617251f7fcf1ed1ad6732d278d788b18bcd882c4c2f7cfcb4453cae17f5499b5b9ae9f69d2f3fc541fa3b965f8939bdd65648a10903edc87b500d0f0589259cb74c8121b6ac789caaf5aca0f6cff9958dd61985507dc8ff86d0487ebe60b9bf788ea766b906e5015a29a1de793b425fc9924dd40d652089899e0e6088f7c030f4d294c1aa74d40fc26175b8da7ea5248cf617e160d8867d1579a097339af428c66e2bf6ef086a03b8b0e08ee4dd400bb7b81914759a4a221cc0969a50dee87b9903363ff95696b0a09671a15c2985d8c1df652c8a9ea5b8c4cf0b4e2fc7b6b58461ccf81e77983193af0e8baf89a5f884fa7b15e31659a1c25f7e4fed8ae268b7f6db23451823a63d0c26fbdde6c90ce6fefe28b95b7b16ad0b5467eb3e746c934ddf080d47bcf3e499cd95062fb1b600c2b8cdd91166e257bc6cd61d6e24f83b780675fc96d078f0228ea02ccea38fff16c4a52
 ```
 
 
 http://instala.dwim.mx/getuuidbyimei/861693035102268
 http://instala.dwim.mx/printinstallpdf/uuid:79fba5d4-a795-4011-b964-aebf174a50a4
 http://ci.dwim.mx/getuuidbyimei/862951028920271
 http://ci.dwim.mx/printinstallpdf/uuid:2b005564-77df-45bb-9f7a-b09026b03ba0
 
 
 12
 ```
mysql -u root -p
Capture when prompted password=Dwimserver9
CREATE USER 'gpscontrol'@'localhost' IDENTIFIED BY 'qazwsxedc';
GRANT ALL PRIVILEGES ON * . * TO 'gpscontrol'@'localhost';
exit
mysql -u gpscontrol -p
password: qazwsxedcv 
create database gpscontrol;
exit

Export commands in source machine:  
mysqldump -u gpscontrol -p dispatch  > backup.sql  
To copy backup file from one machine to another  
scp -p backup.sql root@192.237.253.49:.  
Import commands in destination machine:  
mysql -u gpscontrol -p -D dispatch < newtables.sql  

  
 ```




https://dispatch.dudewhereismy.mx/services/listjson
```
{  
   "planet_name":"dispatch",
   "error":"ok",
   "lista":[  
      {  
         "name":"Traffic",
         "url":"https://sun.dudewhereismy.mx/secc/traffic",
         "perm":"View Traffic",
         "observations":"None"
      }
   ]
}
```
https://dispatch.dudewhereismy.mx/services/treeOfdispatch
```
{  
   "lista":[  
      {  
         "sons":[  
            {  
               "sons":"",
               "name":"Alert Traffic",
               "url":"https://sun.dudewhereismy.mx/secc/traffic",
               "description":"Watch Alert Traffic from the platforms",
               "id":300
            }
         ]
      }
```
