from setuptools import setup

setup(name='myfirstmodule',
    version='0.1',
    packages=['myfirstmodule'],
    install_requires=[
        'markdown',
    ],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['myfirstmodule=myfirstmodule.command_line:main']
    },
    include_package_data=True,
)