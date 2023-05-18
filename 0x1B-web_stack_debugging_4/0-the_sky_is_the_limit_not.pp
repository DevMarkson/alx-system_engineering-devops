# code to fix nginx to accept and serve more requests
exec { 'fix--for-nginx':
  path    => '/usr/local/bin/:/bin/'
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
} ->

# code to restart Nginx
exec { 'nginx-restart':
  path    => '/etc/init.d/'
  command => 'nginx restart',
}