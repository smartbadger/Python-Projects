
class Array(object):

    def __init__(self, capacity, fillValue = None):
        self._items = list()
        for count in xrange(capacity):
            self._items.append(fillValue)

    def __len__(self):
        return len(self._items)


    def __str__(self):
        return str(self._items)


    def __iter__(self):
        return iter(self._items)


    def __getitem__(self, index):
        return self._items[index]


    def __setitem__(self, index, newItem):
        self._items[index] = newItem

