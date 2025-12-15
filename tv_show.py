import tv
# tv_show.py file
# main program

def main():
   # object creation
   tv1 = tv.TV('Samsung')

   # object usage
   tv1.show_status()
   tv1.turn_on()
   tv1.show_status()
   tv1.show_channels()
   tv1.set_channels(['TVP1','TVP2','Polsat','TVN','Filmbox','Discovery','History'])
   tv1.show_channels()
   tv1.increase_vol()
   tv1.show_status()
   tv1.turn_off()


if __name__ == "__main__":
   main()