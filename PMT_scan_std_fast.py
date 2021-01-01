'''
Usage: PMT_scan.py <mono port> <counter port> filename"

if serial is not recognized in anaconda, may need to run 'pip install pyserial'
in the anaconda powershell prompt
'''

import serial
import numpy as np
import sys
import vm502
import time
from datetime import datetime


# Read N samples from counter and return average
def read_n_samples(s, n):
    s.reset_input_buffer()
    print(s.read_until())
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
def main(mp, cp, fname, dfname):
    ms = serial.Serial(mp, 9600, timeout = 5.0)
    cs = serial.Serial(cp, 9600, timeout = 3.0)

    cs.reset_input_buffer()
    print(cs.read_until())

    cl = vm502.vm502_get_lambda(ms)
    print("Wavelength: {0:s}".format(cl))

    t = []
    flux = []
    fstd = []

    dt = []
    dark = []
    dstd = []
    
    # Number of samples to average per wavelength
    #N = 10
    N = 10
    # Total length of the test
    total_mins = .3 #minutes. This is for each wavelength, set just right so 
                    #that one dark and one wav sample are taken at each wavelength
    # Time between measurements
    
    interval = .5 #seconds
    # Frequency that darks are taken
    #dark_mins = 0.5 #minutes
    # Wavelength of test
    wav = '120.0' #nm, starting wavelength for PMT
    # Wavelength of dark
    dwav = '65.0'
    
    t_tot = 0
    #taking a "before measurement" dark
    print('moving to 65nm to take a dark sample')
    cl = vm502.vm502_goto(ms, dwav)
    print("Wavelength: {0:s}".format(cl))
    f, fdev = read_n_samples(cs, N)
    print("Flux: {0:f}, std: {1:f}".format(f, fdev))
    dt.append(t_tot) #appendind dark data
    dark.append(f)
    dstd.append(fdev)
    print('Now beginning test')
    starttime = time.time()
    for i in range(23):
        cl = vm502.vm502_goto(ms, wav) #moving to starting wavelength
        print("Wavelength: {0:s}".format(cl)) #printing wavelength
        t_tot += time.time()-starttime
        print('Elapsed: '+str(t_tot) + ' seconds') #print the time
        f, fdev = read_n_samples(cs, N)#take the data
        #append the data just taken
        t.append(t_tot)
        flux.append(f)
        fstd.append(fdev)
        #step up the wavelength by 1
        wav = float(wav); wav = wav+5.0; wav = str(wav)
        time.sleep(interval) #wait before next measurement


    print('moving to 65nm to take a dark sample')
    cl = vm502.vm502_goto(ms, dwav)
    print("Wavelength: {0:s}".format(cl))
    f, fdev = read_n_samples(cs, N)
    print("Flux: {0:f}, std: {1:f}".format(f, fdev))
    dt.append(t_tot) #appending dark data
    dark.append(f)
    dstd.append(fdev)
    print('This concludes the test.')
    
    
    # print(np.column_stack((t,flux, fstd)))
    #save the data
    np.savetxt(fname, np.column_stack((t, flux, fstd)), delimiter = ',', fmt = '%s')
    np.savetxt(dfname, np.column_stack((dt, dark, dstd)), delimiter = ',', fmt = '%s')
    print('data saved.')
    cl = vm502.vm502_goto(ms, '161.0')

    cs.close()
    ms.close()




if __name__ == '__main__':
    if (len(sys.argv) < 4):
        print("Usage: lamp_monitor.py <mono port> <counter port> filename")
        exit()

    mono_port = str(sys.argv[1])
    counter_port = str(sys.argv[2])

    print("Monochromator Port: {0:s}".format(mono_port))
    print("Counter Port: {0:s}".format(counter_port))

    fname = sys.argv[3]
    print("Saving to file: {0:s}".format(fname))

    ## Save dark rates in a seperate file
    ftype_loc = fname.find('.')
    dfname = fname[:ftype_loc]+'_darks'+fname[ftype_loc:]
    print("Saving dakrs to file: {0:s}".format(dfname))

    main(mono_port, counter_port, fname, dfname)


