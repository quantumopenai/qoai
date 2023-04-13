import setuptools

setuptools.setup(
    name='qoai_cirq',
    version='0.0.1',
    author='QuantumOpenAI',
    author_email='team@quantumopenai.com',
    description='Cirq Quantum API and Access Provider',
    packages=setuptools.find_packages(),
    install_requires=[
        'cirq'
    ],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)