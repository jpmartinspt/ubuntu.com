# ![ubuntu](https://assets.ubuntu.com/v1/9f61b97f-logo-ubuntu.svg "Ubuntu").com codebase

[![CircleCI build status](https://circleci.com/gh/canonical-web-and-design/ubuntu.com.svg?style=shield)](https://circleci.com/gh/canonical-web-and-design/ubuntu.com) [![Code coverage](https://codecov.io/gh/canonical-web-and-design/ubuntu.com/branch/master/graph/badge.svg)](https://codecov.io/gh/canonical-web-and-design/ubuntu.com)

Ubuntu is an open source software operating system that runs from the desktop, to the cloud, to all your internet connected things. [Ubuntu.com](https://ubuntu.com) is the website that helps people learn about, download and get started with Ubuntu. This repo is the codebase and content for the [ubuntu.com](https://ubuntu.com) website.

The site is largely maintained by the [Web and Design team](https://ubuntu.com/blog/topics/design) at [Canonical](https://www.canonical.com). It is a simple, database-less, informational website project based on [Flask](https://flask.palletsprojects.com/en/1.1.x/) and hosted on a [Charmed Kubernetes](https://ubuntu.com/kubernetes) cluster.

## Bugs and issues

If you have found a bug on the site or have an idea for a new feature, feel free to [create a new issue](https://github.com/canonical-web-and-design/ubuntu.com/issues/new), or suggest a fix by [creating a pull request](https://help.github.com/articles/creating-a-pull-request/). You can also find a link to create issues in the footer of every page of the site itself.

If you have found a bug in the Ubuntu OS itself, the please file it [here](https://bugs.launchpad.net/ubuntu/).

## Local development

The simplest way to run the site locally is to first [install Docker](https://docs.docker.com/engine/installation/) (on Linux you may need to [add your user to the `docker` group](https://docs.docker.com/engine/installation/linux/linux-postinstall/)), and then use the `./run` script:

``` bash
./run
```

Once the containers are setup, you can visit <http://127.0.0.1:8001> in your browser.

For more detailed local development instructions, see [HACKING.md](HACKING.md).

## License

The content of this project is licensed under the [Creative Commons Attribution-ShareAlike 4.0 International license](https://creativecommons.org/licenses/by-sa/4.0/), and the underlying code used to format and display that content is licensed under the [LGPLv3](http://opensource.org/licenses/lgpl-3.0.html) by [Canonical Ltd](http://www.canonical.com/).


With ♥ from Canonical
