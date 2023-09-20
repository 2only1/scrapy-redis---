1·请先配置好redis数据库
  这里使用的Redis-x64-3.0.504版本的
2·修改配置文件 redis.windows.conf 
  确保注释：# bind 127.0.0.1 =::1 
  确保关闭私有模式：protected-mode no
3·开启redis服务器
  F:\redis\Redis-x64-3.0.504\start-redis.bat
4·保证服务端和main端的python版本是一致的