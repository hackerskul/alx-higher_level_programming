#!/usr/bin/python3
def multiple_returns(sentance):
    if sentance == '':
        return 0, None
    return len(sentance), sentance[0]
