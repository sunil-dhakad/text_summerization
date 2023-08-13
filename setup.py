import setuptools

with open("README.md", "r",encoding="utf-8 ") as f:
    long_description = f.read()


    __version__= "0.0.1"
    REPO_NAME= "text_summerization"
    AUTHOR_USER_NAME="sunil-dhakad"
    SRC_REPO="textSummarizer"
    AUTHOR_EMAIL="0to1.sunil@gmail.com"



    setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for text summerization app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)