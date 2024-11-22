from setuptools import setup, find_packages

setup(
    name="sccmwtf",
    version="1.0.0",
    author="KcanCurly",
    description="The ldap2json script allows you to extract the whole LDAP content of a Windows domain into a JSON file..",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KcanCurly/sccmwtf",
    packages=find_packages(),
    install_requires=[
        "certifi==2022.6.15",
        "cffi==1.15.1",
        "charset-normalizer==2.1.0",
        "cryptography==37.0.4",
        "idna==3.3",
        "ntlm-auth==1.5.0",
        "pyasn1==0.4.8",
        "pyasn1-modules==0.2.8",
        "pycparser==2.21",
        "requests==2.28.1",
        "requests-ntlm==1.1.0",
        "requests-toolbelt==0.9.1",
        "urllib3==1.26.10"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "sccmwtf.py=src.sccmwtf:main",
            "policysecretunobfuscate.py=src.policysecretunobfuscate:main"
        ],
    },
)