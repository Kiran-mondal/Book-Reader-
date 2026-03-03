from setuptools import setup, find_packages

setup(
 name="ai-book-recommender",
 version="1.0.0",
 description="AI-powered book recommendation system",
 long_description=open("README.md").read(),
 long_description_content_type="text/markdown",
 author="Your Name",
 author_email="your.email@example.com",
 url="https://github.com/yourusername/ai-book-recommender",
 packages=find_packages(),
 include_package_data=True,
 install_requires=[
 "flask==2.3.3",
 "pandas==2.0.3",
 "numpy==1.24.3",
 "scikit-learn==1.2.2",
 "streamlit==1.25.0",
 "transformers==4.33.4",
 "torch==2.0.1",
 ],
 python_requires=">=3.8",
 classifiers=[
 "Development Status :: 5 - Production/Stable",
 "Intended Audience :: Developers",
 "License :: OSI Approved :: MIT License",
 "Programming Language :: Python :: 3.8",
 "Programming Language :: Python :: 3.9",
 "Programming Language :: Python :: 3.10",
 ],
 entry_points={
 "console_scripts": [
 "ai-recommender=app:main",
 ],
 },
)
