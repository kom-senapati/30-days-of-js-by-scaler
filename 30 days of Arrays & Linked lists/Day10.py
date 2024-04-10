# Merge interval | Insert interval

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort(key=lambda i:i.start)
        res = [intervals[0]]
        for interval in intervals[1:]:
            le = res[-1].end
            if interval.start <= le:
                res[-1].end = max(le, interval.end)
            else:
                res.append(interval)
        return res