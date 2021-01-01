# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 11:33:51 2020

@author: pahi9557
"""


import numpy as np
import matplotlib.pyplot as plt
import csv


def PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file):
    with open(inc_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        time_i = []
        flux_i = []
        error_i = []
        for row in readCSV:
            time_i.append(row[0])
            flux_i.append(row[1])
            error_i.append(row[2])
            
    with open(inc_darks_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        time_id = []
        flux_id = []
        error_id = []
        for row in readCSV:
            time_id.append(row[0])
            flux_id.append(row[1])
            error_id.append(row[2])
    dark_temp = (float(flux_id[0]) + float(flux_id[1]))/2
    error_temp = (float(error_id[0]) + float(error_id[1]))/2
    flux_id = np.zeros(len(flux_i))
    for i in range(len(flux_id)): flux_id[i] = dark_temp
    error_id = np.zeros(len(flux_i))
    for i in range(len(error_id)): error_id[i] = error_temp
    
    with open(ref_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        time_r = []
        flux_r = []
        error_r = []
        for row in readCSV:
            time_r.append(row[0])
            flux_r.append(row[1])
            error_r.append(row[2])

    with open(ref_darks_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        time_rd = []
        flux_rd = []
        error_rd = []
        for row in readCSV:
            time_rd.append(row[0])
            flux_rd.append(row[1])
            error_rd.append(row[2])
    dark_temp = (float(flux_rd[0]) + float(flux_rd[1]))/2
    error_temp = (float(error_rd[0]) + float(error_rd[1]))/2
    flux_rd = np.zeros(len(flux_r))
    for i in range(len(flux_rd)): flux_rd[i] = dark_temp
    error_rd = np.zeros(len(flux_r))
    for i in range(len(error_rd)): error_rd[i] = error_temp
    
   
    time_i = np.asarray(time_i, dtype=np.float32)
    flux_i = np.asarray(flux_i, dtype=np.float32)
    error_i= np.asarray(error_i, dtype=np.float32)
    
    time_id = np.asarray(time_id, dtype=np.float32)
    flux_id = np.asarray(flux_id, dtype=np.float32)
    error_id= np.asarray(error_id, dtype=np.float32)
    
    time_r = np.asarray(time_r, dtype=np.float32)
    flux_r = np.asarray(flux_r, dtype=np.float32)
    error_r= np.asarray(error_r, dtype=np.float32)
    
    time_rd = np.asarray(time_rd, dtype=np.float32)
    flux_rd = np.asarray(flux_rd, dtype=np.float32)
    error_rd= np.asarray(error_rd, dtype=np.float32)
    
    # unadjusted_Reflectivity = flux_r/flux_i
    # unadjusted_error = unadjusted_Reflectivity*np.sqrt((error_i/flux_i)**2+(error_r/flux_r)**2)
    
    flux_i = flux_i - flux_id
    flux_r = flux_r - flux_rd
    error_i = np.sqrt(error_i**2 + error_id**2)
    error_r = np.sqrt(error_r**2 + error_rd**2)
    
    
    Reflectivity_sample = flux_r/flux_i
    error_sample = Reflectivity_sample*np.sqrt((error_i/flux_i)**2+(error_r/flux_r)**2)
    return(Reflectivity_sample,error_sample)



def MCP_ref_curve(MCP_inc_and_ref_file):
    with open(MCP_inc_and_ref_file) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        wav_MCP =[]
        flux_i_MCP = []
        error_i_MCP = []
        flux_id_MCP = []
        error_id_MCP = []
        flux_r_MCP = []
        error_r_MCP = []
        flux_rd_MCP = []
        error_rd_MCP = []
        # for row in readCSV: print(row)
        for row in readCSV:
            wav_MCP.append(row[0])
            flux_i_MCP.append(row[1])
            error_i_MCP.append(row[2])
            flux_id_MCP.append(row[3])
            error_id_MCP.append(row[4])
            flux_r_MCP.append(row[5])
            error_r_MCP.append(row[6])
            flux_rd_MCP.append(row[7])
            error_rd_MCP.append(row[8])
    wav_MCP = np.asarray(wav_MCP, dtype=np.float32)
    flux_i_MCP = np.asarray(flux_i_MCP, dtype=np.float32)
    error_i_MCP= np.asarray(error_i_MCP, dtype=np.float32)
    flux_id_MCP = np.asarray(flux_id_MCP, dtype=np.float32)
    error_id_MCP= np.asarray(error_id_MCP, dtype=np.float32)
    flux_r_MCP = np.asarray(flux_r_MCP, dtype=np.float32)
    error_r_MCP= np.asarray(error_r_MCP, dtype=np.float32)
    flux_rd_MCP = np.asarray(flux_rd_MCP, dtype=np.float32)
    error_rd_MCP= np.asarray(error_rd_MCP, dtype=np.float32)
    flux_i_MCP = flux_i_MCP - flux_id_MCP
    flux_r_MCP = flux_r_MCP - flux_rd_MCP
    error_i_MCP = np.sqrt(error_i_MCP**2 + error_id_MCP**2)
    error_r_MCP = np.sqrt(error_r_MCP**2 + error_rd_MCP**2)
    Reflectivity = flux_r_MCP/flux_i_MCP
    error = Reflectivity*np.sqrt((error_i_MCP/flux_i_MCP)**2+(error_r_MCP/flux_r_MCP)**2)
    return(Reflectivity,error)




inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF1.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF1_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF1.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF1_darks.csv"
Reflectivity_sampleF_1, error_sample1_1 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF2.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF2_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF2.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF2_darks.csv"
Reflectivity_sampleF_2, error_sample1_2 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF3.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF3_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF3.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF3_darks.csv"
Reflectivity_sampleF_3, error_sample1_3 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF4.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF4_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF4.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF4_darks.csv"
Reflectivity_sampleF_4, error_sample1_4 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF5.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\incident_datF5_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF5.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleF\reflected_datF5_darks.csv"
Reflectivity_sampleF_5, error_sample1_5 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

#############################################################################################################
inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG1.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG1_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG1.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG1_darks.csv"
Reflectivity_sampleG_1, error_sample1_1 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG2.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG2_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG2.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG2_darks.csv"
Reflectivity_sampleG_2, error_sample1_2 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG3.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG3_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG3.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG3_darks.csv"
Reflectivity_sampleG_3, error_sample1_3 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG4.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG4_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG4.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG4_darks.csv"
Reflectivity_sampleG_4, error_sample1_4 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)

inc_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG5.csv"
inc_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\incident_datG5_darks.csv"
ref_file =r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG5.csv"
ref_darks_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\SampleG\reflected_datG5_darks.csv"
Reflectivity_sampleG_5, error_sample1_5 = PMT_ref_curve(inc_file,inc_darks_file,ref_file,ref_darks_file)


master_ref_sampleF = []
master_err_sampleF = []
for i in range(len(Reflectivity_sampleF_1)):
    a = [Reflectivity_sampleF_1[i] , Reflectivity_sampleF_2[i]  , Reflectivity_sampleF_3[i]  , 
                      Reflectivity_sampleF_4[i]  , Reflectivity_sampleF_5[i]]
    master_ref_sampleF.append(float(np.mean(a)))
    master_err_sampleF.append(float(np.std(a)))
master_ref_sampleF = np.asarray(master_ref_sampleF)
master_err_sampleF = np.asarray(master_err_sampleF)

master_ref_sampleG = []
master_err_sampleG = []
for i in range(len(Reflectivity_sampleG_1)):
    a = [Reflectivity_sampleG_1[i] , Reflectivity_sampleG_2[i]  , Reflectivity_sampleG_3[i]  , 
                      Reflectivity_sampleG_4[i]  , Reflectivity_sampleG_5[i]]
    master_ref_sampleG.append(float(np.mean(a)))
    master_err_sampleG.append(float(np.std(a)))
master_ref_sampleG = np.asarray(master_ref_sampleG)
master_err_sampleG = np.asarray(master_err_sampleG)





MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref1.csv.csv"
Reflectivity_MCPF_1, error_MCPF_1 = MCP_ref_curve(MCP_inc_and_ref_file)

MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref2.csv.csv"
Reflectivity_MCPF_2, error_MCPF_2 = MCP_ref_curve(MCP_inc_and_ref_file)

MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref3.csv.csv"
Reflectivity_MCPF_3, error_MCPF_3 = MCP_ref_curve(MCP_inc_and_ref_file)

MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref4.csv.csv"
Reflectivity_MCPF_4, error_MCPF_4 = MCP_ref_curve(MCP_inc_and_ref_file)

MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref5.csv.csv"
Reflectivity_MCPF_5, error_MCPF_5 = MCP_ref_curve(MCP_inc_and_ref_file)

MCP_inc_and_ref_file = r"C:\Users\pahi9557\Desktop\LAB\SquareTank\JPL_samples\calibration_samples\MCP\SampleF\inc_and_ref6.csv.csv"
Reflectivity_MCPF_6, error_MCPF_6 = MCP_ref_curve(MCP_inc_and_ref_file)

master_ref_sampleF_MCP= []
master_err_sampleF_MCP= []
for i in range(len(Reflectivity_MCPF_1)):
    a = [Reflectivity_MCPF_1[i] , Reflectivity_MCPF_2[i]  , Reflectivity_MCPF_3[i]  , 
                      Reflectivity_MCPF_4[i], Reflectivity_MCPF_5[i], Reflectivity_MCPF_6[i]]
    master_ref_sampleF_MCP.append(float(np.mean(a)))
    master_err_sampleF_MCP.append(float(np.std(a)))
master_ref_sampleF_MCP= np.asarray(master_ref_sampleF_MCP)
master_err_sampleF_MCP= np.asarray(master_err_sampleF_MCP)







wav = np.linspace(120,230,23)
wav_MCP = [92.0,97.1,102.6,104.8,106.6,111.5,114.3,116.4,120.5,125.0]

fig1 = plt.figure()
#sample 1 0904F 

plt.plot(wav, 100*Reflectivity_sampleF_1, color = 'green', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleF_2, color = 'green', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleF_3, color = 'green', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleF_4, color = 'green', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleF_5, color = 'green', alpha =0.2)
plt.errorbar(wav, 100*master_ref_sampleF, 100*master_err_sampleF, xerr=None, color = 'green', ecolor='green', linewidth=2, elinewidth=1, capsize=2, label = 'Al ebeam evap {70}, ALD LiF 90C {1200}'
             ,alpha = 0.5)
#\n $\overline{R}$ $\pm$ $\sigma$

plt.plot(wav, 100*Reflectivity_sampleG_1, color = 'red', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleG_2, color = 'red', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleG_3, color = 'red', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleG_4, color = 'red', alpha =0.2)
plt.plot(wav, 100*Reflectivity_sampleG_5, color = 'red', alpha =1)
plt.errorbar(wav, 100*master_ref_sampleG, 100*master_err_sampleG, xerr=None, color = 'red', ecolor='red', linewidth=2, elinewidth=1, capsize=2, label = 'Al ebeam evap {70}, ALD LiF 90C {1200}'
             ,alpha = 0.5)


# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_1,100*error_MCPF_1, color = 'magenta', alpha = 0.2)
# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_2,100*error_MCPF_2, color = 'magenta', alpha = 0.2)
# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_3,100*error_MCPF_3, color = 'magenta', alpha = 0.2)
# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_4,100*error_MCPF_4, color = 'magenta', alpha = 0.2)
# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_5,100*error_MCPF_5, color = 'magenta', alpha = 0.2)
# plt.errorbar(wav_MCP, 100*Reflectivity_MCPF_6,100*error_MCPF_6, color = 'magenta', alpha = 0.2)

plt.plot(wav_MCP, 100*Reflectivity_MCPF_1,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.plot(wav_MCP, 100*Reflectivity_MCPF_2,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.plot(wav_MCP, 100*Reflectivity_MCPF_3,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.plot(wav_MCP, 100*Reflectivity_MCPF_4,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.plot(wav_MCP, 100*Reflectivity_MCPF_5,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.plot(wav_MCP, 100*Reflectivity_MCPF_6,linestyle ='dashed', color = 'green', alpha = 0.2)
plt.errorbar(wav_MCP, 100*master_ref_sampleF_MCP, 100*master_err_sampleF_MCP, xerr=None,linestyle ='dashed', color = 'green', ecolor='green', linewidth=2, elinewidth=1, capsize=2, label = 'MCP'
    ,alpha = 0.5)


plt.ylabel('% Reflected', fontsize=18)
plt.xlabel('Wavelength (nm)', fontsize=18)
#plt.xlim(8191, 16383)
plt.ylim(0, 90)
plt.title(r'Calibration Samples, A.O.I. = 5$\degree$', fontsize=18)
plt.legend()





