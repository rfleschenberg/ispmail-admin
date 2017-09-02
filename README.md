ispmail-admin
=============

A Django-based admin interface for <https://workaround.org/ispmail>.

```
git clone git@github.com:rfleschenberg/ispmail-admin
cd ispmail-admin
direnv allow  # optional
sudo -u postgres createuser -d ispmail
sudo -u postgres createdb ispmail -O ispmail
echo "alter role \"ispmail\" password 'ispmail';"|sudo -u postgres psql
python3.6 -m venv ~/.virtualenvs/ispmail-admin
source ~/.virtualenvs/ispmail-admin/bin/activate
pip install -r requirements.txt
```
