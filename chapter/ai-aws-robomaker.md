# RoboMaker on AWS sp20-516-223 Rahul Dharmchand 

* Rahul Dharmchand
* [sp20-516-223](https://github.com/cloudmesh-community/sp20-516-223) 
* [ai-aws-robomaker.md](https://github.com/cloudmesh-community/sp20-516-223/blob/master/chapter/ai-aws-robomaker.md)

## Introduction

Human's invented (and still inventing) many things to make human life easier. Some of the greatest inventions like 
**wheels, airplanes, telephone** completed changed the way we travel and communicate. Computers and the Internet belong
 to this elite category which has disrupted the way we interact, gossip, read, learn, entertain and even think. 
 
We also are passionate to make machines more human. 
Due to lack of advanced technology this passion could not be realized till now. But now it is possible using  **AI**, **ML** and **cloud computing**. 
AWS RoboMaker is one such service from Amazon.

### Software vs Robot Applications
 
Unlike software development, robot applications development and testing are more complex as they involves hardware
 parts. Software can be easily tested on computers, but testing robot applications by deploying to robots is not
  always feasible because the cost of hardware and building a robot will be high. A sophisticated simulation is
   required to create 3D model and test the robot application before they can be deployed on to the robot for final
    testing in the real world. 

## AWS RoboMaker

AWS RoboMaker [sp20-516-223-aws-rm] service was introduced by Amazon in late 2018 to make robot application development
and testing easier and cost-effective. This service provides a development environment to build robot applications, 
simulation to test the applications and deployment manager to deploy these applications on either a single robot or to a
 fleet of robots.

### AWS RoboMaker Features

AWS RoboMaker provides the following features [@sp20-516-223-aws-rm-ft]

* [Cloud extension for ROS](#Cloud-Extension-for-ROS)
* [Development environment](#Development-environment)
* [Simulation](#Simulation)
* [Fleet management](#Fleet-Management)

#### Cloud Extension for ROS

ROS (Robot Operating System) was created at Stanford in 2007 as open source project. ROS provides software libraries 
to build robot applications and is widely used as default operating system in most of the modern-day robots. AWS
 RoboMaker provides the cloud extension for ROS to make it easier to integrate with other AWS services to delegate
resource intensive tasks and freeing up robots to focus on main tasks. 

Out of box services that are supported with this ROS extension are

* Computer vision with Amazon Kinesis [sp20-516-223-aws-rm-kinesis] and Amazon Rekognition [sp20-516-223-aws-rm-rekognition]
* Voice command with Amazon Lex and Amazon Polly [sp20-516-223-aws-rm-polly]
* Monitoring and logging with Amazon CloudWatch [sp20-516-223-aws-rm-cloudwatch]

#### Development Environment  

One way to develop robot application is to setup a machine with all the required software. This will require to
 invest in high end machines as well as periodically keep maintaining the installed software.  

AWS RoboMaker provides a development environment to build and edit robot application online. No software to installation
 or maintenance required. RoboMaker development environment provides a fully-featured editor and pre-configured ROS
  tools with AWS Cloud9. Many sample application are available for reference and to quick start the development. 

#### Simulation

Testing the robot application in real-world with a complex and constantly changing environment will require a lot of
 investment in setting up such an environment as well as building the physical robot itself. AWS RoboMaker provides a
  full-featured simulation service using Gazebo to design 3D artificial models and movement of the robot within these
   simulated models. This service also provides many out-of-box 3D artificial models to get started right away. 

#### Fleet Management

After developing the robot application and testing, applications will be required to be deployed to the physical robot
. AWS RoboMaker Fleet management service can register your robots. Once registered applications can be deployed to the
 robots over the air using AWS IoT Greengrass [sp20-516-223-aws-rm-greengrass] for both x86 and ARM based architectures.

## Getting Started

To get started, an AWS account is required [sp20-516-223-aws-account]. AWS account provides access to all AWS
 services including RoboMaker. In the chapter, we will demonstrate how to run a sample Hello World application using
  AWS RoboMaker.

:o2: RoboMaker sample simulation run for default 1 hour, so terminate the job once done to avoid charges or free-tier
 allowance usage.

### Hello World

To illustrate RoboMaker features, we will launch an out-of-box Hello World sample application [sp20-516-223-aws-rm-sample]. 

1. Login in to your AWS account.
2. From Services menu, search RoboMaker and select the AWS RoboMaker from suggestions.
3. From RoboMaker service page, click on "Try Sample Application" link. 
4. Under Sample Application Details, select the radio button for the application of your choice. In this chapter we
 will select Hello World. 
5. Expand the Default Settings section and adjust the setting according to your use case. For this demonstration we
 will leave the defaults.
6. Carefully review the licensing information [sp20-516-223-aws-rm-gs-info].
7. Click on "Launch simulation job" to launch the simulation. 
8. AWS will provision and integrate with required services in order to run the sample simulation. You can monitor and
 manage using [AWS RoboMaker console](https://console.aws.amazon.com/robomaker). After the sample application is
  created, you will be redirected to simulation job detail page. 
9. After the status of the simulation is changed to running, to launch and view the simulation, click on select
 Gazebo. This will launch the Gazebo client (gzclient) with the robot spinning clockwise in simulation environment.    

:o2: :TODO: CLI version to launch sample application, for e.g:

``` # Create Robot Application
$ aws robomaker create-robot-application --application hello-world-sample --robot-software-suite name=ROS,version=Melodic --sources architecture=X86_64,s3Bucket=awsrobomakerhelloworld-158121637282-bundlesbucket-7jgue1pq1k6u,s3Key=hello-world-robot.tar
```

### Code Repository

#### Hello World github location

The Hello World sample application code is available on [github] (https://github.com/aws-robotics/aws-robomaker-sample-application-helloworld).

## Pricing

Pricing of AWS RoboMaker depends majorly on the number of features used and other AWS services that are integrated with
 the robot application. As many services can be integrated, the pricing is bit complicated. 

* [Cloud extension for ROS](#Cloud-Extension-for-ROS) are free under the
 Apache Software License 2.0 and is a permissible licence with limited reuse
  restriction. However, you will incur standard AWS charges when the robot application uses other AWS services (like
   Polly, Lex, Rekognition etc.) through the cloud extension.

* [Development environment](#Development-environment) uses AWS Cloud 9 and charged at Standard AWS Cloud9 rates [sp20
-516-223-aws-rm-c9-price]. Cloud9 has no additional charges but only charges for compute and storage resources used
 to run and store the code respectively. 

* [Simulation](#Simulation) will be charged only when the simulation is used. Amazon charges per SU (Simulation
 Unit). One SU is 1 CPU and 2 GB of memory and charges $0.40/SU/Hour. Depending upon the number of SUs used for your
  simulation, the cost will be computed. In addition to SU, EC2 standard rates also will be added to the cost based
   on the network traffic generated by the simulation.

* [Fleet management](#Fleet-Management) uses Greengrass to deploy robot application OTA (over-the-air) and thus
 charges standard AWS Greengrass pricing [sp20-516-223-aws-rm-gg-price]. In general AWS Greengrass costs $0.16/Device
 /Month.

### Pricing Computation

We will demonstrate price computation of 2 Robots usage for 1 hour per day with no additional services.

### Cloud Extension Cost 

**Cloud Extension** will incur 0 cost as no additional services are used. 

### Development Environment Cost

Lets consider one person is developing the robot application and uses m4.large (8 GB) EC2 instance and 2 GB of
 storage completing the robot-application in 4 days. The cost can be computed as

Instance hours used: 8 hours/day * 4 days   = 32 hours

EC2 price/hour for m4.large                 = $0.10 

EC2 Total Charge                            = 32 * $0.10 = $3.2

EBS volume used: 2 GB                       = 2 * 1 = 2 **EBS is computed per month

Total EBS charges: 2 GB-month * $0.10/GB-month = $0.20

**Total Cost of Cloud9 Dev Environment**    = $3.2 + $0.2 = **$3.4**

### Simulation Cost

Lets consider that the developer uses 100 simulation hours with 2 SU. The cost can be computed as

Total SU-hours used: 100 hours * 2 SUs      = 200 SU-hours

RoboMaker simulation price per SU per hour  = $0.40

Total Simulation charges: 200 * $0.40       = $50

### Fleet Management Cost

Lets consider that we use 2 active Robots to manage. The cost can be computed as 

AWS Greengrass price per active device per month: $0.16

Total charges: 2 devices * $0.16/device = $0.32 

### Total Cost

**Total Overall Cost** for developing/testing/deploying and managing robot-application based on above assumptions
 will be

Total Cost = $3.4 + $50 + $0.32 = **$53.72**

### Additional Costing Details

For more detailed pricing explanation that includes other AWS services with 50 robots see <https://aws.amazon.com/robomaker/pricing/>

