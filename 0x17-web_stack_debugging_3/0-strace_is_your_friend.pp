# puppet script that fix 500 server error for  a GET method

file { 'replace':
  ensure   => file,
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
