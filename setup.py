try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='compphys',
    version='0.1',
    description='Effective Computation in Physics',
    author='Anthony Scopatz and Kathryn D. Huff',
    author_email='koolkatz@gmail.com',
    url='http://physics.codes',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    license='BSD-3-Clause',
    zip_safe=False,
    packages=['compphys', 'compphys.more', 'compphys.tests'],
    package_dir={
        'compphys': 'compphys',
        'compphys.more': 'compphys/more',
        'compphys.tests': 'compphys/tests',
        },
    include_package_data=True,

    # or you can specify explicitly:
    package_data={
        'compphys': ['assets/*.txt']
        },
)

if __name__ == "__main__":
    setup()
