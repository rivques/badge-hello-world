import time
import badge
from badge.input import Buttons

class App(badge.BaseApp):
    def on_open(self):
        # this method is called once, when the app opens
        self.logger.info("this app just launched!")

        self.counter = 0

        badge.display.fill(1)
        badge.display.nice_text("Hello, World!", 0, 0, 24)
        badge.display.show()

    def loop(self):
        # this method is called repeatedly while the app is running
        if badge.input.get_button(Buttons.SW4):
            self.logger.info("SW4 pressed!")
            badge.display.fill(1)
            badge.display.nice_text(f"Counter: {self.counter}", 0, 10, 18)
            badge.display.show()
        self.counter += 1
        self.logger.info(f"Counter: {self.counter}")
        time.sleep(1)