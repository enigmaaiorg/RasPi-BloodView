# pip install coremltools==4.0b2
# pip install -r requirements.txt 
# pip install onnx>=1.7.0

import os

def export_JIT():

    # correction in the line 53 in export.py from original repo
    os.system('python ./../yolo-v5/models/export.py --weights ./runs/FINAL/weights/best.pt --img 640 --batch 1')


if __name__ == '__main__':
    export_JIT()
    
'''

(Pytorch) D:\TRABAJOS\PROYECTOS\ENIGMA\RasPi-BloodView\Blood-Detector>python export_jit.py
Namespace(batch_size=1, img_size=[640, 640], weights='./runs/FINAL/weights/best.pt')
Fusing layers... 
Model Summary: 140 layers, 7.25191e+06 parameters, 0 gradients

Starting TorchScript export with torch 1.6.0...
./../yolo-v5\models\yolo.py:48: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  if self.grid[i].shape[2:4] != x[i].shape[2:4]:
D:\ANACONDA\envs\Pytorch\lib\site-packages\torch\jit\__init__.py:1109: TracerWarning: Encountering a list at the output of the tracer might cause the trace to be incorrect, this is 
only valid if the container structure does not change based on the module's inputs. Consider using a constant container instead (e.g. for `list`, use a `tuple` instead. for `dict`, 
use a `NamedTuple` instead). If you absolutely need this and know the side effects, pass strict=False to trace() to allow this behavior.
  module._c._create_method_from_trace(method_name, func, example_inputs, var_lookup_fn, strict, _force_outplace)
TorchScript export success, saved as ./runs/FINAL/weights/best.torchscript.pt

Starting ONNX export with onnx 1.8.0...
./../yolo-v5\models\yolo.py:48: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  if self.grid[i].shape[2:4] != x[i].shape[2:4]:
ONNX export success, saved as ./runs/FINAL/weights/best.onnx
scikit-learn version 0.23.1 is not supported. Minimum required version: 0.17. Maximum required version: 0.19.2. Disabling scikit-learn conversion API.

Starting CoreML export with coremltools 4.0b2...
CoreML export failure: module 'torch._C' has no attribute '_jit_pass_canonicalize_ops'

Export complete (25.10s). Visualize with https://github.com/lutzroeder/netron.
'''