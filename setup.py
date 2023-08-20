import json
import os
from setuptools import setup


with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

setup(
    name=package_name,
    version=package["version"],
    author="lpawlick",
    packages=[package_name],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=["dash"],
    classifiers = [
        'Framework :: Dash',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Development Status :: 5 - Production/Stable'
    ],    
    project_urls={
        'Documentation': 'https://docs.pawlick.dev/projects/dash_google_picker',
        'Source': 'https://github.com/lpawlick/dash_google_picker',
        'Tracker': 'https://github.com/lpawlick/dash_google_picker/issues',
    },
    keywords='dash google file picker',
    python_requires='>=3.6',
)
