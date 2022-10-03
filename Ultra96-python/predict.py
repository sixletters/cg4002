from pynq import Overlay
import pynq.lib.dma
from pynq import DefaultIP
from pynq import allocate
import struct
import numpy as np
import time
from struct import pack, unpack

overlay = Overlay('./design_3_wrapper.bit') # add path to bitstream
dma = overlay.axi_dma_0

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return np.log(e_x / e_x.sum())

# returns category group 0/1/etc
def predict(inputs, overlay, dma):
    output = []
    input_buffer = allocate(shape = (6,), dtype=np.int32)
    for i in range(6):
        input_buffer[i] = unpack('i', pack('f', inputs[i]))[0]
    output_buffer = allocate(shape = (3,), dtype=np.int32)
    dma.sendchannel.transfer(input_buffer)
    dma.recvchannel.transfer(output_buffer)
    dma.sendchannel.wait()
    dma.recvchannel.wait()
    for i in range(3):
        output.append(unpack('f', pack('i',output_buffer[i]))[0])
    output = softmax(output)
    output = output.tolist().index(max(output))
    return output
