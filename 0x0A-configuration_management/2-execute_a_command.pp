# this file kills the killmenow file.

exec{ 'pkill':
  command => 'pkill killnow',
  provider => 'shell',
}
