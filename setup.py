from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='plumbium',
    version='0.6.1',
    packages=['plumbium', 'plumbium.recorders'],
    zip_safe=True,
    author='Jon Stutters',
    author_email='j.stutters@ucl.ac.uk',
    description='Record the inputs and outputs of scripts',
    long_description=readme(),
    url='https://github.com/jstutters/plumbium',
    install_requires=['wrapt'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    license='MIT',
    classifiers=[
    ]
)
