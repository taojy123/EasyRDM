



def handle_keys(keys):
    """
    input: ['aa:bb:cc', 'xx:yy', 'aa:bb:dd']
    output:
    [
        {
            "id": "aa",
            "label": "aa",
            "children": [
                {
                    "id": "aa:bb",
                    "label": "bb",
                    "children": [
                        {
                            "id": "aa:bb:cc",
                            "label": "cc"
                        },
                        {
                            "id": "aa:bb:dd",
                            "label": "dd"
                        }
                    ]
                }
            ]
        },
        {
            "id": "xx",
            "label": "xx",
            "children": [
                {
                    "id": "xx:yy",
                    "label": "yy"
                }
            ]
        }
    ]
    """

    # step1:
    # [
    #   ['aa', 'bb', 'cc'],
    #   ['aa', 'bb', 'dd'],
    #   ['xx', 'yy']
    # ]
    all_key_items = []
    for key in keys:
        key_items = key.split(':')
        all_key_items.append(key_items)
    all_key_items.sort()

    # step2:
    # {
    #     'aa': {
    #         'bb': {
    #             'cc': {},
    #             'dd': {},
    #         }
    #     },
    #     'xx': {
    #         'yy': {}
    #     },
    #  }
    def _make_children(all_items):
        if not all_items:
            return {}
        t = {}
        # { 'aa': [ ['bb', 'cc'],  ['bb', 'dd'] ],  'xx': [['yy']] }
        for items in all_items:
            first_item = items[0]
            after_items = items[1:]
            if first_item not in t:
                t[first_item] = []
            if after_items:
                # 没有下级就不要再添加了
                t[first_item].append(after_items)
        for k in t.keys():
            t[k] = _make_children(t[k])
        return t

    all_key_items = _make_children(all_key_items)

    # step3: final output
    def _make_list(all_items, parent_sid=''):
        if not all_items:
            return []
        rs = []
        for k in sorted(all_items.keys()):
            sid = k
            if parent_sid:
                sid = parent_sid + ':' + k
            r = {
                'id': sid,
                'label': k,
            }
            children_list = _make_list(all_items[k], sid)
            if children_list:
                r['children'] = children_list
            rs.append(r)
        return rs

    all_key_items = _make_list(all_key_items)

    return all_key_items


