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

if __name__ == "__main__":
   main()