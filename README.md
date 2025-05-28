# 🔎 Binary Search in Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A simple and efficient implementation of the binary search algorithm in Python.

---

## 🚀 Overview

Binary search is a classic algorithm for quickly finding a target value within a sorted list. It repeatedly divides the search interval in half, achieving **O(log n)** time complexity.

---

## 📦 Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RosmeoP/binary-search.git
   cd binary-search
Run the script:

bash
python binary_search.py
Edit the input list or search target inside binary_search.py as needed.

📝 Example
Python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(arr, target)
print(f"Element found at index: {result}")
📚 Resources
Binary Search (Wikipedia)
Python Documentation
📄 License
This project is licensed under the MIT License.
