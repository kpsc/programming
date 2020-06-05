## pandarallel

```python
import pandas as pd
from pandarallel import pandarallel
pandarallel.initialize(nb_workers=4)

df.parallel_apply(func, axis=1)
```

```python
workers = 10
from joblib import Parallel, delayed
size = int(len(data) / workers) + 10
results = Parallel(n_jobs=workers)(delayed(fun)(data[i:i+size]) for i in range(0, len(data), size))
```

