class Clock:
    '''
    Clock takes input hours and minutes and outputs time as a string 
    in 24 hour format. You can add minutes to the time by using add method. 
    add() takes a parameter minute
    '''
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
        self.total_minutes = (minutes + hours * 60) % 1440
        if self.total_minutes < 0:
            self.total_minutes = 1440 - self.total_minutes
        
    def __str__(self):
        return '%02d:%02d' % (int(self.total_minutes / 60), self.total_minutes % 60)
        
    def __eq__(self, other):
        return self.hours == other.hours and self.minutes == other.minutes
        
    def add(self, minutes):
        self.total_minutes = (self.total_minutes + minutes) % 1440
        if self.total_minutes < 0:
            self.total_minutes = 1440 - self.total_minutes
        return self
  
if __name__ == '__main__':
    print('This is a clock which asks you to input hours and minutes.\nYou get time in hh:mm 24 hour format. \nYou can add minutes later if you wish to do so.\n')
    hours_input = int(input('Enter hours : '))
    minutes_input = int(input('Enter minutes : '))
    clock_variable = Clock(hours_input, minutes_input)
    print (clock_variable)
    print('\nType "exit" to exit. Type "add" to add minutes.')
    next_instruction = input('Next Instruction  : ')
    while(not next_instruction.lower() == 'exit'):
        if next_instruction.lower() == 'add':
            minutes_to_add = int(input('Enter minutes to add : '))
            clock_variable.add(minutes_to_add)
            print(clock_variable)
            next_instruction = input('Enter next instruction') 
        elif next_instruction.lower() == 'exit':
            break
        else:
            print ('Your instruction is invalid. Please try again :', end=' ')
            next_instruction = input() 
            