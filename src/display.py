class Display:
    def __init__(self,
                 display_id,
                 message="",
                 is_on=False):
        self.id = display_id
        self.message = message
        self.is_on = is_on

    def update(self, data):
        if "message" in data:
            self.message = data["message"]

        if self.is_on:
            for key, value in data.items():
                print(f"{key}: {value}")