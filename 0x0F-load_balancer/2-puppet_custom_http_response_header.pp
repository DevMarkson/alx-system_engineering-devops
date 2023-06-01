# Setup nginx server
package { 'nginx':
  ensure     => 'installed',
}

file_line { 'aaaaa':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}
file_line { 'b':
  ensure  => 'present',
  path    => '/etc/nginx/sites-available/default',
  after   => 'listen 80 default_server;',
  line    => 'add_header X-Served-By $HOSTNAME;',
  require => Package['nginx'],
}
file { '/var/www/html/index.html':
  content => 'Hello World!',
}
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
