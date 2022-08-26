import numpy as np

text = "Cnn()=sssfccccggD"

chars = tuple(set(text))
print(f"chars:{chars}")
int2char = dict(enumerate(chars))
print(f"int2char:{int2char}")
char2int = {ch: ii for ii, ch in int2char.items()}
print(f"char2int:{char2int}")
# Encode the text
encoded = np.array([char2int[ch] for ch in text])
print(f"encoded:{encoded}")
