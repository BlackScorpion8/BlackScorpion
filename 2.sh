#!/bin/bash

export payload="allShortcutsEnabled:false"

# 卸载防火墙规则
echo "卸载防火墙规则..."
sudo iptables -F
sudo iptables -X
sudo iptables -t nat -F
sudo iptables -t nat -X
sudo iptables -t mangle -F
sudo iptables -t mangle -X
sudo iptables -P INPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -P OUTPUT ACCEPT

# 安装Dante SOCKS5服务器
echo "安装Dante SOCKS5服务器..."
sudo apt-get update
sudo apt-get install -y dante-server

# 配置Dante服务器
echo "配置Dante服务器..."
cat <<EOL | sudo tee /etc/danted.conf
logoutput: /var/log/socks.log
internal: eth0 port = 50088
external: eth0

method: none

client pass {
        from: 0.0.0.0/0 to: 0.0.0.0/0
}
pass {
        from: 0.0.0.0/0 to: 0.0.0.0/0
        command: bind connect udpassociate
}
EOL

# 启动Dante服务器
echo "启动Dante服务器..."
sudo systemctl start danted

# 设置Dante服务器开机自启动
echo "设置Dante服务器开机自启动..."
sudo systemctl enable danted

# 检查Dante服务器状态
echo "检查Dante服务器状态..."
sudo systemctl status danted

echo "Dante SOCKS5服务器已安装和配置，端口设置为50088
