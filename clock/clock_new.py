class Clock:
    def __init__(self, hour, minute):
        self.hour = hour % 24
        self.hour += minute // 60
        self.hour %= 24
        self.minute = minute % 60

    def __str__(self):
        return "{0:02}:{1:02}".format(self.hour, self.minute)

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def add(self, minute):
        self.minute += minute
        self.hour += self.minute // 60
        self.hour %= 24
        self.minute %= 60
        return self
   
if __name__ == '__main__':
    hours_input = int(input('Enter hours : '))
    minutes_input = int(input('Enter minutes : '))
    clock_variable = Clock(hours_input, minutes_input)
    print (clock_variable)