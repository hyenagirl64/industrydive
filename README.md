# Articles Demonstration Server
This is a demonstration django server for the Industry Dive Senior Software Engineer Technical Assessment. 

You must have python3 and django installed to set up and run the server.

## To Set Up
Navigate to the root directory of the project, then run the following command to initialize the database:

```
python manage.py migrate
```

## To Run
From the root directory of the project, run the following command to start the server:

```
python manage.py runserver
```

## To Use
Once the server is running, navigate to the following URL to reach the article index:

```
localhost:8000/articles/
```

There are three pages: the index page, which is the one at that url, the create page and detail pages for each article.  All are navigable via links from the index page, although the detail pages won't be viewable until articles have been created.

## System Design
In this repository is an image representing a first draft of a potential cloud based system design for this application, once productionized.

There are two major components, the Application layer and the storage layer.  Each should have a load balancer which will accept incoming requests and route them between different server nodes in the cloud.  As traffic scaled up, new nodes would be booted up to meet the demand.

In my current draft of the design, each node has it's own cache, though this could potentially be done as a service rather than a local cache.  The purpose of this cache is to store and serve articles that are currently experiencing high traffic to avoid calling the storage service.  Of particular interest is caching images in a future iteration of the articles server, as this will avoid reading them from the file system.  

My reasoning for doing this with a per-node cache rather than an external service is to improve the speed by having the cache local to the server.  The trade off is that this will increase memory consumption overall, as each node will have it's own in-memory cache.

The storage layer is a scalable read-replica database.  I think this would be a good, scalable solution for articles because I suspect there will be few writes in comparison to the volume of reads.  The load balancer would direct writes to the master node, and reads to the replica nodes as well as master.  Additional read replicas could be spun up to meeting increasing demand.

The images themselves would be stored on the file system, and need to be synchronized between nodes.  Again, this increases resource consumption, in this case hard disk usage, but would increase retrieval speed when dealing with high traffic volumes.

## Development Notes
I had a lot of fun with this project!  I definitely did not spend an hour on it!

The server code itself took me about 2 hours to complete, and the system design took another hour or so including researching various cloud solutions.  I also spent another hour preparing this README and upload the code to github.  This should give and you an idea of how much effort I put in in terms of raw coding.

However, I spent significantly more time learning Python and Django.  In addition to some prelimiary research before the interview on friday, I spent 4-5 hours on friday night going through a python tutorial, and another 4-5 hours on saturday afternoon going through a Django tutorial.  I don't consider this to be part of the "development time" exactly since doing this was also of benefit to me beyond the interivew, but I want to be up front about how much time I spent so you can make your best assessment of my abilities, both in terms of coding and in terms of learning these tools.

My overall implemention phillosophy for this project was "keep it simple to retain felxibility."  Since the project prompt said this was a "proof of concept" and that there might be additional features down the line, I decided to use as many out-of-the-box django features as possible, and to try to stick to standards.  My reasoning is that I think this will provide more flexibility as the codebase is refined in future iterations.  All of the code I wrote is easy to replace or refactor with more specific implementations.  Plus, it being a "proof of concept" where styling was optional, I mostly avoided adding features beyond the prompt unless they were short and immediately useful (headers for the pages, navigations links, using a uuid for the articles off the bat rather than an incremental id).  I also wrote the small amount of javascript used in this project directly into the relevant file, and avoided importing any libraries, to keep the javascript portion of the solution open-ended until more specific implementations and frameworks are selected down the road.  No reason to import jquery just to clear a few form fields!

Thank you for this project.  It was, frankly, the most fun I've had coding in a while.  Python is a fun language, and Django is viscerally powerful.