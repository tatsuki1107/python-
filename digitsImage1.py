import sklearn.datasets
import maplotlib.pylot as plt

digits = sklearn.datasets.load_digits()

plt.imshow(digits.images[0], cmap="Greys")
plt.show()