import pandas as pd
import random
serviceRandomNumber = 0
interArrivalTime = []
serviceTime = []
arrivals = []
timeServiceBegins = []
serviceEnds = []
waitingQueue = []
timeSpentInSystem = []
spentTime = 0
waiting = 0
arrivalTime = 0
serviceBegins = 0
timeServiceEnds = 0
systemIdle = 0
systemIdleTime = []
num0fSim = 1
for i in range(20):
    randomNumber = int(random.random() * 1000)
    if i == 0:
        interArrivalTime.append(0)
    else:
        if 0 <= randomNumber <= 125:
            interArrivalTime.append(1)
        elif 126 <= randomNumber <= 250:
            interArrivalTime.append(2)
        elif 251 <= randomNumber <= 375:
            interArrivalTime.append(3)
        elif 376 <= randomNumber <= 500:
            interArrivalTime.append(4)
        elif 501 <= randomNumber <= 625:
            interArrivalTime.append(5)
        elif 626 <= randomNumber <= 750:
            interArrivalTime.append(6)
        elif 751 <= randomNumber <= 875:
            interArrivalTime.append(7)
        elif 876 <= randomNumber <= 1000:
            interArrivalTime.append(8)
for i in range(20):
    serviceRandomNumber = int(random.random() * 100)
    if 0 <= serviceRandomNumber <= 10:
        serviceTime.append(1)
    elif 11 <= serviceRandomNumber <= 30:
        serviceTime.append(2)
    elif 31 <= serviceRandomNumber <= 60:
        serviceTime.append(3)
    elif 61 <= serviceRandomNumber <= 85:
        serviceTime.append(4)
    elif 86 <= serviceRandomNumber <= 95:
        serviceTime.append(5)
    elif 96 <= serviceRandomNumber <= 100:
        serviceTime.append(6)
for i in range(num0fSim):
    for j in range(20):
        arrivalTime = arrivalTime+interArrivalTime[j]
        arrivals.append(arrivalTime)

        if arrivals[j] == 0:
            serviceBegins = 0
        else:
            if arrivals[j] > serviceEnds[j-1]:
                serviceBegins = arrivals[j]
            else:
                serviceBegins = serviceEnds[j-1]
        timeServiceBegins.append(serviceBegins)
        timeServiceEnds = timeServiceBegins[j] + serviceTime[j]
        serviceEnds.append(timeServiceEnds)
        waiting = timeServiceBegins[j]-arrivals[j]
        if waiting < 0:
            waiting = 0
        waitingQueue.append(waiting)
        spentTime = serviceTime[j] + waitingQueue[j]
        timeSpentInSystem.append(spentTime)
        if arrivals[j] - serviceEnds[j-1] <= 0:
            systemIdle = 0
        else:
            systemIdle = arrivals[j] - serviceEnds[j-1]
        systemIdleTime.append(systemIdle)
newPandas = pd.DataFrame({'iat': interArrivalTime, "arrival time": arrivals, "service time": serviceTime,"service begins":timeServiceBegins ,"Service Ends":serviceEnds, "time in queue":waitingQueue , "time spent in system":timeSpentInSystem,"time idle":systemIdleTime})
print(newPandas)
with open("output.txt", "w") as file:
    newPandas.to_excel("output.xlsx", index=True)