from xportage.reading.sst import SST


def get_reader_cls(name):
    if name == 'sst':
        return SST
