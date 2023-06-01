# Load Balancer Configuration

This repository provides instructions for configuring a load balancer and setting up custom HTTP response headers on web servers. The project aims to automate the configuration process and ensure the smooth distribution of traffic across multiple web servers.

## Task 0: Double the number of webservers

### Requirements
- Configure Nginx on web-01 and web-02 to include a custom HTTP response header.
- The custom header must be named "X-Served-By".
- The value of the custom header should be the hostname of the server running Nginx.
- Use the provided script `0-custom_http_response_header` to configure a new Ubuntu machine.

## Task 1: Install your load balancer

### Requirements
- Install and configure HAproxy on the lb-01 server.
- HAproxy should distribute traffic to web-01 and web-02 using a round-robin algorithm.
- Ensure HAproxy can be managed via an init script.
- Make sure the servers are configured with the correct hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.

