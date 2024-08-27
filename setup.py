from setuptools import setup, find_packages
#Command line tool assisstence found at: https://www.codium.ai/blog/creating-powerful-command-line-tools-in-python-a-practical-guide/
setup(
    name='generals_tool',
    version='0.1',
    packages=find_packages(),
    py_modules=['Task', 'taskTest'],
    entry_points={
        'console_scripts': [
            'process_generals=Task:main',
            'test_generals=taskTest:main',
        ],
    },
    install_requires=[
        'pandas',
    ],
    author='Bryant Reese',
    description='Tool for GeneralsPerformance dataset which sorts to above 3 battle and by aWAR.',
)