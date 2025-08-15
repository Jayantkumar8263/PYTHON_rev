#Data frame
import pandas as pd
data = {
    'food items' : ['x', 'y', 'z'],
    "price" : [30, 40, 50],
    'sold quantity' :[100, 120, 200]
}
df = pd.DataFrame(data, index=(1,2,3))
print(df)