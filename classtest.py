class area:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def areacalc(self):
        answer = self.length * self.width
        return answer

    def printarea(self):
        thisanswer = self.areacalc()
        print(f'L={self.length} W={self.width} A={thisanswer}')


equ1 = area(10, 10)
equ1.printarea()
equ2 = area(2, 2)
equ2.printarea()
equ3 = area(100, 100)
equ3.printarea()
