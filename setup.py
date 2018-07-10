import setuptools
import versioneer

if __name__ == "__main__":
    setuptools.setup(
        name='molssidevops',
        version=versioneer.get_version(),
        cmdclass=versioneer.get_cmdclass(),
        # version="1",
        description='Example project for the MolSSI Bootcamp',
        author='Matt Mansell',
        url="https://github.com/mmansell7/molssidevops",
        license='BSD 3-C',
        packages=setuptools.find_packages(),
        install_requires=[
        
        ],
        extras_require={
            'docs': [
                'sphinx==1.2.3',  # autodoc was broken in 1.3.1
                'sphinxcontrib-napoleon',
                'sphinx_rtd_theme',
                'numpydoc',
            ],
            'tests': [
                'pytest>=3.0',
                'pytest-cov',
                'codecov'
            ],
            'develop': [     # extra
                'yapf',
                'versioneer'
           ]
        },

        tests_require=[
            'pytest',
        ],
        zip_safe=True,
    )
