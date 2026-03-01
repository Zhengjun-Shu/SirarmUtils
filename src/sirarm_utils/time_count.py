import time
import uuid


class TimeCount:
    def __init__(self):
        self.list = {}
        self.name_list = []

    def start(self, name=None):
        try:
            import torch
            torch.cuda.synchronize()
        except:
            pass
        if name is None:
            name = str(uuid.uuid1())[:5]
        self.name_list.append(name)
        self.list[name] = {
            'start': time.time(),
            'end': None,
            'range': None,
        }
        return name

    def end(self, name=None):
        try:
            import torch
            torch.cuda.synchronize()
        except:
            pass
        if name is None:
            raise Exception('name is None')
        self.list[name]['end'] = time.time()
        self.list[name]['range'] = self.list[name]['end'] - self.list[name]['start']
        return self.list[name]['range']

    def get(self, name=None, re_point_time=False):
        if name is None:
            raise Exception('name is None')
        if re_point_time:
            return self.list[name]['range'], self.list[name]['start'], self.list[name]['end']
        else:
            return self.list[name]['range']

    def has_name(self, name):
        return name in self.name_list

    def functionCount(self, name, func, *args, **kwargs):
        name = self.start(name)
        out = func(*args, **kwargs)
        return out, self.end(name)
