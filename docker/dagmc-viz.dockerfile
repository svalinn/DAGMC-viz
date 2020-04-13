FROM  svalinn/pymoab-py2-18.04

# ubuntu setup
RUN apt-get update
RUN apt-get install -y --fix-missing \
    wget \
    cpio \
    libpcre3-dev \
    libpython-dev \
    libgl1-mesa-glx \
    libgl1-mesa-dev \
    libsm6 \
    libxt6 \
    libglu1-mesa

# pytest setup
RUN pip install xmldiff

# install VisIt
RUN cd $HOME/opt \
    && wget http://portal.nersc.gov/project/visit/releases/2.13.3/visit2_13_3.linux-x86_64-ubuntu18.tar.gz \
    && wget http://portal.nersc.gov/project/visit/releases/2.13.3/visit-install2_13_3 \
    && echo 1 > input \
    && bash visit-install2_13_3 2.13.3 linux-x86_64-ubuntu18 /usr/local/visit < input

# set environment variables
ENV PATH /usr/local/visit/bin:$PATH
ENV LD_LIBRARY_PATH /usr/local/visit/2.13.3/linux-x86_64/lib/:$LD_LIBRARY_PATH
ENV PYTHONPATH /usr/local/visit/2.13.3/linux-x86_64/lib/site-packages:$PYTHONPATH
