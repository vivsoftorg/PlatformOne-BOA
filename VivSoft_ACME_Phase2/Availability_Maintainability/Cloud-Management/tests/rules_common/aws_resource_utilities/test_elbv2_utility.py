# eventParam.awsPartitionName = 'aws'
# eventParam.accNo = '107339370656' 

import os
import unittest
import datetime
from dateutil.tz import tzutc
from rules_common.aws_resource_utilities.elbv2_utility import Elbv2Utility
import common.compliance_object_factory as complianceobjectfactory
from common.compliance_object_factory import ComplianceObjectFactory
from common.common_constants import AWSResourceClassConstants, ComplianceConstants
from common.common_constants import BotoConstants
from common.boto_utility import BotoUtility
from tests.rules_common.aws_resource_utilities.test_rules_common_placebo_initializer import PlaceboMockResponseInitializer 


EVENT_JSON = {
    "configRuleId": "config-rule-1v52mx",
    "version": "1.0",
    "configRuleName": "aws-sample-rule",
    "configRuleArn": "arn:aws:config:us-east-1:411815166437:config-rule/config-rule-1v52mx",
    "invokingEvent": "{\n  \"configurationItemDiff\": null,\n  \"configurationItem\": {\n    \"relatedEvents\": [],\n    \"relationships\": [\n      {\n        \"resourceId\": \"eni-3cc64fd2\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::NetworkInterface\",\n        \"name\": \"Contains NetworkInterface\"\n      },\n      {\n        \"resourceId\": \"sg-056a2f78\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::SecurityGroup\",\n        \"name\": \"Is associated with SecurityGroup\"\n      },\n      {\n        \"resourceId\": \"sg-33178157\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::SecurityGroup\",\n        \"name\": \"Is associated with SecurityGroup\"\n      },\n      {\n        \"resourceId\": \"subnet-e41559ad\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::Subnet\",\n        \"name\": \"Is contained in Subnet\"\n      },\n      {\n        \"resourceId\": \"vol-03807f5f89a1b3d0b\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::Volume\",\n        \"name\": \"Is attached to Volume\"\n      },\n      {\n        \"resourceId\": \"vpc-a02ce1c6\",\n        \"resourceName\": null,\n        \"resourceType\": \"AWS::EC2::VPC\",\n        \"name\": \"Is contained in Vpc\"\n      }\n    ],\n    \"configuration\": {\n      \"instanceId\": \"i-098f9826f1ee4072d\",\n      \"imageId\": \"ami-a4c7edb2\",\n      \"state\": {\n        \"code\": 16,\n        \"name\": \"running\"\n      },\n      \"privateDnsName\": \"ip-172-31-28-156.ec2.internal\",\n      \"publicDnsName\": \"ec2-54-235-57-47.compute-1.amazonaws.com\",\n      \"stateTransitionReason\": \"\",\n      \"keyName\": \"REAN_GAURAVASHTIKAR_VIRGINIA_KEYPAIR\",\n      \"amiLaunchIndex\": 0,\n      \"productCodes\": [],\n      \"instanceType\": \"t2.nano\",\n      \"launchTime\": \"2017-07-09T17:34:48.000Z\",\n      \"placement\": {\n        \"availabilityZone\": \"us-east-1b\",\n        \"groupName\": \"\",\n        \"tenancy\": \"default\",\n        \"hostId\": null,\n        \"affinity\": null\n      },\n      \"kernelId\": null,\n      \"ramdiskId\": null,\n      \"platform\": null,\n      \"monitoring\": {\n        \"state\": \"disabled\"\n      },\n      \"subnetId\": \"subnet-29aa575e\",\n      \"vpcId\": \"vpc-c5ec30a0\",\n      \"privateIpAddress\": \"172.31.28.156\",\n      \"publicIpAddress\": \"54.235.57.47\",\n      \"stateReason\": null,\n      \"architecture\": \"x86_64\",\n      \"rootDeviceType\": \"ebs\",\n      \"rootDeviceName\": \"/dev/sda1\",\n      \"blockDeviceMappings\": [\n        {\n          \"deviceName\": \"/dev/sda1\",\n          \"ebs\": {\n            \"volumeId\": \"vol-0bc42d36aa49858fd\",\n            \"status\": \"attached\",\n            \"attachTime\": \"2017-01-10T06:29:11.000Z\",\n            \"deleteOnTermination\": true\n          }\n        }\n      ],\n      \"virtualizationType\": \"hvm\",\n      \"instanceLifecycle\": null,\n      \"spotInstanceRequestId\": null,\n      \"clientToken\": \"FSRse1484029749587\",\n      \"tags\": [\n        {\n          \"key\": \"Project\",\n          \"value\": \"mnc\"\n        },\n        {\n          \"key\": \"Environment\",\n          \"value\": \"Testing\"\n        },\n        {\n          \"key\": \"Owner\",\n          \"value\": \"gaurav.ashtikar\"\n        },\n        {\n          \"key\": \"Name\",\n          \"value\": \"Gaurav-Test-Machine\"\n        },\n        {\n          \"value\": \"NoShutdown\",\n          \"key\": \"true\"\n        },\n        {\n          \"key\": \"ExpirationDate\",\n          \"value\": \"2017-07-10\"\n        }\n      ],\n      \"securityGroups\": [\n        {\n          \"groupName\": \"gaurav-test-sg\",\n          \"groupId\": \"sg-da9da1aa\"\n        }\n      ],\n      \"sourceDestCheck\": true,\n      \"hypervisor\": \"xen\",\n      \"networkInterfaces\": [\n        {\n          \"networkInterfaceId\": \"eni-3cc64fd2\",\n          \"subnetId\": \"subnet-e41559ad\",\n          \"vpcId\": \"vpc-a02ce1c6\",\n          \"description\": \"Primary network interface\",\n          \"ownerId\": \"411815166437\",\n          \"status\": \"in-use\",\n          \"macAddress\": \"0a:18:41:09:07:34\",\n          \"privateIpAddress\": \"10.16.3.63\",\n          \"privateDnsName\": \"ip-10-16-3-63.ec2.internal\",\n          \"sourceDestCheck\": true,\n          \"groups\": [\n            {\n              \"groupName\": \"launch-wizard-92\",\n              \"groupId\": \"sg-da9da1aa\"\n            }\n          ],\n          \"attachment\": {\n            \"attachmentId\": \"eni-attach-29cd5d69\",\n            \"deviceIndex\": 0,\n            \"status\": \"attached\",\n            \"attachTime\": \"2017-01-10T06:29:10.000Z\",\n            \"deleteOnTermination\": true\n          },\n          \"association\": null,\n          \"privateIpAddresses\": [\n            {\n              \"privateIpAddress\": \"10.16.3.63\",\n              \"privateDnsName\": \"ip-10-16-3-63.ec2.internal\",\n              \"primary\": true,\n              \"association\": null\n            }\n          ],\n          \"ipv6Addresses\": []\n        }\n      ],\n      \"iamInstanceProfile\": {\n        \"arn\": \"arn:aws:iam::411815166437:instance-profile/jenkins_master_noel.georgi\",\n        \"id\": \"AIPAJ4KIXV5QRL25MMMCK\"\n      },\n      \"ebsOptimized\": false,\n      \"sriovNetSupport\": null,\n      \"enaSupport\": null\n    },\n    \"supplementaryConfiguration\": {},\n    \"tags\": {\n      \"Project\": \"mnc\",\n      \"Owner\": \"gaurav.ashtikar\",\n      \"ExpirationDate\": \"2017-07-11\",\n      \"Environment\": \"Testing\",\n      \"NoShutdown\": \"true\",\n      \"Name\": \"Gaurav-Test-Machine\"\n    },\n    \"configurationItemVersion\": \"1.2\",\n    \"configurationItemCaptureTime\": \"2017-05-18T18:47:14.686Z\",\n    \"configurationStateId\": 1495133234686,\n    \"awsAccountId\": \"411815166437\",\n    \"configurationItemStatus\": \"OK\",\n    \"resourceType\": \"AWS::EC2::Instance\",\n    \"resourceId\": \"i-098f9826f1ee4072d\",\n    \"resourceName\": null,\n    \"ARN\": \"arn:aws:ec2:us-east-1:411815166437:instance/i-098f9826f1ee4072d\",\n    \"awsRegion\": \"us-east-1\",\n    \"availabilityZone\": \"us-east-1b\",\n    \"configurationStateMd5Hash\": \"ed5fe5d85665e3be3607c27aa50fa0ea\",\n    \"resourceCreationTime\": \"2017-05-13T14:14:48.000Z\"\n  },\n  \"notificationCreationTime\": \"2017-05-19T08:40:15.976Z\",\n  \"messageType\": \"ConfigurationItemChangeNotification\",\n  \"recordVersion\": \"1.2\"\n}",
    "resultToken": "",
    "eventLeftScope": "False",
    "ruleParameters": "{\"environmentValues\": \"Staging,Preproduction,Production,Testing\",\"performAction\": \"True\",\"notifier\": \"sns\",\"toEmail\": \"gaurav.ashtikar@reancloud.com\"}",
    "executionRoleArn": "arn:aws:iam::411815166437:role/awsconfig-role",
    "accountId": "411815166437"
}

