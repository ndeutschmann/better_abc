from setuptools import find_packages, setup

setup(
    package_dir={'': 'src'},
    name='better_abc',
    packages=find_packages(where="src"),
    version='0.1.0',
    description='Python ABC with a simple @abstract_property decorated checked after instantiation',
    author='Nicolas Deutschmann',
    license='MIT',
)