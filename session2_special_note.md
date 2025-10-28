
---

### 📌 Special Note: Why CSV Headers Matter

The `csv.DictReader` in Python **requires headers** in the first row of the CSV file. These headers define the keys for each dictionary it reads.

If headers like `id,title,completed` are missing:
- `DictReader` will treat the first **data row** as headers.
- You’ll get incorrect keys like `'1'`, `'Learn Python'`, which break your logic.
- Accessing `row["title"]` will throw a `KeyError`.

Always write headers once when creating the file, using:
```python
writer.writeheader()
```
This keeps your file readable and compatible with future reads.

---
