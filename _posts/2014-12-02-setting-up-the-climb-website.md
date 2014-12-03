---
layout: post
title: "Setting up the CLIMB website"
description: ""
category: 
tags: []
---

If you have Docker installed, it is now trivially easy to set up
a working Wordpress.org installation.

For example, this Github repository will set up Wordpress using
MySQL and nginx:

 <https://github.com/eugeneware/docker-wordpress-nginx>

Forking this repository permits you to make custom configurations
to the setup.

  git clone https://github.com/eugeneware/docker-wordpress-nginx.git
  cd docker-wordpress-nginx
  sudo docker build -t="docker-climb.ac.uk" .

Then create the instance:

  sudo docker run -p 192.168.1.5:9991:80 --name docker-climb.ac.uk-test -d docker-climb.ac.uk
 
Not much more to it than this.

It should be possible now to:

* trivially make copies of the entire website,
  e.g. to make the live version
* backup the website (content, configuration)

However, I assume this Docker instance is now fairly locked into
whatever versions of MySQL and nginx etc. were used initially.
To upgrade everything will require making a new Dockerfile which
has all the files and changes associated with it?



 
