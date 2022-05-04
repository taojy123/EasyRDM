# EasyRDM
The simple web GUI for redis, inspired by RDM(resp).

<img width="1000" src="https://user-images.githubusercontent.com/3334897/166682161-02bca328-e346-4608-8255-f8227fe9597b.png">

online website demo:
https://easyrdm.tslow.cn


# Install

there ara three ways to install and run `EasyRDM`:

### By source code

Require python3.7+ installed
```bash
git clone https://github.com/taojy123/EasyRDM
pip install -r requirements.txt
python easyapp
```
Then, open brower and visit `http://127.0.0.1:8080`


### By docker image

Require docker installed
```bash
docker run --name easyrdm -p 8080:8080 -d --rm registry.cn-shanghai.aliyuncs.com/taojy123/easyrdm
```
Then, open brower and visit `http://127.0.0.1:8080`


### Use online public website

Direct open brower and visit `https://easyrdm.tslow.cn`

***warning:*** *the online version may pass your redis server information and data through the network, so don't use it in a production environment.*



# Quick start

1. Add your redis server
<img width="780" src="https://user-images.githubusercontent.com/3334897/166685223-43a2bdd0-045f-452f-9dde-edbe9900c6df.png">
2. Select a db
<img width="780" src="https://user-images.githubusercontent.com/3334897/166685291-81cc5b21-1ca2-4d10-b05c-2d3df901089b.png">
3. Search keys

4. Click on the key point in the tree you are interested

5. View the detail info of the key
<img width="780" src="https://user-images.githubusercontent.com/3334897/166685338-72f9f097-205c-4c2d-97cc-216e6147e071.png">



# Todo list:
- create string key
- create list key
- create hash key
- create set key
- create zset key
- modify string key
- modify list key
- modify hash key
- modify set key
- modify zset key
- view value of string key by json format
- view value of list/hash/set/zset key by a single textarea
- connect by ssh tunnel


