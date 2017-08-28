# Data
A set of APIs for use by dashboard for displaying data.

## API
###/aggs  
<details><summary>Possible parameters:</summary>

* **filter**: will update the count on all other variables.
	possible filter params:
	* Category
	* Discount
	* Style
	* Brand
	* Size
	* Retailer
	* Colour
	* Market
	* Sex 

```
?filter={"Brand":["ZALORA"]}
```

<details>
<summary> Full api return:</summary>

```python
 {
  "Brand": {
    "& Seven Days": 32,
    .... 
    "1028": 24, 
    "youme&hunny": 19, 
    "zatu emerald": 17, 
    "zaxy": 26
  }, 
  "Category": {
    "Accessories": 68975, 
    .... 
    "Swimwear & Beachwear": 34239, 
    "Tops": 161380
  }, 
  "Colour": {
    " apricot": 43, 
    " apricot black": 3, 
    .... 
	"zinfandel": 56, 
    "zinfandel marle": 5, 
    "zinfandel wash": 6
  }, 
  "Discount": {
    .... 
    "91.0": 39, 
    "95.0": 99, 
    "96.0": 10, 
    "97.0": 1
  }, 
  "Market": {
    "Malaysia": 170800, 
    "Singapore": 170800, 
    "UK": 170800, 
    "US": 170800
  }, 
  "Retailer": {
    "adidas": 1733, 
    .... 
    "whitesoot": 624, 
    "zalora": 220454
  }, 
  "Sex": {
    "Female": 12345, 
    "Male": 0, 
    "Unisex": 124
  }, 
  "Size": {
    "CHEST 38IN R": 1,
    .... 
    "CUP A": 9, 
    "CUP B": 9, 
    "CUP C": 8  
  }, 
  "Style": {
    "A Line Dresses": 138, 
    "Backpacks": 8017, 
    .... 
    "Baju Kurungs": 6307, 
      }
}
```
</details>
</details>