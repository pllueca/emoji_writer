from distutils.core import setup

setup(
    name="emoji_writer",
    version="0.0.3",
    url="https://github.com/Brinon/emoji_writer",
    author="Pablo Llueca",
    author_email="pablo.llueca@gmail.com",
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
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
