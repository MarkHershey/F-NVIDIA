# F-NVIDIA

## Some weird stuff I found out about NVIDIA GPUs / CUDA

1. `nvidia-smi` only tells you the driver version, not the CUDA version. The `CUDA Version:` shown at the top-right corner does not reflect what CUDA version you have installed at all. Instead, it just tells you the highest CUDA version the installed driver supports.

    Ref: [https://stackoverflow.com/a/55717476](https://stackoverflow.com/a/55717476)

2. When we say 'install `CUDA`', we mean 'install the `CUDA Toolkit`'.

    - The CUDA toolkit is a collection of libraries, header files, and tools for GPU-accelerated computing.
    - The CUDA toolkit is not the same as the CUDA driver.
    - The CUDA driver is a low-level software layer that provides access to the GPU hardware for CUDA programs. The CUDA driver is required to run CUDA applications on Windows and Linux.

3. Most of the time, we do not need to install `CUDA` or `cuDNN` manually, because they are included in the PyTorch when you install CUDA-enabled PyTorch via `pip` or `conda`.

    Ref: [PyTorch - Get Started Locally](https://pytorch.org/get-started/locally/)

4. However, in the event you do need to install `CUDA` and `cuDNN` manually. The installing sequence should be:

    1. Install the NVIDIA driver. [NVIDIA Driver Downloads](https://www.nvidia.com/download/index.aspx)
    2. Install the CUDA toolkit. [NVIDIA CUDA Installation Guide for Linux](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html)
    3. Install cuDNN. [Installing cuDNN on Linux](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)
