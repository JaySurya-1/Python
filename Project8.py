print("Jay Surya \n1AY24AI048 \nAIML 'M' ")
class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    def from_seconds(self, total_seconds):
        self.hours = total_seconds // 3600
        total_seconds %= 3600
        self.minutes = total_seconds // 60
        self.seconds = total_seconds % 60
        return self
def mul_time(time, number):
    total_seconds = time.to_seconds() * number
    result = Time().from_seconds(int(total_seconds))
    return result
def average_pace(finishing_time, distance):
    pace_seconds = finishing_time.to_seconds() / distance
    return Time().from_seconds(int(pace_seconds))

finish = Time(1, 30, 0)  
distance = 10  
print("Time multiplied by 2:", mul_time(finish, 2))  
print("Average pace per mile:", average_pace(finish, distance)) 
