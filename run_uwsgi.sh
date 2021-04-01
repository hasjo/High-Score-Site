uwsgi --http 0.0.0.0:8081 --module Site:app --master --processes 2 --threads 2
