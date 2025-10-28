import jax.numpy as jnp

x = jnp.array([1.0, 2.0, 3.0])
y = jnp.array([4.0, 5.0, 6.0])

print(x + y)
print(x * y)
print(jnp.dot(x, y))