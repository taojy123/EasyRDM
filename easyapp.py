import redis

import bottle
from bottle import route, run, template, request
from utils import handle_keys


@route('/')
def index():
    # bottle.TEMPLATES.clear()
    # return template('index', **locals())
    return open('index.html').read()


@route('/search_keys')
def search_keys():

    host = request.params.host
    port = request.params.port
    password = request.params.password
    by_ssh = request.params.by_ssh
    ssh_host = request.params.ssh_host
    ssh_port = request.params.ssh_port
    ssh_user = request.params.ssh_user
    ssh_password = request.params.ssh_password
    db = request.params.db
    search = request.params.search or ''

    redis1 = redis.Redis(
        host=host,
        port=port,
        password=password,
        db=db,
        decode_responses=True,
        socket_timeout=5,
    )

    pattern = '*' + search + '*'
    print(pattern)

    try:
        # keys = redis1.keys(pattern=pattern)
        keys = []
        cursor = 0
        while True:
            cursor, skeys = redis1.scan(cursor=cursor, match=pattern, count=1000)
            print('scan', cursor, len(skeys))
            keys += skeys
            if not cursor:
                break
    except Exception as e:
        return {'error': str(e)}

    print(keys[:10])
    # keys = ['aa:bb:cc', 'xx:yy', 'aa:bb:dd']
    # keys.sort()

    result_keys = handle_keys(keys)

    return {'keys': keys, 'result_keys': result_keys}


@route('/get_dbs')
def get_dbs():

    host = request.params.host
    port = request.params.port
    password = request.params.password
    by_ssh = request.params.by_ssh
    ssh_host = request.params.ssh_host
    ssh_port = request.params.ssh_port
    ssh_user = request.params.ssh_user
    ssh_password = request.params.ssh_password

    dbs = []
    for i in range(8):
        redis1 = redis.Redis(
            host=host,
            port=port,
            password=password,
            socket_timeout=3,
            db=i
        )
        try:
            count = redis1.dbsize()
        except:
            break
        dbs.append({
            'id': i,
            'title': f'db{i} ({count})',
        })
    if not dbs:
        dbs.append({
            'id': 0,
            'title': 'connect fail',
        })
    return {'dbs': dbs}


@route('/test_connection')
def test_connection():
    host = request.params.host
    port = request.params.port
    password = request.params.password
    by_ssh = request.params.by_ssh
    ssh_host = request.params.ssh_host
    ssh_port = request.params.ssh_port
    ssh_user = request.params.ssh_user
    ssh_password = request.params.ssh_password

    redis1 = redis.Redis(
        host=host,
        port=port,
        password=password,
        db=0,
        socket_timeout=5,
    )

    data = {}
    try:
        redis1.dbsize()
        data['success'] = True
    except Exception as e:
        data['success'] = False
        data['error'] = str(e)

    return data


@route('/get_key_detail')
def get_key_detail():
    host = request.params.host
    port = request.params.port
    password = request.params.password
    by_ssh = request.params.by_ssh
    ssh_host = request.params.ssh_host
    ssh_port = request.params.ssh_port
    ssh_user = request.params.ssh_user
    ssh_password = request.params.ssh_password
    db = request.params.db
    key = request.params.key

    redis1 = redis.Redis(
        host=host,
        port=port,
        password=password,
        db=db,
        decode_responses=True,
        socket_timeout=5,
    )

    ttl = redis1.ttl(key)
    key_type = redis1.type(key)

    if key_type == 'none':
        key_type = ''

    data = {
        'key_type': key_type,
        'ttl': ttl,
        'string_data': '',
        'list_data': [],
        'hash_data': [],
        'set_data': [],
        'zset_data': [],
    }

    if key_type == 'string':
        data['string_data'] = redis1.get(key)

    elif key_type == 'list':
        rs = redis1.lrange(key, 0, -1)
        n = 0
        for value in rs:
            data['list_data'].append({
                'index': n,
                'value': value,
            })
            n += 1

    elif key_type == 'hash':
        rs = redis1.hgetall(key)
        for key, value in rs.items():
            data['hash_data'].append({
                'key': key,
                'value': value,
            })

    elif key_type == 'set':
        rs = redis1.smembers(key)
        for value in rs:
            data['set_data'].append({
                'value': value,
            })

    elif key_type == 'zset':
        rs = redis1.zrange(key, 0, -1, withscores=True)
        for value, score in rs:
            data['zset_data'].append({
                'score': score,
                'value': value,
            })

    else:
        assert not key_type, (key, key_type)

    return data


run(host='0.0.0.0', port=8080, reloader=True, debug=True)


# docker run -it --rm -p 6379:6379 redis
# pip install -r requirements.txt
# python easyapp.py

