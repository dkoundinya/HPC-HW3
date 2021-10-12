# Part A Question 8
from matplotlib import pyplot as plt
import numpy as np 
import scipy

#Frequency in terms of Hertz
fre  = 5 
#Sample rate
fre_samp = 50
t = np.linspace(0, 2, 2 * fre_samp, endpoint = False )
a = np.sin(fre  * 2 * np.pi * t)
figure, axis = plt.subplots()
axis.plot(t, a)
axis.set_xlabel ('Time (s)')
axis.set_ylabel ('Signal Amplitude')
plt.show()

#do DFT and visualize:
from scipy.fft import fft
m = fft(a)

N = len(m)
n = np.arange(N)
T = N/fre_samp
freq = n/T 
plt.stem(freq, abs(m), 'b', \
         markerfmt=" ", basefmt="-b")
plt.xlabel('Freq (Hz)')
plt.ylabel('DFT Amplitude |X(freq)|')
plt.show()  