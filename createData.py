import argparse

if __name__ == "__main__":

    #check minimum records

    parser = argparse.ArgumentParser(description="Create measurement file")
    parser.add_argument("-o","--output", dest="ouput", type=str, help="Measurement file name - default is measurements.txt",default="measurements.txt")




