sudo su postgres
createuser --superuser --pwprompt --username postgres alaa2
chmod +x openerp-server
alaa2@:~/erp/odoo-7.0$ ./openerp-server --addons-path=./addons -s
http://localhost:8069

