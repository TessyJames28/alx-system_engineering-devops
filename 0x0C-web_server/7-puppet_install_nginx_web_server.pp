#setup nginx web server using puppet

package {'nginx':
ensure   => 'installed',
provider => 'apt'
}

file {'/var/www/html/index.html':
ensure  => file,
content => 'Hello World!
'
}

exec {'100 allow nginx':
command => '/usr/sbin/ufw allow "Nginx HTTP"'
}

file_line { 'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'root /var/www/html;',
  line   => 'rewrite ^/redirect_me https://www.digitalocean.com/community permanent;',
}

service {'nginx':
ensure => running,
enable => true
}
