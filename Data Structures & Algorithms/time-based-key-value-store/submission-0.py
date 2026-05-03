class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in map, initialize empty list for it
        # then append value, timestamp to the list
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        l = 0
        r = len(values) - 1
        # we want to get the value with the given timestamp
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] == timestamp:
                res = values[mid][0]
                break
            if values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid -1 
        return res
