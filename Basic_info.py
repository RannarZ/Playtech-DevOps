import psutil

def systemParameters():
    parameter = input("What do you wish to see? ")
    if parameter == "cpu":

        cores = psutil.cpu_count()
        load_avg = psutil.getloadavg()
        data = psutil.cpu_times(percpu=True)
        cpu_pr = psutil.cpu_percent(1, True)

        print("\nCPU\n---\ncores\n-----\n-\n" + str(cores) + "\n-\n" + "load average\n------------\n 1    5    15\n---- ---- ----\n " + str(round(load_avg[0], 2)) + "  " + str(round(load_avg[1], 2)) + "  " + str(round(load_avg[2], 2)) + "\n")
        print("times\n-----\n     user    nice    system    idle    iowait    irq    softirq    steal    guest    guest_nice\n--  -----   -----   -------   -----   -------   ----   --------   ------   ------   -----------\n")
        for i in range(cores):
            times_string = ""
            for j in range(len(data[i])):
                times_string = times_string + str(round(data[i][j], 2)) + "  "
            print(str(i) + "   " + times_string)
            
        core_string = " "
        underlines = ""
        core_percents = ""
        for i in range(cores):
            core_string = core_string + str(i) + "     "
            underlines = underlines + "----  "
            core_percents = core_percents + str(round(cpu_pr[i], 2)) + "   "
        print("\nUtilization\n-----------\n" + core_string + "\n" + underlines + "\n" + core_percents)
        return 1

    elif parameter == "mem":
        memory_data = psutil.virtual_memory()
        swap_memory = psutil.swap_memory()

        print("\nMEMORY\n------\n")
        listOfMemAttributes = ["total", "available", "percent", "used", "free", "active", "inactive", "buffers", "cached", "shared", "slab"]
        print("virtual memory\n--------------\n---------  ----------")
        for i in range(len(memory_data)):
            if len(listOfMemAttributes[i]) <= 5:
                memDataString = listOfMemAttributes[i] + "       " + str(round(memory_data[i], 2))
            else:
                memDataString = listOfMemAttributes[i] + "     " + str(round(memory_data[i], 2))
            print(memDataString)

        print("---------  ----------\n")
        print("swap\n----\n-------  ----------")
        listOfSwapAttributes = ["total", "used", "free", "percent", "sin", "sout"]
        for i in range(len(swap_memory)):
            if len(listOfSwapAttributes[i]) < 4:
                print(listOfSwapAttributes[i] + "        " + str(round(swap_memory[i], 2)))
            elif len(listOfSwapAttributes[i]) == 4:
                print(listOfSwapAttributes[i] + "       " + str(round(swap_memory[i], 2)))
            elif len(listOfSwapAttributes[i]) == 5:
                print(listOfSwapAttributes[i] + "      " + str(round(swap_memory[i], 2)))
            else:
                print(listOfSwapAttributes[i] + "    " + str(round(swap_memory[i], 2)))
        print("-------  ----------")
        
        return 1
    else:
        print("Invalid input!")
        systemParameters()
        return 0

systemParameters()
