import pynvml


def check():
    pynvml.nvmlInit()

    driver_version = pynvml.nvmlSystemGetDriverVersion()
    print(f"NVIDIA Driver Version: {driver_version}")

    device_count = pynvml.nvmlDeviceGetCount()
    print(f"Device Count: {device_count}")

    devices = []

    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        # print("Handle:", handle)

        uuid = pynvml.nvmlDeviceGetUUID(handle)

        device_name = pynvml.nvmlDeviceGetName(handle)
        print(f"  - GPU {i}: {device_name} (uuid: {uuid})")

        info = pynvml.nvmlDeviceGetMemoryInfo(handle)
        mem_total = info.total / 1024**3
        mem_used = info.used / 1024**3
        mem_free = info.free / 1024**3

        free_ratio = mem_free / mem_total * 100
        used_ratio = mem_used / mem_total * 100

        print(f"    - Total Memory: {mem_total:.1f} GB")
        print(f"    - Free Memory : {mem_free:.1f} GB ({free_ratio:.1f}%)")
        print(f"    - Used Memory : {mem_used:.1f} GB ({used_ratio:.1f}%)")

        devices.append(
            dict(
                index=i,
                uuid=uuid,
                name=device_name,
                total=mem_total,
                used=mem_used,
                free=mem_free,
                free_ratio=free_ratio,
                used_ratio=used_ratio,
            )
        )

    return dict(
        driver_version=driver_version,
        device_count=device_count,
        devices=devices,
    )


if __name__ == "__main__":
    info = check()
    # print(info)
