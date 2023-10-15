# fix extension
exec { 'replace-wordpress-variable':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-configuration.php',
  path    => '/usr/local/bin/:/bin/'
}
