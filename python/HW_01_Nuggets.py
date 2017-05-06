#Seth Muhlestein
#Fin6320

def max_nugget_number(num, pkg1 = 6, pkg2 = 9, pkg3 = 20):
    for i in range(num//pkg1 + 1):
        for j in range(num//pkg2 + 1):
            for k in range(num//pkg3 + 1):
                if(pkg1*i + pkg2*j + pkg3*k == num):
                    return True

    return False

def main():
    possible = 6
    highest = 0
    counter = 0
    smallest_pkg = 6

    while(counter < smallest_pkg):
        if(max_nugget_number(possible)):
            counter += 1
        else:
            highest = possible
            counter = 0
        possible += 1

    print("The highest number of nuggest that you cannot purchase is:{}".format(highest))

if __name__ == "__main__":
    main()
