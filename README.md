
        Installation For Mkdocs
    https://www.mkdocs.org/user-guide/installation/

         " pip install mkdocs "


        Installed mkdocs-material
    https://squidfunk.github.io/mkdocs-material/

         " pip install mkdocs-material "
         
    mkdocs-material is used to customized the static sites

          To run Execute      

          " mkdocs serve & "

     Use build To Generate Static Files For Hosting
          " mkdocs build "

          This will create a new directory, named site. Take a look inside " site " directory:

     Building Static Files   
     To generate static files for hosting, which creates a `site` directory:                                                   │

     ```bash
     mkdocs build
     ```
    Running in Docker
    You can also run MkDocs using the official Docker image:
    ```bash 
    docker run -d --rm -it -p 8001:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

    ## Changelog 
    See [CHANGELOG.md](CHANGELOG.md) for a history of updates and fixes.