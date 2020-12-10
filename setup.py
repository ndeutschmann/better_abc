from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    package_dir={'': 'src'},
    name='abc_property',
    packages=find_packages(where="src"),
    version='1.0',
    description='Python ABC with a simple @abstract_property decorated checked after instantiation',
    author='Nicolas Deutschmann',
    license='MIT',
    url='https://github.com/ndeutschmann/better_abc',
    long_description=long_description,
    long_description_content_type="text/markdown"
)
