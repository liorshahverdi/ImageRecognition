from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

i = Image.open('images/numbers/0.1.png')
iar = np.asarray(i)

plt.imshow(iar)
print (iar)
plt.show()