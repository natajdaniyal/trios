class TriosState:
    """
    هسته وضعیت لحظه‌ای Trios

    این بخش مثل حافظه کوتاه‌مدت سیستم عصبی عمل می‌کند:
    موقعیت، حرکت و حالت فعلی آزمایش را نگه می‌دارد.
    """

    def __init__(self):

        # موقعیت اولیه
        self.x = 0
        self.y = 0

        # سرعت حرکت
        self.velocity_x = 0
        self.velocity_y = 0

        # وضعیت آزمایش
        self.running = False

        # نام آزمایش فعال
        self.current_experiment = None



    def move(self, dx, dy):

        self.x += dx
        self.y += dy



    def reset(self):

        self.x = 0
        self.y = 0

        self.velocity_x = 0
        self.velocity_y = 0

        self.running = False

        self.current_experiment = None



    def start_experiment(self, name):

        self.current_experiment = name
        self.running = True



    def stop_experiment(self):

        self.running = False



# نمونه اصلی سیستم وضعیت Trios
state = TriosState()