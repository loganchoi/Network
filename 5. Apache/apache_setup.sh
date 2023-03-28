#!/bin/bash

# Install
# This part will be done for you on the gitlab-ci.
# You may do it manually on your VM.

## Fedora
# sudo dnf install httpd
# Enable incoming http/https using firewall GUI

## Debain
# sudo apt install apache2
# Use gufw or ufw to enable incoming http/https

echo "Runing on:"
cat /etc/os-release

if grep 'docker\|lxc' /proc/1/cgroup >/dev/null 2>&1; then
    # Debian-like remote docker machine (CI/CD pipeline)
    # Enable and start Apache
    service apache2 start
    a2enmod cgid
    service apache2 restart

    # Get the goal_files/ in the right place to be served:
    chmod -R 777 /var/www/html
    cp goal_files/* /var/www/html
    cp scripts/* /usr/lib/cgi-bin
    cp -r goal_files/dir /var/www/html

else
    # Enable and start Apache on your local machine
    # (for easier development)
    if grep Fedora </etc/os-release &>/dev/null; then
        echo.

    elif grep Debian </etc/os-release &>/dev/null; then
        # Enable and start Apache
        sudo service apache2 start
        sudo a2enmod cgid
        sudo service apache2 restart

        #Get the goal_files/ in the right place to be served:
        sudo chmod -R 777 /var/www/html
        sudo cp goal_files/* /var/www/html
        sudo cp scripts/* /usr/lib/cgi-bin
        sudo cp -r goal_files/dir /var/www/html
        : # Delete this line and write your code
    fi
fi
