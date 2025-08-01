# Sorting 0s, 1s, and 2s Without Using Sorting Algorithms

This project implements an efficient, one-pass sorting algorithm specifically for arrays containing only the integers `0`, `1`, and `2`. The solution uses the **Dutch National Flag Algorithm** to sort the array in **linear time O(n)** without using any built-in sorting functions or traditional sorting algorithms.

---

## 🚀 Features

- One-pass, in-place sorting
- No additional space required
- Optimized for arrays containing only `0`, `1`, and `2`
- Demonstrates the Dutch National Flag algorithm

---

## 📌 Problem Statement

Given an array that contains only 0s, 1s, and 2s, sort the array in a single scan (i.e., visit each element only once).

### Example:

**Input:**
```
0 1 2 1 0 2
```

**Output:**
```
0 0 1 1 2 2
```

---

## 📂 File Structure

```
sorting array without sorting algo only012.py
README.md
```

---

## 🧠 Algorithm Used

### Dutch National Flag Algorithm

We maintain three pointers:
- `low`: Index to place 0s
- `mid`: Current element
- `high`: Index to place 2s

Depending on the value at `arr[mid]`, we:
- Swap with `low` if it's 0
- Move ahead if it's 1
- Swap with `high` if it's 2

This ensures one-pass sorting in-place.

---

## 📄 Code Overview

```python
def sort012(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    print(arr)
```

---

## ▶️ How to Run

### Prerequisites:
- Python 3.x

### Run the script:
```bash
python sorting\ array\ without\ sorting\ algo\ only012.py
```

### Example Input:
```
0 1 2 1 2 0
```

### Example Output:
```
0 0 1 1 2 2
```