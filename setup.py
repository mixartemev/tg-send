from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'Telegram Bot HTTP Client'
LONG_DESCRIPTION = 'For sending reports to channel.'

# Setting up
setup(
    name="tg_bot_client",
    version=VERSION,
    author="Mike Artemiev",
    author_email="<mixartemev@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(),
    # package_dir={'': 'src'},
    install_requires=['aiohttp'], # , 'python-dotenv'
    keywords=['telegram', 'bot', 'http-client', 'api'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
    ]
)