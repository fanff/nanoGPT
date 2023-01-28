import os
import pickle

import numpy as np


stoi = {}
for i in range(10):
    stoi[str(i)] = i
stoi["("] = 10
stoi[")"] = 11
stoi["+"] = 12
stoi["="] = 13
stoi[" "] = 14



itos={v:k for k,v in stoi.items()}


meta_path = os.path.join(os.path.dirname(__file__), 'meta.pkl')
with open(meta_path, 'wb') as f:
    metadict = {
        "stoi":stoi,
        'itos':itos,
        "vocab_size": len(stoi)
    }
    print(metadict)
    pickle.dump(metadict ,f)

encode = lambda s: [stoi[c] for c in s]
decode = lambda l: ''.join([itos[i] for i in l])


a= np.random.randint(0,49,(50*10**6,3),dtype=np.uint16)


a[:,2] = a[:,0] + a[:,1]

aa = ' '.join((f"({l[0]}+{l[1]})={l[2]}" for l in a))
del a


train_ids = np.array(encode(aa), dtype=np.uint16)
del aa
train_ids.tofile(os.path.join(os.path.dirname(__file__), 'train.bin'))


quit()
