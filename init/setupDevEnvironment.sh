username=$(whoami)
echo $username

read -d '' userConf <<EOF
<Directory "/Users/${username}/Sites/">
	Options Indexes MultiViews
	AllowOverride All
	Order allow,deny
	Allow from all
</Directory>
EOF

sudo touch  "/etc/apache2/users/${username}.conf" 
echo "$userConf" | sudo tee /etc/apache2/users/${username}.conf  


# Enable user apache folder
mkdir -p ~/Sites

sudo apachectl start


# Install python PIP
echo "You should install python PIP"
# curl -o get-pip.py 'https://bootstrap.pypa.io/get-pip.py'
# python get-pip.py
