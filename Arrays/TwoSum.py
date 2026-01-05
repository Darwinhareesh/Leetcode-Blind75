# 🧮 Two Sum

## 🔍 Problem Statement
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers** such that they add up to `target`.

You may assume that:
- Each input has **exactly one solution**
- You may not use the same element twice

---

## 🧠 Intuition (Think This Way)
Instead of checking **every pair** (which is slow), we can:
- Remember the numbers we have already seen
- For each new number, check if its **required complement** already exists

This allows us to solve the problem in **one pass**.

---

## 💡 Key Idea (Hash Map)
If:
a + b = target
Then:
b = target - a

So while iterating:
- Calculate `remSum = target - nums[i]`
- Check if `remSum` already exists in a hash map

---

## 🚶 Step-by-Step Approach
1. Create an empty hash map to store numbers and their indices
2. Traverse the array
3. For each element:
   - Compute `remSum = target - nums[i]`
   - If `remSum` exists in the map → solution found
   - Otherwise, store the current number with its index

---

## 🧪 Example Walkthrough
### Input
nums = [2, 7, 11, 15]
target = 9

### Execution
| Index | Value | remSum | HashMap | Action |
|------|------|--------|--------|--------|
| 0 | 2 | 7 | {} | Store 2 |
| 1 | 7 | 2 | {2:0} | Found → return |

### Output
[1, 0]


---

## 💻 Code (One-Pass Hash Map)
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        Hmap = {}
        for i in range(len(nums)):
            remSum = target - nums[i]
            if remSum in Hmap:
                return [i, Hmap[remSum]]
            Hmap[nums[i]] = i
⏱ Time & Space Complexity

Time Complexity: O(n)

Space Complexity: O(n)

🎯 Why This Works

Each number is checked once

Hash map lookup is O(1)

Avoids unnecessary nested loops

⚠️ Edge Cases

Negative numbers

Zero values

Target = 0

(All handled naturally by the hash map)

🧠 Interview Tip

If asked to explain, say:

“I store previously seen numbers in a hash map and for each element I check whether its complement exists. This allows me to solve the problem in one pass.”

✅ Summary

Avoid brute force

Use hash map for fast lookups

One pass solution

Clean and efficient


---

If you want, next I can:
- Create **templates** for all problems
- Rewrite explanations in **interview speaking style**
- Help you maintain **consistent formatting** across the repo

Just tell me 👍
