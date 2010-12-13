from setuptools import setup, find_packages

setup(
    name='django-orderedrelations',
    version='0.0.1',
    description='Django app allowing to sort relationships via admin inlines.',
    author='Praekelt Foundation',
    author_email='dev@praekelt.com',
    url='http://github.com/praekelt/django-orderedrelations',
    packages = find_packages(),
    include_package_data=True,
)
