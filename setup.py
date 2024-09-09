from setuptools import setup, find_packages

setup(
    name='sierra-testing',  # Replace with your package name
    version='0.1.0',  # Version of your package
    description='A brief description of your package',  # Short description
    long_description=open('README.md').read(),  # Detailed description from README
    long_description_content_type='text/markdown',  # The format of the long description (e.g., Markdown)
    author='Samuel Gómez',  # Your name or your team’s name
    author_email='samuel.gomez.balderas@gmail.com',  # Your email address
    url='https://github.com/yourusername/your-repo',  # URL of the package’s GitHub repository
    packages=find_packages(exclude=['test*']),  # Automatically finds all sub-packages
    include_package_data=True,  # Include data from MANIFEST.in
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Choose an appropriate license
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify Python version compatibility
)
