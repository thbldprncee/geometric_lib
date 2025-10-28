# Math formulas
## Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²

## Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a

# Functions
## Circle
## Calculating the area:
*(r - radius)*
```python
import math
def area(r):
    return math.pi * r * r
```
> Example area(5) -> 78.53981633974483

## Calculating the perimeter:
*(r - radius)*
```python
import math
def perimeter(r):
    return 2 * math.pi * r
```
> Example perimeter(5) -> 31.41592653589793


## Rectangle

## Calculating the area:
*(a, b - sides of rectangle)*
```python
def area(a, b):
    return a * b
```
> Example area(5, 6) -> 30

## Calculating the perimeter:
*(a, b - sides of rectangle)*
```python
def perimeter(a, b):
    return 2 * (a + b)
```

>Example perimeter(5, 6) -> 22

## Square

## Calculating the area:
*(a - square's side)*

```python
def area(a):
    return a * a
```

>Example area(5) -> 25

## Calculating the perimeter:
*(a - square's side)*
```python
def perimeter(a):
    return 4 * a
```

>Example perimeter(5) -> 20

## Triangle

## Calculating the area:
*(a - base of the triangle, h - height of the triangle)*

```python
def area(a, h):
    return a * h / 2
```
>Example area(5, 2) -> 5
## Calculating the perimeter:
*(a - base of the triangle, h - height of the triangle)*
```python
def perimeter(a, b, c):
    return a + b + c
```
>Example perimeter(4, 5, 6) -> 15

# Changelog
[fixed rectangle.py](https://github.com/thbldprncee/geometric_lib/commit/a7ab35a5426c8a5b58ab820b1c8b1d47a36d60f7)
[added triangle.py](https://github.com/thbldprncee/geometric_lib/commit/d8b83f2abb4f5fb09cd770425237070552fe488)
[added rectangle.py](https://github.com/thbldprncee/geometric_lib/commit/0d79b66a2ad2ffb23b4a20089d6b29d26ff2461e)
# Changelog
- [Fixed rectangle.py](https://github.com/thbldprncee/geometric_lib/commit/a7ab35a5426c8a5b58ab820b1c8b1d47a36d60f7)
- [Added triangle.py](https://github.com/thbldprncee/geometric_lib/commit/d8b83f2abb4f5fb09cd770425237070552fe488)
- [Added rectangle.py](https://github.com/thbldprncee/geometric_lib/commit/0d79b66a2ad2ffb23b4a20089d6b29d26ff2461e)
- [L-03: Docs added](https://github.com/thbldprncee/geometric_lib/commit/d078c8d9ee6155f3cb0e577d28d337b791de28e2)
- [L-03: Circle and square added](https://github.com/thbldprncee/geometric_lib/commit/8ba9aeb3cea847b63a91ac378a2a6db758682460)