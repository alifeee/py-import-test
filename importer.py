"""tests"""

# works
from themeparks.monkeyworld import Baboon, Macaque

monkey1 = Baboon("Joseph")
monkey2 = Macaque("Brian")

monkey1.hoot()
monkey2.hoot()

# works
from themeparks import monkeyworld

monkey1 = monkeyworld.Baboon("Joseph")
monkey2 = monkeyworld.Macaque("Brian")

monkey1.hoot()
monkey2.hoot()

# works
# from themeparks import ChipWagon

# chipwagon = ChipWagon(100)
# chipwagon.serve("fries")

# # works
# import themeparks

# chipwagon = themeparks.ChipWagon(100)

# chipwagon.serve("fries")

# # works
# import themeparks

# chipwagon = themeparks.food.ChipWagon(100)

# chipwagon.serve("fries")

# does not work
import themeparks

monkey1 = themeparks.monkeyworld.Baboon("Joseph")
monkey2 = themeparks.monkeyworld.Macaque("Brian")

monkey1.hoot()
monkey2.hoot()