CONTEXT = ""
RESOURCE_TYPE_ELB_V2 = AWSResourceClassConstants.ELB_V2_RESOURCE
RESOURCE_ID_ELB_V2 = 'arn:aws:elasticloadbalancing:us-east-1:107339370656:loadbalancer/app/vaibhavALBMNCTESTCOPYRULE/c01bcf796c5611d6'
CONFIG_EVENT = {'loadbalancerarn': 'arn:aws:elasticloadbalancing:us-east-1:107339370656:loadbalancer/app/vaibhavALBMNCTESTCOPYRULE/c01bcf796c5611d6', 'dnsname': 'vaibhavALBMNCTESTCOPYRULE-1987971516.us-east-1.elb.amazonaws.com', 'canonicalhostedzoneid': 'Z35SXDOTRQ7X7K', 'createdtime': datetime.datetime(2018, 10, 23, 7, 2, 58, 20000, tzinfo=tzutc()), 'loadbalancername': 'vaibhavALBMNCTESTCOPYRULE', 'scheme': 'internet-facing', 'vpcid': 'vpc-38738c43', 'state': {'code': 'active'}, 'type': 'application', 'availabilityzones': [{'zonename': 'us-east-1a', 'subnetid': 'subnet-7b8dbc1f'}, {'zonename': 'us-east-1b', 'subnetid': 'subnet-eecf8dc1'}], 'securitygroups': ['sg-03ab796da1406111e', 'sg-0ac3bbd40cade08f0'], 'ipaddresstype': 'ipv4', 'region': 'us-east-1', 'missingTagsTargetGroups': [{'ResourceArn': 'arn:aws:elasticloadbalancing:us-east-1:107339370656:targetgroup/vaibhavMNCTargetGroup/8b41b3e1be1d905f', 'Tags': [{'key': 'Name', 'value': 'vaibhavCopyTestNAMETag'}], 'tagsToAdd': [{'key': 'Project', 'value': 'MNC'}, {'key': 'ExpirationDate', 'value': '2018-10-30'}]}]}
CONFIG_EVENT_WO_MISSINGTAGS = {'loadbalancerarn': 'arn:aws:elasticloadbalancing:us-east-1:107339370656:loadbalancer/app/vaibhavALBMNCTESTCOPYRULE/c01bcf796c5611d6', 'dnsname': 'vaibhavALBMNCTESTCOPYRULE-1987971516.us-east-1.elb.amazonaws.com', 'canonicalhostedzoneid': 'Z35SXDOTRQ7X7K', 'createdtime': datetime.datetime(2018, 10, 23, 7, 2, 58, 20000, tzinfo=tzutc()), 'loadbalancername': 'vaibhavALBMNCTESTCOPYRULE', 'scheme': 'internet-facing', 'vpcid': 'vpc-38738c43', 'state': {'code': 'active'}, 'type': 'application', 'availabilityzones': [{'zonename': 'us-east-1a', 'subnetid': 'subnet-7b8dbc1f'}, {'zonename': 'us-east-1b', 'subnetid': 'subnet-eecf8dc1'}], 'securitygroups': ['sg-03ab796da1406111e', 'sg-0ac3bbd40cade08f0'], 'ipaddresstype': 'ipv4', 'region': 'us-east-1'}

