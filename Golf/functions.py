def calcHandicap(rounds, diffList):
    handicapDiff = diffList[:]
    x = 0
    total = 0
    if rounds <= 6:
        diffUsed = 1
    elif rounds <=8:
        diffUsed = 2
    elif rounds <= 10:
        diffUsed = 3
    elif rounds <= 12:
        diffUsed = 4
    elif rounds <= 14:
        diffUsed = 5
    elif rounds <= 16:
        diffUsed = 6
    elif rounds == 17:
        diffUsed = 7
    elif rounds == 18:
        diffUsed = 8
    elif rounds == 19:
        diffUsed = 9
    elif rounds >= 20:
        diffUsed = 10
    while x < diffUsed:
        low = min(handicapDiff)
        handicapDiff.remove(low)
        total = total+low
        x += 1
    handicap = (.96*(total/diffUsed))
    handicap = round(handicap, 2)
    return handicap

def yearAverages(rounds):
    roundsplayed = len(rounds)
    avgScore = 0
    avgPutts = 0
    avgFH = 0
    avgGIR = 0
    for x in range(0, roundsplayed):
        year = rounds[x].date.year
        avgScore += rounds[x].strokes
        avgPutts += rounds[x].putts
        avgFH += rounds[x].fairways_hit
        avgGIR += rounds[x].gir
    avgScore = avgScore/roundsplayed
    avgPutts = avgPutts/roundsplayed
    avgFH = avgFH/roundsplayed
    avgGIR = avgGIR/roundsplayed
    return (year, roundsplayed, avgScore, avgPutts, avgFH, avgGIR)

def rollingAverages(rounds):
    last_5 = rounds[:5]
    #last_10 = rounds[0:9]
    #last_20 = rounds[0:19]
    avgScore = 0
    avgPutts = 0
    avgFH = 0
    avgGIR = 0
    for x in range(0, 5):
        avgScore += last_5[x].strokes
        avgPutts += last_5[x].putts
        avgFH += last_5[x].fairways_hit
        avgGIR += last_5[x].gir
    avgScore = avgScore/5
    avgPutts = avgPutts/5
    avgFH = avgFH/5
    avgGIR = avgGIR/5
    return (avgScore, avgPutts, avgFH, avgGIR)
