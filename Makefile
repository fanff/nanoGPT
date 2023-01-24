


help:
    cat "lol"

run_big_french
     python train.py --dataset=big_french --n_layer=8 --n_head=8 --n_embd=256 --device=cuda --compile=False --eval_interval=200 --log_interval=10 --block_size=256 --batch_size=10
