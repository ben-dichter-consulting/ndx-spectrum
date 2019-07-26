# ndx-spectrum Extension for NWB:N

[![PyPI version](https://badge.fury.io/py/ndx-spectrum.svg)](https://badge.fury.io/py/ndx-spectrum)

[Python Installation](#python-installation)

[Python Usage](#python-usage)
    
### Python Installation
```bash
pip install ndx-spectrum
```

### Python Usage

```python
from ndx_spectrum import Spectrum
from datetime import datetime
from pynwb import NWBFile

nwb = NWBFile('session_description', 'identifier', datetime.now().astimezone())

spectrum = Spectrum('test_spectrum', frequencies=[1.,2.,3.], power=[1.,2.,3.],
                    phase=[1.,2.,3.])
```
