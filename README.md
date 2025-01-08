# flask-session-sample
small sample for flask session usage


### setup
```bash
  python -m venv .venv
  . .venv/bin/activate
  pip install -r requirements.txt
```

### switch to server-side storage
To switch from client-side storage (i.e. cookies) to server-side, add these statements after app configuration 
```python
  from flask_session import Session
  app2.config['SESSION_TYPE'] = 'filesystem'
  server_session = Session(app2)
```


### run with flask dev env
```bash
python -m flask  --app app2 run
# or
python app2
```


### run with gunicorn
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app2:app2

```

### run with waitress
```bash
waitress-serve --host 0.0.0.0 --port 5000  app2:app2
```
