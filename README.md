# F-NVIDIA

## Some weird stuff I found out about NVIDIA GPUs / CUDA

1. `nvidia-smi` only tells you the driver version, not the CUDA version. The `CUDA Version:` shown at the top-right corner does not reflect what CUDA version you have installed at all. Instead, it just tells you the highest CUDA version the installed driver supports.

    Ref: [https://stackoverflow.com/a/55717476](https://stackoverflow.com/a/55717476)
