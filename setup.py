from setuptools import setup, find_packages
from pathlib import Path
from src.ansciier import __version__

ROOT = Path(__file__).parent

with open(f'{ROOT}/README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

with open(f'{ROOT}/requirements.txt', 'r', encoding='utf-8') as f:
    reqs = [req.strip() for req in f.read().strip().split('\n')]

setup(
    name='ansciier',
    version=__version__,
    author='Cudiph',
    license='MIT',
    author_email='dwiaceromo@gmail.com',
    description='Command line program to mimic any image to your terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Cudiph/ansciier',
    project_urls={
        'Bug Tracker': 'https://github.com/Cudiph/ansciier/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Topic :: Multimedia',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'Topic :: Terminals',
    ],
    entry_points = {
        'console_scripts': ['ansciier = ansciier:main'],
    },
    package_dir={'': 'src'},
    install_requires=reqs,
    packages=find_packages(where='src'),
    python_requires='>=3.6',
)
