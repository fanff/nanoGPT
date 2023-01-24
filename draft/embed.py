import requests
import tiktoken


enc = tiktoken.get_encoding("gpt2")


a = enc.encode_ordinary("un embedding de taille vocabulaire")

pass