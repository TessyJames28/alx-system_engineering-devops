#manifest that setup a custom HTTP header for web server

package {"haproxy":
ensure   => "installed",
provider => "apt"
}

exec {"nginx header":
command  => '/usr/sbin/ufw allow "Nginx HTTP"'
}

file_line {"custom header":
ensure   => "present",
path     => "/etc/nginx
after    => "sendfile on",
line     => "	add_header X-Served-By $(hostname);"
}

service {"nginx":
ensure   => "running",
enable   => true
}
