import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="mozambique",
    version="0.1",
    author="Ariel Nunez, Jeffrey Johnson",
    author_email="ingenieroariel@gmail.com",
    description="Code behind moz-adapt",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: GNU Library or General Public License (GPL)',
    ],
    license="GPL 3",
    keywords="horn of africa geonode django",
    url='https://github.com/gfdrr/mozambique',
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
