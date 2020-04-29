from setuptools import Extension, find_namespace_packages, setup

setup(
    name="cython_example",
    version="0.1.0",
    description="Minimal working example of a package using Cython extension.",
    author="Libor Martinek",
    author_email="libasmartinek@protonmail.com",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    ext_modules=[
        Extension(
            "cython_example.cythonized_ext",
            sources=["src/cython_example/cythonized_ext/example_cython.pyx"],
        ),
    ],
    install_requires=["cython"],
    setup_requires=["cython"],
)
