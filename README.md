### Restaurant Booking Django Application

Usage:

```bash
pip install -r requirements.txt
cp restaurant_booking/settings-dist.py restaurant_booking/settings.py
# Add Facebook and Twitter key and secret to restaurant_booking/settings.py
touch db.sqlite3
python manage.py loaddata data.json
python manage.py migrate
python manage.py runserver
```