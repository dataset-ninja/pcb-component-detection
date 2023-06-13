Dataset **PCB Component Detection** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/q/y/kf/ZzG4auEDYJSX2jiKLdAZM62MJDMpa7Qk7zZuGrxtrMtRHJAqWD0nV4bUET3RFSNeINKUsuaOffQas6xPvnSyNoXF1WnVl341RLO9xtkEd00L0D7wKPyiMmmXOiEy.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PCB Component Detection', dst_path='~/dtools/datasets/PCB Component Detection.tar')
```
The data in original format can be 🔗[downloaded here.](https://www.kaggle.com/datasets/animeshkumarnayak/pcb-fault-detection/download?datasetVersionNumber=1)