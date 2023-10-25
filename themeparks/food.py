"""food wagons"""

class ChipWagon:
    """yummy chips"""
    def __init__(self, temperature):
        self.temperature = temperature

    def serve(self, food):
        """Serve food"""
        heat = "hot" if self.temperature > 90 else "cold"
        print(f"Here is your {food}. It is {heat}.")
