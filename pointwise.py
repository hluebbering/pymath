# linearly spaced numbers
x = np.linspace(-5, 5, 500)

# define functions
y1 = x**2 + x
y5 = ((x**2 + 5*x)/5)
y10 = ((x**2 + 10*x)/10)
y20 = ((x**2 + 20*x)/20)

# figure parameters
fig = plt.figure()
ax = fig.add_subplot()
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['top'].set_color('none')

# plot functions
plt.plot(x, y1, 'g', label = r'$f_1$', color = 'mediumslateblue')
plt.plot(x, y5, 'g', label = r'$f_5$', color = 'darkslateblue')
plt.plot(x, y10, 'g', label = r'$f_{10}$', color = 'lightskyblue')
plt.plot(x, y20, 'g', label = r'$f_{20}$', color = 'mediumseagreen')

# plot axis 
plt.ylim(-3, 5)
plt.xticks(fontsize = 6)
plt.yticks(fontsize = 6)

# plot title 
plt.title(label='Let $\mathit{f_n = \\frac{x^2+nx}{n}}$ on all $\mathbb{R}$:', 
          fontsize = 14, color = 'black', fontfamily = 'Times', loc='left')

# plot legend
ax.legend(shadow = False, fontsize = 8, frameon = True, ncol = 1, loc = 'best')

# save figure as svg  
fig.tight_layout()
plt.savefig("test.svg")
