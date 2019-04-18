class SelectorStatistics:
    def __init__(self):
        self._statisticsDictionary = {}

    def increment(self, name):
        if self._statisticsDictionary.keys().__contains__(name):
            hit_count = self._statisticsDictionary[name]
            hit_count += 1
            self._statisticsDictionary[name] = hit_count
        else:
            self._statisticsDictionary[name] = 1

    def print(self):
        for key in self._statisticsDictionary.keys():
            hit_count = self._statisticsDictionary[key]
            print(" " + key, hit_count)
