from setuptools import setup

setup(
    name='issorting_package',
    version='0.1',
    description='This a package for sorting arrays using various algorithms. Idea from:https://www.dataquest.io/blog/python-projects-for-beginners/',
    py_modules=['sorting_package'],
    entry_points={
        'console_scripts': [
            'bubble_sort=sorting_package:bubble_sort',
            'quick_sort=sorting_package:quick_sort'
        ]
    },
    author='Ife-Michaela Spencer',
    author_email='21itmj@gmail.com',
    url='https://github.com/iffysravioli/sort',
    license='MIT',
    keywords='sorting algorithms'
)
