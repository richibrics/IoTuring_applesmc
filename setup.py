from setuptools import Extension, setup

setup(
    name='IoTuring_applesmc',
    version="1.0.0",
    ext_modules=[
        Extension(
            name='ioturing_applesmc',
            sources=['module/smc.c', 'module/smc-wrapper.c'],
            extra_link_args=['-framework', 'IOKit'],
        ),
    ],
)
