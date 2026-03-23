import math

class levelExpCalculator:
    @classmethod
    def getExpValue(self, lvl, growthRate: str):
        
        expValue = 0
        if(growthRate == "slow"):
            expValue = 5 * math.pow(lvl, 3) / 4
            return expValue
        if(growthRate == "mediumslow"):
            expValue = ((6/5) * math.pow(lvl, 3)) - (15*(math.pow(lvl, 2))) + (100*lvl) - 140
            return expValue
        if(growthRate == "mediumfast"):
            expValue = math.pow(lvl, 3)
            return expValue
        if(growthRate == "fast"):
            expValue = 4 * math.pow(lvl, 3) / 5
            return expValue
        else:
            print("Invalid growth rate.")
            return expValue