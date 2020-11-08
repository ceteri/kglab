import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kglab",
    version="0.1.0",
    author="Paco Xander Nathan",
    author_email="paco@derwen.ai",
    description="Python wrapper for knowledge graph construction tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/DerwenAI/kglab",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Text Processing :: Indexing",
    ],
    python_requires=">=3.5",
    install_requires=[
          "python-dateutil",
          "networkx",
          "rdflib",
          "rdflib-jsonld",
    ],
    keywords="knowledge graph, graph algorithms, graph visualization, rdf, skos, owl, controlled vocabulary, n3, turtle, json-ld",
    license="MIT",
    zip_safe=False,
)