from setuptools import setup, find_packages

setup(
    name='pdfzoomer',
    version='0.1',
    author='Marco Madera',
    author_email='me@marcomadera.com',
    description='A Python library for cropping PDF pages',
    long_description='PDF Zoomer is a Python tool for cropping and resizing PDF files.',
    url='https://github.com/MarcoMadera/pdfzoomer',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pdfzoomer=pdfzoomer.zoomer:main'
        ]
    },
    install_requires=[
        'PyPDF2'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)