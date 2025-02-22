from setuptools import setup, find_packages


setup(
    name='anonfile_uploader',
    version='0.1.2',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=['requests'],
    author='rkndeveloper',
    author_email='rkndeveloper935@gmail.com',
    description='A simple Python library to upload files to anonfile.la',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/RknDeveloper/anonfile-uploader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
