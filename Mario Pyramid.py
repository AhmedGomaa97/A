def mario_pyramid(heigh) :
  for i in range(0, heigh +1):
     print(" " * (heigh - i) + "#" * i)

mario_pyramid(4)