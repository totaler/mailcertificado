# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='mailcertificado',
    version='0.0.1-dev',
    url='',
    author='Joan Manuel Grande',
    author_email='totaler@gmail.com',
    packages=['mailcertificado'],
    install_requires=['suds', 'PyPDF2'],
    license='GPLv3',
    description='MailCertificado',
    long_description=open('README.md').read(),
)