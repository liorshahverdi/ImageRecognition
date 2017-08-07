from PIL import Image
import numpy as np 
import matplotlib.pyplot as plt

i = Image.open('captcha_to_break/captcha_1.png')
iar = np.asarray(i)

plt.imshow(iar)
print (iar[20])
plt.show()