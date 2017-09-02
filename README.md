ispmail-admin
=============

A Django-based admin interface for <https://workaround.org/ispmail>.

```
git clone git@github.com:rfleschenberg/ispmail-admin
cd ispmail-admin
direnv allow  # optional

echo "create database ispmail" | mysql -u root
echo "create user 'ispmail'@'localhost' identified by 'ispmail'" | mysql -u root
echo "grant create on ispmail.* to 'ispmail'@'localhost'" | mysql -u root
echo "grant drop on ispmail.* to 'ispmail'@'localhost'" | mysql -u root
echo "grant create on test_ispmail.* to 'ispmail'@'localhost'" | mysql -u root
echo "grant drop on test_ispmail.* to 'ispmail'@'localhost'" | mysql -u root
echo "grant all privileges on ispmail.* to 'ispmail'@'localhost'" | mysql -u root
echo "grant all privileges on test_ispmail.* to 'ispmail'@'localhost'" | mysql -u root

python3.6 -m venv ~/.virtualenvs/ispmail-admin
source ~/.virtualenvs/ispmail-admin/bin/activate
pip install -r requirements.txt
./manage.py createsuperuser
```
