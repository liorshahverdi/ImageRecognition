from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

i = Image.open('images/dotndot.png')
iar = np.asarray(i)

plt.imshow(iar)
plt.show()