
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
        data=f.read()

    toks = np.array(enc.encode_ordinary(data), dtype=np.uint16)
    print(f"data has {len(toks):,} tokens")

    toks.tofile(input_file+'.bin')

if __name__ == '__main__':
    main()