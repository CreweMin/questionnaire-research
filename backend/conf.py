# 用于处理mysql中文的存储
table_args = {
    'mysql_engine': 'InnoDB',
    'mysql_charset': 'utf8'
}
# 用于测试的服务器和端口，注意这里不能用http://
httpserver = "192.168.1.100"
httpport = "5100"

