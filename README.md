# EasyRDM
The Simple web GUI for redis, inspired by RDM(resp).

<img alt="example" src="https://user-images.githubusercontent.com/3334897/166682161-02bca328-e346-4608-8255-f8227fe9597b.png">

# Install

there ara three ways to install and run `EasyRDM`:

## By source code

Require python3.7+ installed
```bash
git clone https://github.com/taojy123/EasyRDM
pip install -r requirements.txt
python easyapp
```
Then, open brower and visit `http://127.0.0.1:8080`


## By docker image

Require docker installed
```bash
docker run --name easyrdm -p 8080:8080 -d --rm registry.cn-shanghai.aliyuncs.com/taojy123/easyrdm
```
Then, open brower and visit `http://127.0.0.1:8080`


## Use online public website

Direct open brower and visit `https://easyrdm.tslow.cn`

***warning:*** *the online version may pass your redis server information and data through the network, so don't use it in a production environment.*



# Quick start

1. Add your redis server
<img src="https://user-images.githubusercontent.com/3334897/166683729-cbc59c2e-274f-4aee-8cd4-74a69112965b.png">

2. Select a db
<img alt="image" src="https://user-images.githubusercontent.com/3334897/166684154-94fdeb0f-935c-4ead-a18f-d450eaa28534.png">

3. Search keys

4. Click on the key point in the tree you are interested

5. View the detail info of the key
<img width="1051" alt="image" src="https://user-images.githubusercontent.com/3334897/166684764-f375065a-f788-4de5-8aa0-3c59c62d8ac7.png">





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


