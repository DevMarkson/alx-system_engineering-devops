# Modify OS Security Configuration for Seamless Login and File Access

exec {'OS security config':
command => 'sed -i "s/holberton/foo/" /etc/security/limits.conf',
path => '/usr/bin/env/:/bin/:/usr/bin/:/usr/sbin/'
}