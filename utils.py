import numpy as np
import torch

# Defining method to encode one hot labels
def one_hot_encode(arr, n_labels):
  # Initialize the the encoded array
  one_hot = np.zeros((np.multiply(*arr.shape), n_labels), dtype=np.float32)
  # Fill the appropriate elements with ones
  one_hot[np.arange(one_hot.shape[0]), arr.flatten()] = 1.
  # Finally reshape it to get back to the original array
  one_hot = one_hot.reshape((*arr.shape, n_labels))
  return one_hot

def check_gpu():
    # Check if GPU is available
    train_on_gpu = torch.cuda.is_available()

    return train_on_gpu

def number_encoder(text):
    #Encodetext: result example [0 9 9 9 ... 1 3 4 4]
    chars = tuple(set(text))
    int2char = dict(enumerate(chars))
    char2int = {ch: ii for ii, ch in int2char.items()}
    # Encode the text
    encoded = np.array([char2int[ch] for ch in text])
    return encoded, chars
