# pymath

### Example 1. Pointwise Convergence

![](test.svg)

<img src="https://render.githubusercontent.com/render/math?math=f(x) = \lim_{n \rightarrow \infty} f_{n}(x) = \lim_{n \rightarrow \infty} \left (\frac{n x \dotplus x^{2}}{n}\right )\mathtt{\text{ = }}x">

Thus, <img src="https://render.githubusercontent.com/render/math?math=(f_n)"> converges pointwise to <img src="https://render.githubusercontent.com/render/math?math=f(x) = x"> on <img src="https://render.githubusercontent.com/render/math?math=\mathbb R">.


### Example 2. Uniform Convergence

![](test2.svg)

For any fixed <img src="https://render.githubusercontent.com/render/math?math=x \in \mathbb R">, we can see that <img src="https://render.githubusercontent.com/render/math?math=\lim f_n(x) = 0"> so that <img src="https://render.githubusercontent.com/render/math?math=f(x) = 0"> is the pointwise limit of the sequence <img src="https://render.githubusercontent.com/render/math?math=(f_n)"> on <img src="https://render.githubusercontent.com/render/math?math=\mathbb R">. **Is this convergence uniform?** The observation that <img src="https://render.githubusercontent.com/render/math?math=1/(1 \dotplus x^2) \leq 1 \ , \ \forall x \in \mathbb R"> implies that

<img src="https://render.githubusercontent.com/render/math?math=|f_n(x) - f(x)| = \left|\frac{1}{1 \dotplus x^2} - 0\right| \leq \frac{1}{n^2}">

Thus, given <img src="https://render.githubusercontent.com/render/math?math=\epsilon \gt 0">, we can choose <img src="https://render.githubusercontent.com/render/math?math=N \gt \frac{1}{\epsilon}"> (which does not depend on <img src="https://render.githubusercontent.com/render/math?math=x">), and it follows that for every <img src="https://render.githubusercontent.com/render/math?math=n \geq N"> implies <img src="https://render.githubusercontent.com/render/math?math=|f_n(x) - f(x)| \lt \epsilon \ , \ \forall x \in \mathbb R">. By Definition, <img src="https://render.githubusercontent.com/render/math?math=f_n \rightarrow 0"> uniformly on <img src="https://render.githubusercontent.com/render/math?math=\mathbb R">.

