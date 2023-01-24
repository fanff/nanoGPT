


help:
    cat "lol"

train_big_french:
     python train.py --dataset=big_french --n_layer=12 --n_head=12 --n_embd=768 --device=cuda --compile=False --eval_interval=2000 --log_interval=10 --block_size=256 --batch_size=10

train_big_french:
     python sample.py --seed=3 --num_samples=10 --max_new_tokens=100 --device=cuda --start="Le doudou il "
