# Costa Rica Stock Exchange Data Harvester
Costa Rica Stock Exchange (Bolsa Nacional de Valores de Costa Rica) data harvester for **ETL batch processing data pipeline**.
This module is an integral component for the financial web-based application: [Inverso](https://inverso.andres-montero.me/).

![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

## Table of contents

* [Costa Rica Stock Exchange Data Harvester](#costa-rica-stock-exchange-data-harvester)
  * [Table of contents](#table-of-contents)
  * [Description](#description)
  * [Data harvest phases](#data-harvest-phases)
    * [Data sourcing](#data-sourcing)
    * [Relevant data extraction](#relevant-data-extraction)
    * [Data normalization](#data-normalization)
    * [Output](#output)
  * [Intended deploy architecture](#intended-deploy-architecture)
  * [Legal disclaimer](#legal-disclaimer)
  * [Author](#author)
  * [License](#license)

## Description

This module gathers, discriminates and normalizes relevant data from daily session records of the Costa Rica Stock Exchange.
Data is retrieved from the public web API of the Costa Rica Stock Exchange.
Once information has been transformed, it is prepared for storage in a data warehouse or data lake awaiting further processing and insight extraction.

## Data harvest phases

The data harvest process comprises the four phases enumerated down below. This sequence of steps transforms raw data into refined and structure information.

1. Data sourcing.
2. Relevant data extraction.
3. Data normalization.
4. Output.

### Data sourcing

The initial phase of the data harvester operates by interfacing with the public web API of the Costa Rica Stock Exchange to retrieve daily session records. Data acquisition is performed through HTTP GET requests. The resultant output is a Microsoft Excel file, encompassing approximately 43 columns and exceeding 1000 rows. The file is loaded into memory as a Pandas DataFrame for transformation in coming phases. 

### Relevant data extraction

The raw data retrieved from the web service in the preceding phase is subsequently resized, reducing the number of columns and retaining only those pertinent for value extraction later on. Among the preserved columns, notable ones include: ISIN, maturity, price, rate, yield, currency, issuer, among others.

### Data normalization

The dataset is normalized through string formatting, such as space removal, separator substitution, accents removal, and character lowercase; conversion of binary values to boolean type, and transformation of repetitive data into referential data structures.

### Output

As a result of the data harvesting process, the module generates enriched files in CSV format, prepared for storage in data lakes or data warehouses awaiting further processing and value extraction. Additionally, the system produces a detailed operations log for control purposes.

Examples of both the refined data files and the operations log from the data harvesting process are available for reference. These can be found in the repository folders labeled "harvest_result" and "logs".

## Intended deploy architecture

As stated before, this module constitutes an integral component within an Extract, Transform, Load (ETL) batch processing data pipeline. The intended deployment architecture for this data management system adheres to a **serverless paradigm** through Amazon Web Services (AWS) infrastructure. This arrangement underscores a scalable and resource-efficient approach, wherein computational resources are dynamically allocated and managed by AWS, thereby optimizing operational efficiency and minimizing administrative overhead.

The AWS architecture diagram down below describes how data flows from different sources through an ETL data pipeline, and as result generates refined information files to be stored awaiting further processing.

![CRSE data harvester base deploy architecture](deploy_architecture_diagrams/crse-architecture-diagram%20-%20crse-architecture-diagram.jpg)

A variation of the pipeline output model can be achieved through the establishment of a linkage between the resultant data lake and SQL or NoSQL databases, thereby enabling seamless integration with external services for consumption. Example given, the financial web-based application [Inverso](https://inverso.andres-montero.me/) retrieves Costa Rica Stock Exchange session record data from a relational database connected to the pipeline.  

![CRSE data harvester deploy architecture for interface consumption](deploy_architecture_diagrams/crse-architecture-diagram%20-%20crse-architecture-diagram-consumption.jpg)
![CRSE data harvester deploy architecture for end-user consumption](deploy_architecture_diagrams/crse-architecture-diagram%20-%20crse-architecture-diagram-end-user-consumption.jpg)


## Legal disclaimer
  
The Costa Rica Stock Exchange Data Harvester functions exclusively as a data processing tool, furnishing end-users with an interface for data consumption and manipulation. It explicitly disclaims any ownership or possession of the data processed through its system. Consequently, it absolves itself of any responsibility for the subsequent utilization and compliance with data rights by end-users.

This piece of software has been developed for personal purposes and is not intended for commercial profit. 
The primary goal of this exercise is to provide the developer a learning and research environment.


## Author

**Andrés Montero Gamboa**<br>
Computing Engineering Undergraduate<br>
Instituto Tecnológico de Costa Rica<br>
[LinkedIn](https://www.linkedin.com/in/andres-montero-gamboa) | [GitHub](https://github.com/andresmg07)

## License

MIT License

Copyright (c) 2024 Andrés Montero Gamboa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
