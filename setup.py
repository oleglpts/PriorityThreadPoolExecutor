from setuptools import setup

setup(
    name='PriorityThreadPoolExecutor',
    version='0.0.1',
    packages=['PriorityThreadPoolExecutor'],
    requires=[],
    url='https://github.com/oleglpts/PriorityThreadPoolExecutor',
    license='MIT',
    platforms='any',
    author='Oleg Lupats',
    author_email='oleglupats@gmail.com',
    description='Thread pool executor with priority queue',
    long_description='Thread pool executor with priority queue: '
                     'little hack of ThreadPoolExecutor from concurrent.futures.thread',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5'
    ]
)
