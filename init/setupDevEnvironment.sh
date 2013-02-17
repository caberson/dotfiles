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