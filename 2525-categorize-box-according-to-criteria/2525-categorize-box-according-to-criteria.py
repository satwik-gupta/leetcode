class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        x=False
        y=False
        if(length>=10**4 or width>=10**4 or height>=10**4 or ((length/1000)*(width/1000)*(height/1000))>=1):
            x=True
        if(mass>=100):
            y=True
        if(x and y):
            return "Both"
        elif(x and not y):
            return "Bulky"
        elif(not x and y):
            return "Heavy"
        else:
            return "Neither"