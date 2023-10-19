# Increase the ULIMIT of the default file
exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => "test \"$(cat /etc/default/nginx | grep '15')\" != ''",
  require => Package['nginx'],  # Ensure nginx package is installed
}

# Restart Nginx
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => Exec['fix-for-nginx'],  # Subscribe to the previous exec
}
