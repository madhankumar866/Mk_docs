## Points to Note:


!!! Notes
      
        Existing archicture does not have load balancer when sudden request come, The server may unable to handle it, 
        request are unable server and drop, we don't have track of dropped request

        

        To solve this we can use  Load balancer it basically does split the request when a instance or service is avaible,LB Make sure that the service is avaiable via Health check's remember it from aws load balacner column to check for  specific request.