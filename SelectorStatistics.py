import plotly.plotly as py
import plotly.graph_objs as go
import datetime


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

    def keys_to_array(self):

        keys = []

        for key in self._statisticsDictionary.keys():
            keys.append(key)

        return keys

    def values_to_array(self):

        values = []

        for value in self._statisticsDictionary.values():
            values.append(value)

        return values

    def chart(self):
        keys = []
        values = []

        for key in self._statisticsDictionary.keys():
            keys.append(key)

        for value in self._statisticsDictionary.values():
            values.append(value)

        now = datetime.datetime.now()

        trace = go.Pie(labels=keys, values=values)

        py.plot([trace], filename="SelectorStatistics" + " " + str(now))
