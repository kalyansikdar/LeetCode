class TimeTable:
    def __init__(self, inStationName, outStationName, checkIn, checkOut):
        self.inStationName = inStationName
        self.outStationName = outStationName
        self.checkIn = checkIn
        self.checkOut = checkOut


class UndergroundSystem:
    def __init__(self):
        self.system = {}
        self.archive = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.system[id] = TimeTable(stationName, None, t, None)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        timeTable = self.system[id]

        timeTable.outStationName = stationName
        timeTable.checkOut = t

        entry = (timeTable.inStationName, timeTable.outStationName)
        travelTime = timeTable.checkOut - timeTable.checkIn

        if entry not in self.archive:
            self.archive[entry] = [travelTime]
        else:
            self.archive[entry].append(travelTime)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        allTravelTimes = self.archive[(startStation, endStation)]
        return sum(allTravelTimes) / len(allTravelTimes)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)