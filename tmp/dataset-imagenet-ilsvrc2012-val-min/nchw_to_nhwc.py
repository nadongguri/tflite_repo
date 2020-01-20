import numpy as np

for i in range(0, 500):
    file_path = './nchw/'
    new_path = './nhwc/'
    file_name = 'input_' + str(i) + '_nchw.npy'
    new_name = 'input_' + str(i) + '_nhwc.npy'
    npy = np.load(file_path + file_name)
    npy = npy.transpose(1,2,0)
    print(npy.shape, npy.dtype)
    np.save(new_path + new_name, npy)



