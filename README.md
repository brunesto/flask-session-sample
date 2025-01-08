# flask-session-sample
small sample for flask session usage


```
  python -m venv .venv
  . .venv/bin/activate
  pip install -r requirements.txt
```

run with flask dev env
```
python -m flask  --app app2 run
# or
python app2
```


run with gunicorn
```
gunicorn -w 4 -b 0.0.0.0:5000 app2:app2

```

run with waitress
```
waitress-serve --host 0.0.0.0 --port 5000  app2:app2
```
