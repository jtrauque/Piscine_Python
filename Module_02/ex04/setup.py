import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="my_minipack",
    version="1.0.0",
    author="jtrauque",
    author_email="jtrauque@student.42.fr",
    description="A small example package in python",
    classifiers=[
		"Developpement Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Intended Audience :: Students",
		"Topic :: Eductation",
		"Topic :: HowTo",
		"Topic :: Package",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
