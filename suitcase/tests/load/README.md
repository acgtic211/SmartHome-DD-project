* Create venv
```
python3 -m venv venv
```
* Activate venv
```
source ./venv/bin/activate
```
* Deactivate venv
```
deactivate
```

# Launch Locust
```
pip install locust
```

```
locust -f loadTesterDD.py --host=https://wot-lab.com
```