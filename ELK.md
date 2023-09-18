<h1>ELK</h1>
<h2>Introduction</h2>
<!-- <h3>What is the ELK Stack?</h3> -->
The ELK Stack is a powerful collection of three open-source tools—Elasticsearch, Logstash, and Kibana—that together enable businesses to search, analyze, and visualize data in real-time. Initially comprising three main components (hence the acronym ELK), the stack has since expanded to include a rich ecosystem of tools, most notably Beats, to provide additional functionalities like data shipping and metric collection.



<h4>Elasticsearch</h4>
Elasticsearch is the heart of the ELK Stack, serving as its search and analytics engine. Built on top of the Lucene library, Elasticsearch is designed for horizontal scalability and distributed, real-time search capabilities. Whether it is textual content, numerical data, or even structured data, Elasticsearch can efficiently index, search, and analyze it.
<h4>Logstash</h4>
Logstash is the data processing component of the ELK Stack. It is responsible for aggregating data from various sources, transforming it, and then sending it to Elasticsearch or other specified destinations. Logstash can handle a variety of data formats and offers an extensive array of input, filter, and output plugins for more tailored data processing.
<h4>Kibana</h4>
Kibana serves as the front-end UI for the ELK Stack. It provides an intuitive interface for exploring, visualizing, and managing the data stored in Elasticsearch. Kibana’s capabilities range from creating real-time dashboards to analyzing trends, thus facilitating actionable insights.

<h3>The Role of Beats: Filebeat and Metricbeat</h4>
Though not initially part of the ELK stack, Beats have become an indispensable addition to the ecosystem. They are lightweight, single-purpose data shippers designed to send different types of data to or from Elasticsearch and Logstash.

<h4>Filebeat</h4>
Filebeat is responsible for forwarding and centralizing log data. It’s designed to be lightweight and keeps resource utilization to a minimum. Filebeat tails log files on your servers and forwards the log entries to either Elasticsearch or Logstash for indexing.

<h4>Metricbeat</h4>
Metricbeat, on the other hand, is used for collecting metrics from the operating system and services running on a server. Metricbeat then takes these metrics and statistics and ships them to the output that you specify, such as Elasticsearch or Logstash.
<h1>Elasticsearch</h1>

<h2>Set up </h2>

- **Install Elasticsearch from archive on Linux or MacOS**
- **Install Elasticsearch with .zip on Windows**
- **Install Elasticsearch with RPM**
- **Install Elasticsearch with Docker**


<h4>Install Elasticsearch with Docker</h4>

```sh
docker pull docker.elastic.co/elasticsearch/elasticsearch:[version]
```


<h4>Elasticsearch Service Configuration for Docker Compose File</h4>

```yaml
es01:
  image: docker.elastic.co/elasticsearch/elasticsearch:${STACK_VERSION}  # Elasticsearch Docker image with version
  networks:
    - elastic  # Network name
  ports:
    - 9200:9200  # Port mapping
  volumes:
    - esdata01:/usr/share/elasticsearch/data  # Persistent data volume
    - certs:/usr/share/elasticsearch/config/certs  # Certificate volume
    - ./synonym.txt:/usr/share/elasticsearch/config/synonyms/synonym.txt  # Synonyms file volume
    - ./stop_words.txt:/usr/share/elasticsearch/config/stop_words.txt  # Stop words file volume
  environment:
    - node.name=es01  # Node name
    - cluster.name=${CLUSTER_NAME}  # Cluster name
    - discovery.type=single-node  # Single-node discovery type
    - ELASTIC_PASSWORD=${ELASTIC_PASSWORD}  # Password for Elasticsearch
    - bootstrap.memory_lock=true  # Lock the process address space into RAM
    - xpack.security.enabled=true  # Enable X-Pack security
    - xpack.security.http.ssl.enabled=true  # Enable SSL for HTTP
    - xpack.security.http.ssl.key=certs/es01/es01.key  # SSL key for HTTP
    - xpack.security.http.ssl.certificate=certs/es01/es01.crt  # SSL certificate for HTTP
    - xpack.security.http.ssl.certificate_authorities=certs/ca/ca.crt  # Certificate authorities for HTTP SSL
    - xpack.security.transport.ssl.enabled=true  # Enable SSL for transport layer
    - xpack.security.transport.ssl.key=certs/es01/es01.key  # SSL key for transport layer
    - xpack.security.transport.ssl.certificate=certs/es01/es01.crt  # SSL certificate for transport layer
    - xpack.security.transport.ssl.certificate_authorities=certs/ca/ca.crt  # Certificate authorities for transport SSL
    - xpack.security.transport.ssl.verification_mode=certificate  # SSL verification mode for transport
    # - xpack.security.http.ssl.client_authentication=required  # Uncomment if client authentication is required
    - xpack.license.self_generated.type=${LICENSE}  # License type
  mem_limit: ${MEM_LIMIT}  # Memory limit
  ulimits:
    memlock:
      soft: -1  # Soft limit for memory lock
      hard: -1  # Hard limit for memory lock
  restart: always  # Always restart the service if it stops
```

<h5>Environment Variable Explanations</h5>

**ELASTIC_PASSWORD**: Sets the password for the Elasticsearch user.
**bootstrap.memory_lock=true**: Locks the process address space into RAM, preventing Elasticsearch from swapping to disk, which is crucial for performance.
**xpack.security.enabled=true**: Enables X-Pack security features like authentication and role-based access control.
**xpack.security.http.ssl.enabled=true**: Enables SSL for HTTP communication