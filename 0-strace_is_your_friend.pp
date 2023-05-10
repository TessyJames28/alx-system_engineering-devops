$file_path = '/var/www/html/wp-settings.php'
$file_contents = file($file_path)

$file_contents = replace($file_contents, /\.phpp'/, ".php'")

file { $file_path:
  ensure => file,
  content => $file_contents,
}
