The notebooks use python 3.9 and the libraries in requirements.txt

Need to use conda on the datateam server in order to use python 3.9

Here is how to miniconda if you need it:
```
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
```

To create a new environment and install requirements:
```
conda create -n scale_comp python=3.9
conda activate scale_comp
pip install -r requirements.txt
```

You will also need `libspatialindex` installed: here are instructions to install [`libspatialindex`](https://libspatialindex.org/en/latest/) or [`libspatialindex-dev`](https://packages.ubuntu.com/bionic/libspatialindex-dev)