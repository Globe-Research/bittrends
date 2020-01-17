# Returns moving average with selected window size
def MovingAverage(data, window):
    moving_average = data.rolling(window=window).mean()
    return moving_average

# Returns true if trend1 crossed under trend2 in most recent step
def crossesUnder(trend1, trend2):
    
    # Check if trend1 has crossed under trend2
    if trend1[len(trend1)-1] >= trend2[len(trend2)-1]:
        return False
    else:
        if trend1[len(trend1)-2] < trend2[len(trend2)-2]:
            return False
        elif trend1[len(trend1)-2] > trend2[len(trend2)-2]:
            return True
        else:
            x = 2
            while trend1[len(trend1)-x] == trend2[len(trend2)-x]:
                x = x + 1
            if trend1[len(trend1)-x] > trend2[len(trend2)-x]:
                return True
            else:
                return False

# Returns true if trend1 crossed over trend2 in most recent step
def crossesOver(trend1, trend2):
    
    # Check if trend1 has crossed over trend2
    if trend1[len(trend1)-1] <= trend2[len(trend2)-1]:
        return False
    else:
        if trend1[len(trend1)-2] > trend2[len(trend2)-2]:
            return False
        elif trend1[len(trend1)-2] < trend2[len(trend2)-2]:
            return True
        else:
            x = 2
            while trend1[len(trend1)-x] == trend2[len(trend2)-x]:
                x = x + 1
            if trend1[len(trend1)-x] < trend2[len(trend2)-x]:
                return True
            else:
                return False
