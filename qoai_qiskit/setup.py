import setuptools

setuptools.setup(
    name='qoai_qiskit',
    version='0.0.2',
    author='QuantumOpenAI',
    author_email='team@quantumopenai.com',
    description='Qiskit Quantum API and Access Provider',
    packages=setuptools.find_packages(),
    install_requires=[
        'qiskit'
    ],
    classifiers= [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)