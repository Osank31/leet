class Solution:
    def getLeftMax(self, freeTime):
        maxTime = 0
        leftMax = []
        for i in range(len(freeTime)):
            leftMax.append(maxTime)
            maxTime = max(maxTime, freeTime[i])
        return leftMax

    def getRightMax(self, freeTime):
        maxTime = 0
        rightMax = [0] * len(freeTime)
        for i in range(len(freeTime) - 1, -1, -1):
            rightMax[i] = maxTime
            maxTime = max(maxTime, freeTime[i])
        return rightMax

    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        freeTime = [startTime[0]]
        for i in range(1, len(startTime)):
            freeTime.append(startTime[i] - endTime[i - 1])
        freeTime.append(eventTime - endTime[-1])

        leftMax = self.getLeftMax(freeTime)
        rightMax = self.getRightMax(freeTime)

        result = 0
        for i in range(1, len(freeTime)):
            d = endTime[i - 1] - startTime[i - 1]
            if d <= max(leftMax[i - 1], rightMax[i]):
                result = max(result, freeTime[i - 1] + d + freeTime[i])
            result = max(result, freeTime[i - 1] + freeTime[i])

        return result