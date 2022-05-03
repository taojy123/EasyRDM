import redis

import bottle
from bottle import route, run, template, request
from nanorm import Model
from utils import handle_keys


@route('/')
def index():
    message = '1111'
    # bottle.TEMPLATES.clear()
    return template('index', **locals())


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

    try:
        # keys = redis1.keys(pattern=pattern)
        keys = []
        cursor = 0
        while True:
            cursor, skeys = redis1.scan(cursor=cursor, match=pattern, count=1000)
            print('scan', cursor, len(skeys))
            if not cursor:
                break
            keys += skeys
    except Exception as e:
        return {'error': str(e)}

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


run(host='localhost', port=8080, reloader=True, debug=True)


# docker run -it --rm -p 6379:6379 redis
# pip install -r requirements.txt
# python easyapp.py

