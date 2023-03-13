from setuptools import setup, find_packages


setup(
    name='sysaidclient',
    version='0.01',
    author='Daniel Gumbleton-Wood, Archie Fergurson',
    description='Wrapper for SysAid API',
    keywords=[],
    url='https://github.com/DanielGumbletonWood/python_sysaid',
    packages=find_packages(),
    scripts=[],
    install_requires=['requests'],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
)
