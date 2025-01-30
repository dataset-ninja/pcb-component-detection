Dataset **PCB Component Detection** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzk4NV9QQ0IgQ29tcG9uZW50IERldGVjdGlvbi9wY2ItY29tcG9uZW50LWRldGVjdGlvbi1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICI2ZE9uUnQyWUJWNzhUcTlKVDJ0UWJNOTg3ZGh2dCtZS2IyVTQxZ3ROZXhFPSJ9)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='PCB Component Detection', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/animeshkumarnayak/pcb-fault-detection/download?datasetVersionNumber=1).