"""
Brianca Washington
1001132562
Hw5
"""


import numpy as np
import scipy.io.wavfile as pa
from scipy.io import wavfile
from scipy.signal import freqz
import matplotlib.pyplot as plt 
import soundfile as sf


cutoff=7500
L=101
M= L-1

#open wav file
orig,fs  = sf.read('P_9_2.wav')

#f
f=cutoff/fs
resultfilter=np.ones(L)
w=np.ones(L)

# make them h[n] lowpass filter
for n in range(len(resultfilter)):
	if(n== M/2):
		result= 2*f
	else:
		result= ((np.sin(2*np.pi*f*(n-(M/2))))/(np.pi*(n-(M/2))))
	resultfilter[n]=result

#create the w[n]
for n in range(len(w)):
	w[n]=0.54 -.46*np.cos(2*np.pi*n/M)

#
filter_coefficients = resultfilter* w
x1, y1 = freqz(resultfilter, 1)
x2, y2 = freqz(filter_coefficients, 1)

#Plot the frequency
# Plot the signals (ORIGINAL, FREQ SIG, APPLIED SIG)
plt.figure(1)
plt.title("Frequency Response")
plt.plot(x1, abs(y1))
plt.plot(x2, abs(y2))
plt.show()

# convolve the signals 
new=np.convolve(filter_coefficients,orig)

#save file back
sf.write('cleanMusic.wav',new , fs)