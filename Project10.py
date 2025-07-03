print("Jay Surya\n1AY24AI048 \nAIML 'M' ")
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.total_seconds = hour * 3600 + minute * 60 + second

    def __str__(self):
        h, m, s = self.to_hms()
        return f"{h:02}:{m:02}:{s:02}"

    def to_hms(self):
        """Convert total_seconds into hours, minutes, seconds."""
        seconds = self.total_seconds
        hour = seconds // 3600
        seconds %= 3600
        minute = seconds // 60
        second = seconds % 60
        return hour, minute, second

    def time_to_int(self):
        """Return total seconds since midnight."""
        return self.total_seconds

    def increment(self, seconds):
        """Add seconds to time."""
        return Time(0, 0, self.total_seconds + seconds)

    def is_after(self, other):
        return self.total_seconds > other.total_seconds

def int_to_time(seconds):
    return Time(0, 0, seconds)

def main():
    start = Time(9, 45, 0)
    print("Start time:", start)

    duration = Time(1, 35, 0)
    print("Duration:", duration)

    end = start.increment(duration.time_to_int())
    print("End time:", end)

    print("Is end after start?", end.is_after(start))

if __name__ == '__main__':
    main()

