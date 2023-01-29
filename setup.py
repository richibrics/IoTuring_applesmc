from setuptools import Extension, setup

setup(
    name='IoTuring_applesmc',
    version="v2023.1.1",
    ext_modules=[
        Extension(
            name='ioturing_applesmc',
            sources=['module/smc.c', 'module/smc-wrapper.c'],
            extra_link_args=['-framework', 'IOKit'],
        ),
    ],
)
