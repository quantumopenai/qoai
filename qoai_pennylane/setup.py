import setuptools

setuptools.setup(
    name='qoai_pennylane',
    version='0.0.2',
    author='QuantumOpenAI',
    author_email='team@quantumopenai.com',
    description='Xanadu Quantum API and Access Provider',
    packages=setuptools.find_packages(),
    install_requires=[
        'pennylane',
        'strawberryfields',
        'pennylane-sf'
    ],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)