import setuptools

VERSION = '0.0.1' 
DESCRIPTION = 'My first Python package'
LONG_DESCRIPTION = 'My first Python package with a slightly longer description'

# Setting up
setuptools.setup(
       # the name must match the folder name 'verysimplemodule'
        name="mypackage", 
        version=VERSION,
        # author="Md Meraz",
        # author_email="merazlab@gmail.com",
        description="NEW calc",
        # long_description="New calcLONG_DESCRIPTION",
        packages=setuptools.find_packages(),
        # install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

)