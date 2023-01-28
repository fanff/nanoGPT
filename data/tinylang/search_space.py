import os

strt_str = "python train.py --dataset=data/tinylang/ "

adds = ["--device=cuda --compile=True",
        "--eval_interval=500 --log_interval=5 --lr_decay_iters=10000 --max_iters=12000",
        "--block_size=128 --batch_size=16"]

import itertools
a = itertools.product([2,4,8,16],
                      [2,4,8,16],
                      [16,64,256,512])


opts = [f"--n_layer={n_layer} --n_head={n_head} --n_embd={n_embd}" for n_layer,n_head,n_embd in a]


cmds = [strt_str+" ".join(adds+[a]) for a in opts]

for cmd in cmds:
    print(cmd)
    os.system(cmd)