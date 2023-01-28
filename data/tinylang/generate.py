import numpy as np
import torch


def open_data_file(dataset):
    alldata = np.memmap(dataset, dtype=np.uint16, mode='r')
    n =len(alldata)
    train_data = alldata[:int(n*0.9)]
    val_data = alldata[int(n*0.9):]
    return train_data,val_data

def x_y_from_data(data,block_size,batch_size,device=None):
    ix = torch.randint(len(data) - block_size, (batch_size,))
    x = torch.stack([torch.from_numpy((data[i:i+block_size]).astype(np.int64)) for i in ix])
    y = torch.stack([torch.from_numpy((data[i+1:i+1+block_size]).astype(np.int64)) for i in ix])

    if device:
        x, y = x.to(device), y.to(device)
    return x, y

def get_batch_gen(split):
    while True:
        # pick random file
        dataset = all_files[random.randint(0, len(all_files) - 1)]
        print(f"loading {split} {dataset}")
        train_data, val_data = open_data_file(dataset)
        data_gen = train_data if split == 'train' else val_data
        iter_count = train_buffer_iter if split == 'train' else val_buffer_iter
        # pick n time in the buffer and release_it
        for i in range(iter_count):

            yield x_y_from_data(data_gen)


#train_data = get_batch_gen('train')
#val_data = get_batch_gen('test')
def get_batch(split):
    data_gen = train_data if split == 'train' else val_data
    return next(data_gen)


x,y = x_y_from_data(np.array(range(100)),2,2)

quit()
