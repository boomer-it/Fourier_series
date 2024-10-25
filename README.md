# Importing required libraries
>[Python library reference](https://docs.python.org/3/library/index.html)
---
## Numpy
>[Numpy docs](https://numpy.org/doc/)
## Matplotlib
>[Matplotlib docs](https://matplotlib.org/stable/users/explain/quick_start.html)
## Scipy
>[Scipy docs](https://docs.scipy.org/doc/scipy/)
---
### Explanation
1. Generate a function using the `def` statement.
2. Interval of the function is important (this is the period), and the function repeats itself after this period.
3. The number of terms has to be defined as a computer does not have the ability to compute to infinite terms.
4. Calculation of fourier coefficients, `a_0` , `a_n` and `b_n` is computed using the scipy library.
### Fourier Coefficients

#### 1. DC Component 1
![DC component](https://math.vercel.app/?color=white&bgcolor=black&from=%5Cfrac%7B1%7D%7Bl%7D%5Ccdot%5Cint_%7B%5Calpha%7D%5E%7B%5Calpha%20%2B%202l%7Df%28x%29dx.svg)
#### 2. Fourier Coefficient 2
![Cosine component](https://math.vercel.app/?color=white&bgcolor=black&from=%5Cfrac%7B1%7D%7Bl%7D%5Ccdot%5Cint_%7B%5Calpha%7D%5E%7B%5Calpha%20%2B%202l%7Df%28x%29%7B%5Ccdot%7Dcos%28%5Cfrac%7Bn%5Cpi%20x%7D%7Bl%7D%29dx.svg)
#### 3. Fourier Coefficient 3
![Sine component](https://math.vercel.app/?color=white&bgcolor=black&from=%5Cfrac%7B1%7D%7Bl%7D%5Ccdot%5Cint_%7B%5Calpha%7D%5E%7B%5Calpha%20%2B%202l%7Df%28x%29%7B%5Ccdot%7Dsin%28%5Cfrac%7Bn%5Cpi%20x%7D%7Bl%7D%29dx.svg)

---

### Finishing by calculating the series and animating in a loop.
1. A buffer is needed to hold intermediate values.
```python
y_dc = np.full_like(x_vals, a0 / 2)   # Start with DC term (constant)
y_sine = np.zeros_like(x_vals)        # Placeholder for current sine term
y_cosine = np.zeros_like(x_vals)      # Placeholder for current cosine term
y_fourier = np.full_like(x_vals, a0 / 2)  # Start cumulative Fourier with DC term
```
2. Clear axes as well using
```python
 for ax in axs.flat:
        ax.cla()
```
3. Add four subplots using the OO API of mpl and add the plots.
4. Animate in a for loop.
---
