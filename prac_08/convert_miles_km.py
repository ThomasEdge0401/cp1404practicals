from kivy.app import App
from kivy.lang import Builder

MILES_TO_KM = 1.60934


class MilesKmConverter(App):
    def build(self):
        self.title = "Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_convert(self):
        miles = self.get_miles()
        self.root.ids.output_label.text = str(miles * MILES_TO_KM)

    def handle_change(self, amount):
        miles = self.get_miles() + amount
        self.root.ids.input_miles.text = str(miles)
        self.handle_convert()

    def get_miles(self):
        try:
            return float(self.root.ids.input_miles.text)
        except:
            return 0


MilesKmConverter().run()
