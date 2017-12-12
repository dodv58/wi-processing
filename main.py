
from scipy import signal
import numpy as np
from json_respond import json_respond

# convolutional
def conv(inputC, kernel):
  max_len = max(len(inputC), len(kernel))
  result = np.real(np.fft.ifft( np.fft.fft(inputC, max_len)*np.fft.fft(kernel, max_len))).tolist()
  result = [round(result[i], 4) for i in range(len(result))]
  return json_respond(200, result)
