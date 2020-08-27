FROM ubuntu:20.04
LABEL maintainer="NCAR XDev Team <xdev@ucar.edu>"

ENV DEBIAN_FRONTEND noninteractive
ENV LANG C.UTF-8

RUN \
    apt-get update --fix-missing               && \
    apt-get upgrade --yes                      && \
    apt-get install --yes   \
    bzip2 \
    curl \
    git \
    libffi-dev \
    lsb-release \
    tzdata \
    nano \
    vim \
    wget \
    ca-certificates

RUN \
    apt-get clean

# Set Mountain Time timezone
ENV TZ=America/Denver

RUN \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime    &&  \
    echo $TZ > /etc/timezone


RUN \
    wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/miniconda3                                  && \
    rm ~/miniconda.sh                                                               && \
    ln -s /opt/miniconda3/etc/profile.d/conda.sh /etc/profile.d/conda.sh            && \
    echo ". /opt/miniconda3/etc/profile.d/conda.sh" >> ~/.bashrc                    && \
    /opt/miniconda3/bin/conda config --set always_yes true --set changeps1 false    && \
    /opt/miniconda3/bin/conda config --set add_pip_as_python_dependency true        && \
    /opt/miniconda3/bin/conda config --set pip_interop_enabled true                 && \
    /opt/miniconda3/bin/conda config --add channels conda-forge                     && \
    /opt/miniconda3/bin/conda update --all

RUN \
    /opt/miniconda3/bin/conda install                     \
        alembic             \
        attrs               \
        certipy             \
        cryptography        \
        decorator           \
        entrypoints         \
        jinja2              \
        jsonschema          \
        jupyterhub==1.1.0   \
        mako                \
        markupsafe          \
        more-itertools      \
        nodejs              \
        oauthlib            \
        pamela              \
        psycopg2            \
        pyopenssl           \
        pyrsistent          \
        python-dateutil     \
        python-editor       \
        python-json-logger  \
        ruamel.yaml         \
        ruamel.yaml.clib    \
        sqlalchemy          \
        tornado             \
        traitlets           \
        zipp

ENV PATH=/opt/miniconda3/bin:$PATH
WORKDIR /tmp

RUN \
    npm install -g configurable-http-proxy                                  &&  \
    git clone https://github.com/jupyterhub/jupyterhub.git                  &&  \
    cd jupyterhub                                                           &&  \
    git checkout tags/1.1.0                                                 &&  \
    cp examples/cull-idle/cull_idle_servers.py /opt/miniconda3/bin/.        &&  \
    chmod u+x /opt/miniconda3/bin/cull_idle_servers.py                      &&  \
    rm -rf ~/.cache ~/.npm && \
    /opt/miniconda3/bin/conda list && \
    /opt/miniconda3/bin/conda clean -aftipsy
