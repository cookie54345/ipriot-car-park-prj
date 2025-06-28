class Display:
    def __init__(self,
                 display_id,
                 message="",
                 is_on=False):
        self.id = display_id
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message}"

    def update(self, data):
        for key, value in data.items():
            print(f"{key}: {value}")