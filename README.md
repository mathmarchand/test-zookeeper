# Simple way to sanity test ZooKeeper installation.
First install the dependencies:
```
python3 -m pip install -r requirements.txt
```
Then you just need to provide the host and the port in this format `hostname:port`
```
python3 test_zookeeper.py --host hostname:port
```
