# F-NVIDIA

## NVIDIA GPU Hardware/Software Stack

| Layer               | Item                            | Remarks                                      |
| ------------------- | ------------------------------- | -------------------------------------------- |
| High-level Library  | PyTorch, TensorFlow, etc.       | Multiple versions can be installed, isolated |
| Low-level Library   | cuDNN                           | Multiple versions can be installed, isolated |
| Low-level Framework | CUDA Toolkit (e.g. 11.8.0)      | Multiple versions can be installed, isolated |
| Driver              | NVIDIA Driver (e.g. 535.154.05) | Single System-wide driver                    |
| Hardware            | NVIDIA GPU                      |                                              |

## Some weird stuff I found out about NVIDIA GPUs / CUDA

1. `nvidia-smi` only tells you the driver version, not the CUDA version. The `CUDA Version:` shown at the top-right corner does not reflect what CUDA version you have installed at all. Instead, it just tells you the highest CUDA version the installed driver supports.

    Ref: [https://stackoverflow.com/a/55717476](https://stackoverflow.com/a/55717476)

2. When we say 'install `CUDA`', we mean 'install the `CUDA Toolkit`'.

    - The CUDA toolkit is a collection of libraries, header files, and tools for GPU-accelerated computing.
    - The CUDA toolkit is not the same as the CUDA driver.
    - The CUDA driver is a low-level software layer that provides access to the GPU hardware for CUDA programs. The CUDA driver is required to run CUDA applications on Windows and Linux.

3. Most of the time, we do not need to install `CUDA` or `cuDNN` manually, because they are included in the PyTorch distribution when you install CUDA-enabled PyTorch via `pip` or `conda`.

    Ref: [PyTorch - Get Started Locally](https://pytorch.org/get-started/locally/)

4. However, in the event you do need to install `CUDA` and `cuDNN` manually. The installing sequence should be:

    1. Install the NVIDIA driver. (Dependent on GPU hardware & Operating system) [[NVIDIA Driver Downloads]](https://www.nvidia.com/download/index.aspx)
    2. Install the CUDA toolkit. (Dependent on NVIDIA driver)[[NVIDIA CUDA Installation Guide for Linux]](https://docs.nvidia.com/cuda/cuda-installation-guide-linux/index.html) [[CUDA Toolkit Versions]](https://developer.nvidia.com/cuda-toolkit-archive)
    3. Install cuDNN. (Dependent on CUDA toolkit) [[Installing cuDNN on Linux]](https://docs.nvidia.com/deeplearning/cudnn/install-guide/index.html)


## GPU Feature List

In the CUDA naming scheme, GPUs are named `sm_xy`, where `x` denotes the GPU generation number, and `y` the version in that generation.

| `nvcc` tags               | GPU Arch | TORCH_CUDA_ARCH_LIST | Year | GPUs           |
| ------------------------- | -------- | -------------------- | ---- | -------------- |
| `sm_50`, `sm_52`, `sm_53` | Maxwell  | `5.0`, `5.1`, `5.3`  | 2014 | GTX 9xx        |
| `sm_60`, `sm_61`, `sm_62` | Pascal   | `6.0`, `6.1`, `6.2`  | 2016 | GTX 10xx, Pxxx |
| `sm_70`, `sm_72`          | Volta    | `7.0`, `7.2`         | 2017 | Titan V        |
| `sm_75`                   | Turing   | `7.5`                | 2018 | RTX 20xx       |
| `sm_80`, `sm_86`, `sm_87` | Ampere   | `8.0`, `8.6`, `8.7`  | 2020 | RTX 30xx, Axxx |
| `sm_89`                   | Ada      | `8.9`                | 2022 | RTX 40xx, L4xx |
| `sm_90`, `sm_90a`         | Hopper   | `9.0`                | 2022 | H100           |


Ref:

- [https://stackoverflow.com/a/74962874](https://stackoverflow.com/a/74962874)
- [https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#virtual-architecture-feature-list](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/index.html#virtual-architecture-feature-list)