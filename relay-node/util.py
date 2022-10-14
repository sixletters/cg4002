import numpy as np

def get_min(inputs):
    return np.min(inputs)

def get_max(inputs):
    return np.max(inputs)

def get_mean(inputs):
    return np.mean(inputs)

def get_std(inputs):
    return np.std(inputs)

def get_med(inputs):
    arr = np.ma.array(inputs).compressed()
    med = np.median(arr)
    return np.median(np.abs(arr - med))

def get_range(inputs):
    return np.max(inputs)-np.min(inputs)

def get_power_spectrum(inputs):
    ft = np.fft.fft(inputs)
    return np.abs(ft**2/len(inputs))

def get_max_f(inputs):
    S = get_power_spectrum(inputs)
    return np.max(S)

def get_mean_f(inputs):
    S = get_power_spectrum(inputs)
    return np.mean(S)

def get_std_f(inputs):
    S = get_power_spectrum(inputs)
    return np.var(S)

def normalize(inputs):
    mean = np.mean(inputs)
    std = np.std(inputs)
    final = (inputs-mean)/std
    return final

def dataParser(inputs, dataMap, key):
    min = get_min(inputs)
    maxV = get_max(inputs)
    mean = get_mean(inputs)
    std = get_std(inputs)
    med = get_med(inputs)
    rnge = get_range(inputs)
    max_f = get_max_f(inputs)
    mean_f = get_mean_f(inputs)
    std_f = get_std_f(inputs)

    dataMap[key] = [min, maxV, mean, std, med, rnge, max_f, mean_f, std_f]