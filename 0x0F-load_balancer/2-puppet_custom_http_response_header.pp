#manifest that setup a custom HTTP header for web server

package {'install nginx':
  ensure   => 'installed',
  provider => 'apt',
}

exec {'allow http':
  command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

file_line {'custom header':
  ensure => 'present',
  path   => '/etc/nginx/nginx.conf',
  after  => 'http {',
  line   => "	add_header X-Served-By ${hostname};",
}

service {'nginx':
  ensure => running,
  enable => true
}
