import torch

qconfig = torch.quantization.get_default_qconfig('qnnpack') # post training quantization 

qconfig = torch.quantization.get_default_qat_qconfig('qnnpack') # quantization aware training.

# torch.backends.quantized.engine = 'qnnpack'  # para hacer inferencia