class TestElbv2Utility(unittest.TestCase):

    def testElbv2UtilityDescribeLoadBalncerSucees(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'describe_load_balancers_success')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)  
        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = Elbv2Utility.describeLoadBalancers(eventParam=eventParam)

        assert return_value

    def testElbv2UtilityDescribeLoadBalncerFailure(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'describe_load_balancers_failure')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)  
        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = Elbv2Utility.describeLoadBalancers(eventParam=eventParam)

        assert not return_value

    def testElbv2UtilityAddTagsToResourceSucees(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'add_tags_to_resource_success')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)

        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        eventItem = ComplianceObjectFactory.createAWSConfigEventItemfrom(resourceId=RESOURCE_ID_ELB_V2, resourceType=RESOURCE_TYPE_ELB_V2, configItems=CONFIG_EVENT)
        resourceListWithTags = eventItem.configItems['missingTagsTargetGroups']

        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = Elbv2Utility.addTagsToResource(eventParam=eventParam, eventItem=eventItem, resourceListWithTags=resourceListWithTags)
        assert return_value.complianceType == ComplianceConstants.COMPLIANT_RESOURCE

    def testElbv2UtilityAddTagsToResourceFailure(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'add_tags_to_resource_success')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)

        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        eventItem = ComplianceObjectFactory.createAWSConfigEventItemfrom(resourceId=RESOURCE_ID_ELB_V2, resourceType=RESOURCE_TYPE_ELB_V2, configItems=CONFIG_EVENT)
        errorResourceListWithTags = [{}]
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)
        return_value = Elbv2Utility.addTagsToResource(eventParam=eventParam, eventItem=eventItem, resourceListWithTags=errorResourceListWithTags)
        assert return_value.complianceType == ComplianceConstants.MNC_ACTION_EXCEPTION

    def testElbV2DescribeTargetGroupsSuccess(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'describe_target_groups_success')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)

        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        awsPartitionName = eventParam.awsPartitionName
        albClient = BotoUtility.getClient(
            BotoConstants.BOTO_CLIENT_AWS_ELB_V2,
            eventParam.accNo,
            BotoConstants.BOTO_CLIENT_READ_TYPE_ROLE,
            awsPartitionName,
            'us-east-1'
        )

        return_value = Elbv2Utility.describeTargetGroupsForElb(elbV2Client=albClient, elbV2Arn=RESOURCE_TYPE_ELB_V2)
        assert return_value

    def testElbV2DescribeTargetGroupsFailure(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'describe_target_groups_failure')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)

        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        awsPartitionName = eventParam.awsPartitionName
        albClient = BotoUtility.getClient(
            BotoConstants.BOTO_CLIENT_AWS_ELB_V2,
            eventParam.accNo,
            BotoConstants.BOTO_CLIENT_READ_TYPE_ROLE,
            awsPartitionName,
            'us-east-1'
        )

        return_value = Elbv2Utility.describeTargetGroupsForElb(elbV2Client=albClient, elbV2Arn=RESOURCE_TYPE_ELB_V2)
        assert not return_value


    def testElbV2DescribeTagsSuccess(self):
        recordedMockResponsePath = os.path.join(os.getcwd(), 'tests', 'rules_common', 'aws_resource_utilities', 'placebo_recorded_responses' , 'elbv2_utility', 'describe_tags')
        PlaceboMockResponseInitializer.replaying_pill(recordedMockResponsePath)

        eventParam = complianceobjectfactory.ComplianceObjectFactory.createEventParamFrom(
            EVENT_JSON,
            CONTEXT
        )

        awsPartitionName = eventParam.awsPartitionName
        albClient = BotoUtility.getClient(
            BotoConstants.BOTO_CLIENT_AWS_ELB_V2,
            eventParam.accNo,
            BotoConstants.BOTO_CLIENT_READ_TYPE_ROLE,
            awsPartitionName,
            'us-east-1'
        )

        return_value = Elbv2Utility.describeTags(elbV2Client=albClient, resourceArnList=[RESOURCE_TYPE_ELB_V2])
        assert return_value