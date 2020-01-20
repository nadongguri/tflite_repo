import numpy as np

for i in range(0, 500):
    file_path = './nchw/'
    new_path = './image/'
    file_name = 'image_' + str(i) + '.npy'
    new_name = 'image' + str(i) + '.npy'
    npy = np.load(file_path + file_name)
    npy = npy.transpose(0,2,3,1)
    print(npy.shape, npy.dtype)
    np.save(new_path + new_name, npy)



