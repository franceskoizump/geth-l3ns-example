# geth_l3ns
[video](https://youtu.be/66gOaZyt0Qw)
1. Build images and start the lab
```
docker build -t eth .
python3 ./lab.py
```
docker logs -f MADT_eth_eth2
```
if you see generating DAG, everything is okey

2. Connect all nodes and check peers and blockNumber
```
docker exec -it node2 ./distr/connect.sh 4
docker exec -it node2 ./distr/check.sh
```

if you see json with info and block number are same, or increased with time, everything is okey
