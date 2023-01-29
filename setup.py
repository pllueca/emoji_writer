from distutils.core import setup

setup(
    name="EmojiWriter",
    version="0.2dev",
    url="https://github.com/Brinon/emoji_writer",
    author="Pablo Llueca",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=[
        "emoji_writer",
    ],
    license="Creative Commons Attribution-Noncommercial-Share Alike license",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    entry_points={"console_scripts": ["emoji_writer = main:main"]},
)
