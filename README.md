
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


     To run Mkdocs in docker use the following command


     `https://hub.docker.com/r/squidfunk/mkdocs-material`

     docker run -d --rm -it -p 8001:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
          
