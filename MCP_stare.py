'''
Usage: MCP_scan.py <mono port> <counter port> filename"

if serial is not recognized in anaconda, may need to run 'pip install pyserial'
in the anaconda powershell prompt
'''

import serial
import numpy as np
import sys
import vm502
import time



# Read N samples from counter and return average
def read_n_samples(s, n):
    s.reset_input_buffer()
    # print(s.read_until())
    #print(s.read_until())

    l = []
    for i in range(n):
        v = s.read_until()
        #print(v)
        v = np.float(v.decode('ASCII').replace(',', ''))
        l.append(v)
        #l.append(float(s.read_until()))

    a = np.array(l)
    return(np.average(a), np.std(a))


#mp : monochromotor port
#cp : counter port
#fname : filename to save it under.
#dfnmae : dark filename. If left blank it will be fname_dark
def main(mp, cp):
    starttime = time.time()
    ms = serial.Serial(mp, 9600, timeout = 5.0)
    cs = serial.Serial(cp, 9600, timeout = 3.0)

    wav = input("\n Please enter a wavelength: (e.g. 92.0)\n")  
    print(f'You entered {wav}')
    
    cs.reset_input_buffer()
    # print(cs.read_until())

    cl = vm502.vm502_get_lambda(ms)
    N  = 50


    dwav = '65.0'
    t_tot = 0
    
    print(f'Now moving to {wav} \n')
    cl = vm502.vm502_goto(ms, wav) #moving to starting wavelength
    time.sleep(0.5) #wait half a second!
    f, fdev = read_n_samples(cs, N)#take the data
    print('----------------------------')
    print("Flux: {0:f}, std: {1:f} ".format(f, fdev))
    print('---------------------------- \n')
    
    #taking a dark
    print('moving to 65nm to take a dark sample \n')
    cl = vm502.vm502_goto(ms, dwav)
    print("Wavelength: {0:s} ".format(cl))
    time.sleep(0.5) #wait half a second!
    f, fdev = read_n_samples(cs, int(N/3))
    print('----------------------------')
    print("Flux: {0:f}, std: {1:f} \n".format(f, fdev))
    print('---------------------------- \n')


    
    
    t_tot += time.time()-starttime
    print('Elapsed: '+str(t_tot) + ' seconds \n') #print the time


    cs.close()
    ms.close()




if __name__ == '__main__':
    if (len(sys.argv) < 2):
        print("Usage: lamp_monitor.py <mono port> <counter port>")
        exit()

    mono_port = str(sys.argv[1])
    counter_port = str(sys.argv[2])

    print("Monochromator Port: {0:s}".format(mono_port))
    print("Counter Port: {0:s}".format(counter_port))


    main(mono_port, counter_port)
