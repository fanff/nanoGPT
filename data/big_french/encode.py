
import argparse
import click

import numpy as np
import tiktoken





import os

@click.command()
@click.argument('input_file')
@click.option('--encoder',default="gpt2", )
def main(input_file, encoder):
    enc = tiktoken.get_encoding(encoder)


    with open(input_file, 'r', encoding="utf-8") as f:
        stack = []
        stack_size = 0
        outidx=0
        while True:
            a = f.read(1000000)
            if len(a) == 0:
                write_stack(stack,stack_size,outidx)

                break

            toks = np.array(enc.encode_ordinary(a), dtype=np.uint16)

            stack.append(toks)
            stack_size+=len(toks)

            if stack_size>=200*1000*1000:
                write_stack(stack,stack_size,outidx)
                stack = []
                outidx+=1
                stack_size=0
def write_stack(stack,stack_size,idx):
    filename = f"{idx:04d}.bin"
    np.concatenate(stack).tofile(filename)
    print(f"wrote {filename} with {stack_size} tokens")

if __name__ == '__main__':
    main()