import sys
import importlib
import math

def lb2kg(kg):
    try:
        lb = float(kg) * 2.20462
        if __name__ == "__main__":
            a = float(sys.argv[1])
            lb = kg_lb(a)
            print(lb)
    except:
        lb = 0.0
        if __name__ == "__main__":
            print(lb)
    return lb

def in2mm(inch):
    try:
        mm = float(inch) * 25.4
        if __name__ == "__main__":
            a = float(sys.argv[1])
            mm = inch_mm(a)
            print(mm)
    except:
        mm = 0.0
        if __name__ == "__main__":
            print(mm)
    return mm

def lbin2Nmm(lbin):
    try:
        Nmm = float(lbin) / 5.7101471627692
        if __name__ == "__main__":
            a = float(sys.argv[1])
            Nmm = lbin2Nmm(a)
            print(Nmm)
    except:
        Nmm = 0.0
        if __name__ == "__main__":
            print(Nmm)
    return Nmm