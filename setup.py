import io
import os.path
from setuptools import setup

path = os.path.join(os.path.dirname(__file__), 'README.rst')
with io.open(path, encoding='utf8') as f:
    LONG_DESCRIPTION = f.read()

install_requires = [
    "pgzero>=1.2"
]

setup(
    name='pgzhelper',
    version='1.0b0',
    description="Pygame Zero Helper enhance Pygame Zero with additional capabilities",
    long_description=LONG_DESCRIPTION,
    author='Cort',
    author_email='cort@cortscorner.net',
    url='https://www.aposteriori.com.sg/pygame-zero-helper/',
    include_package_data=True,
    py_modules=['pgzhelper'],
    install_requires=install_requires,
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Education',
        'Topic :: Games/Entertainment',
    ]
)
